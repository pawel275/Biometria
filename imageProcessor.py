from PySide.QtCore import *
from PySide.QtGui import *
import luts
import copy


class ImageProcessor:
    def __init__(self, main_window):
        self._mw = main_window

    def filter_red(self):
        self._mw.images_manager.apply_lut(g=luts.zero(), b=luts.zero())

    def filter_green(self):
        self._mw.images_manager.apply_lut(r=luts.zero(), b=luts.zero())

    def filter_blue(self):
        self._mw.images_manager.apply_lut(r=luts.zero(), g=luts.zero())

    def exponential_lut(self):
        dialog = Dialog(self._mw, "Enter exponent", ("exp",))
        dialog.spin_boxes["exp"].setMinimum(0)
        dialog.spin_boxes["exp"].setMaximum(100)
        if dialog.exec_():
            self._mw.images_manager.apply_lut(luts.exp(dialog.values()["exp"]))

    def logarithmic_lut(self):
        dialog = Dialog(self._mw, "Enter base of logarithm", ("base",))
        dialog.spin_boxes["base"].setMinimum(0.01)
        dialog.spin_boxes["base"].setMaximum(100)
        if dialog.exec_():
            self._mw.images_manager.apply_lut(luts.exp(dialog.values()["base"]))

    def hist_stretch(self):
        dialog = Dialog(self._mw, "Enter min and max values", ("min", "max",))
        dialog.spin_boxes["min"].setMinimum(0)
        dialog.spin_boxes["min"].setMaximum(255)
        dialog.spin_boxes["max"].setMinimum(0)
        dialog.spin_boxes["max"].setMaximum(255)
        if dialog.exec_():
            a, b = dialog.values()["min"], dialog.values()["max"]
            self._mw.images_manager.apply_lut(luts.hist_stretch(a, b))

    def hist_eq(self):
        bits = self._mw.images_manager.processed_img.bits()
        r, g, b = bits[2::4], bits[1::4], bits[::4]
        self._mw.images_manager.apply_lut(r=luts.hist_eq(r), g=luts.hist_eq(g), b=luts.hist_eq(b))

    def grayscale(self):
        # print(self._mw.images_manager.processed_img.isGrayscale())
        bits = self._mw.images_manager.processed_img.bits()
        for i in range(0, len(bits), 4):
            bits[i] = (bits[i] + bits[i + 1] + bits[i + 2]) // 3
            bits[i + 2] = bits[i + 1] = bits[i]
        self._mw.iv_processed.refresh()

    def custom_thresholding(self):
        dialog = Dialog(self._mw, "Enter threshold", ("threshold",))
        dialog.spin_boxes["threshold"].setMinimum(0)
        dialog.spin_boxes["threshold"].setMaximum(255)
        if dialog.exec_():
            if not self._mw.images_manager.processed_img.isGrayscale():
                self.grayscale()
            self._mw.images_manager.apply_lut(luts.threshold(dialog.values()["threshold"]))

    def otsu_thresholding(self):
        if not self._mw.images_manager.processed_img.isGrayscale():
            self.grayscale()
        bits = self._mw.images_manager.processed_img.bits()
        n = len(bits) / 4
        hist = 256 * [0]
        for i in range(0, len(bits), 4):
            hist[bits[i]] += 1
        s = sum(hist[i] * i for i in range(256))
        w = maximum = threshold = s0 = 0
        for i in range(256):
            w += hist[i]
            if n == w:
                break
            if w != 0:
                s0 += i * hist[i]
                between = (s0 * n - s * w) ** 2 / w / (n - w)
                if between > maximum:
                    threshold = i
                    maximum = between
        print(threshold)
        self._mw.images_manager.apply_lut(luts.threshold(threshold))

    def niblack_thresholding(self):
        dialog = Dialog(self._mw, "Enter block size and k", ("size", "k",))
        dialog.spin_boxes["k"].setMinimum(-1)
        dialog.spin_boxes["k"].setMaximum(0)
        if dialog.exec_():
            if not self._mw.images_manager.processed_img.isGrayscale():
                self.grayscale()
            img = self._mw.images_manager.processed_img
            colors = img.bits()[::4]
            w, h = img.width(), img.height()
            size, k = int(dialog.values()["size"]), dialog.values()["k"]
            thresholds = len(colors) * [0]
            for i in range(len(colors)):
                x, y = i % w, i // w
                x0, y0 = x - size // 2, y - size // 2
                block = []
                for y1 in range(y0, y0 + size):
                    for x1 in range(x0, x0 + size):
                        if 0 <= x1 < w and 0 <= y1 < h:
                            block.append(y1 * w + x1)
                block = list(map(lambda a: colors[a], block))
                m = sum(block) / len(block)
                d = (sum(map(lambda a: (a - m) ** 2, block)) / len(block)) ** 0.5
                thresholds[i] = int(m + k * d)
            bits = img.bits()
            for i, v in enumerate(thresholds):
                c = 0 if colors[i] <= v else 255
                bits[4 * i] = c
                bits[4 * i + 1] = c
                bits[4 * i + 2] = c
            self._mw.iv_processed.refresh()

    def _apply_mask(self, mask_size, operation):
        img = self._mw.images_manager.processed_img
        bits = img.bits()
        bits_copy = copy.deepcopy(list(bits))
        red, green, blue = [], [], []
        for y in range(img.height()):
            for x in range(img.width()):
                del red[:]
                del green[:]
                del blue[:]
                for my in range(mask_size):
                    for mx in range(mask_size):
                        x0, y0 = abs(x + mx - mask_size // 2), abs(y + my - mask_size // 2)
                        if x0 >= img.width():
                            x0 -= 2 * mx
                        if y0 >= img.height():
                            y0 -= 2 * my
                        p0 = (y0 * img.width() + x0) * 4
                        red.append(bits_copy[p0])
                        green.append(bits_copy[p0 + 1])
                        blue.append(bits_copy[p0 + 2])
                p = (y * img.width() + x) * 4
                bits[p] = min(255, max(operation(red), 0))
                bits[p + 1] = min(255, max(operation(green), 0))
                bits[p + 2] = min(255, max(operation(blue), 0))
        self._mw.iv_processed.refresh()

    def linear_filter(self):
        size_dialog = Dialog(self._mw, "Enter matrix size", ("size",))
        size_dialog.spin_boxes["size"].setMinimum(3)
        if size_dialog.exec_():
            size = size_dialog.values()["size"]
            if size % 2 != 1:
                msg_box = QMessageBox(self._mw)
                msg_box.setText("Invalid size")
                msg_box.exec_()
                return
            size = int(size)
            matrix_dialog = MatrixDialog(self._mw, size, "Enter values")
            if matrix_dialog.exec_():
                mask = matrix_dialog.values()
                mask_sum = sum(sum(row) for row in mask)
                if mask_sum != 0:
                    mask = list(map(lambda row: list(map(lambda v: v / mask_sum, row)), mask))

                def operation(array):
                    val = 0
                    for y in range(size):
                        for x in range(size):
                            val += array[y*size+x] * mask[x][y]
                    return int(val)

                self._apply_mask(size, operation)

    def median_filter(self):
        size_dialog = Dialog(self._mw, "Enter matrix size", ("size",))
        size_dialog.spin_boxes["size"].setMinimum(3)
        if size_dialog.exec_():
            size = size_dialog.values()["size"]
            if size % 2 != 1:
                msg_box = QMessageBox(self._mw)
                msg_box.setText("Invalid size")
                msg_box.exec_()
                return
            size = int(size)
            self._apply_mask(size, lambda arr: sorted(arr)[len(arr) // 2])

    def kuwahara_filter(self):
        size_dialog = Dialog(self._mw, "Enter matrix size", ("size",))
        size_dialog.spin_boxes["size"].setMinimum(3)
        if size_dialog.exec_():
            size = size_dialog.values()["size"]
            if size % 2 != 1:
                msg_box = QMessageBox(self._mw)
                msg_box.setText("Invalid size")
                msg_box.exec_()
                return
            size = int(size)

            def operation(arr):
                r = [[], [], [], []]
                for i, x in enumerate(arr):
                    if i <= len(arr) // 2:
                        if i % size <= size // 2:
                            r[0].append(x)
                        if i % size >= size // 2:
                            r[1].append(x)
                    if i >= len(arr) // 2:
                        if i % size <= size // 2:
                            r[2].append(x)
                        if i % size >= size // 2:
                            r[3].append(x)
                rsize = (size // 2 + 1) ** 2
                m = [sum(a) / rsize for a in r]
                v = [sum((b - m[i]) ** 2 for b in a) / rsize for i, a in enumerate(r)]
                return int(m[v.index(min(v))])

            self._apply_mask(size, operation)


class Dialog(QDialog):
    def __init__(self, parent=None, label="", values=()):
        super(Dialog, self).__init__(parent)
        self._value_names = values
        self._labels = {}
        self.spin_boxes = {}
        layout = QGridLayout()
        layout.addWidget(QLabel(label), 0, 0, 1, 2)
        for i, name in enumerate(self._value_names):
            self._labels[name] = QLabel(name)
            self.spin_boxes[name] = QDoubleSpinBox()
            layout.addWidget(self._labels[name], i + 1, 0)
            layout.addWidget(self.spin_boxes[name], i + 1, 1)
        btn_ok = QPushButton("Ok")
        btn_cancel = QPushButton("Cancel")
        layout.addWidget(btn_ok)
        layout.addWidget(btn_cancel)
        self.setLayout(layout)
        self.connect(btn_ok, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(btn_cancel, SIGNAL("clicked()"), self, SLOT("reject()"))

    def values(self):
        vals = {}
        for name in self._value_names:
            vals[name] = self.spin_boxes[name].value()
        return vals


class MatrixDialog(QDialog):
    def __init__(self, parent, size, label=""):
        super(MatrixDialog, self).__init__(parent)
        layout = QGridLayout()
        layout.addWidget(QLabel(label), 0, 0, 1, size)
        self.matrix = [[QDoubleSpinBox() for i in range(size)] for j in range(size)]
        for row in self.matrix:
            for sb in row:
                sb.setMinimum(-100)
        for y in range(size):
            for x in range(size):
                layout.addWidget(self.matrix[x][y], y + 1, x)
        btn_ok = QPushButton("Ok")
        btn_cancel = QPushButton("Cancel")
        layout.addWidget(btn_ok)
        layout.addWidget(btn_cancel)
        self.setLayout(layout)
        self.connect(btn_ok, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(btn_cancel, SIGNAL("clicked()"), self, SLOT("reject()"))

    def values(self):
        return list(map(lambda row: list(map(lambda v: v.value(), row)), self.matrix))
