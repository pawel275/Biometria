from PySide.QtCore import *
from PySide.QtGui import *
from io import BytesIO
from PIL import Image


class ImagesManager:
    original_img = None
    processed_img = None
    pen_color = qRgb(0, 0, 0)

    def __init__(self, main_window):
        self._main_window = main_window

    def select_pen_color(self):
        color = QColorDialog.getColor()
        self.pen_color = color.rgb()
        c = self.pen_color
        self._main_window.lbl_selected_color.setText("R:%d G:%d B:%d" % (qRed(c), qGreen(c), qBlue(c)))

    def put_pixel(self, x, y):
        self.processed_img.setPixel(x, y, self.pen_color)
        self._main_window.iv_processed.refresh()

    def apply_lut(self, rgb=None, r=None, g=None, b=None):
        bits = self.processed_img.bits()
        if rgb:
            for i in range(0, len(bits), 4):
                bits[i] = rgb[bits[i]]
                bits[i + 1] = rgb[bits[i + 1]]
                bits[i + 2] = rgb[bits[i + 2]]
        else:
            for i, c in enumerate((b, g, r)):
                if c:
                    for j in range(0, len(bits), 4):
                        bits[i + j] = c[bits[i + j]]
        self._main_window.iv_processed.refresh()

    def revert_changes(self):
        self.processed_img = self.original_img.copy()
        self._main_window.iv_processed.set_image(self.processed_img)

    def load(self):
        file = QFileDialog.getOpenFileName(self._main_window, "Open image",
                                           filter="JPEG Image (*.jpg);;TIFF Image (*.tif);;GIF Image(*.gif);;PNG(*.png)")
        self.original_img = QImage(file[0])
        self.processed_img = self.original_img.copy()
        self._main_window.iv_original.set_image(self.original_img)
        self._main_window.iv_processed.set_image(self.processed_img)

    def save(self):
        file = QFileDialog.getSaveFileName(self._main_window, "Save Image",
                                           filter="JPEG Image (*.jpg);;TIFF Image (*.tif);;GIF Image(*.gif)")
        if "gif" in file[1]:
            buffer = QBuffer()
            buffer.open(QIODevice.ReadWrite)
            self.processed_img.save(buffer, "PNG")
            img_data = BytesIO()
            img_data.write(buffer.data().data())
            buffer.close()
            img_data.seek(0)
            pil_im = Image.open(img_data)
            pil_im.save(file[0])
        else:
            self.processed_img.save(file[0])
