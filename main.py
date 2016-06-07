import sys
import matplotlib.pyplot as plt
from PySide.QtCore import *
from PySide.QtGui import *
from ui import ui_main
from imagesManager import ImagesManager
from imageProcessor import ImageProcessor
import tkinter.filedialog
import luts


class MainWindow(QMainWindow, ui_main.Ui_MainWindow):
    original_img = None
    processed_img = None
    images_manager = None
    image_processor = None
    _zoom = 1.0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # plt.switch_backend("QT4Agg")
        self.images_manager = ImagesManager(self)
        self.image_processor = ImageProcessor(self)

        self.action_quit.activated.connect(sys.exit)
        self.action_open.activated.connect(self.images_manager.load)
        self.action_save.activated.connect(self.images_manager.save)

        self.action_revert.activated.connect(self.images_manager.revert_changes)

        self.action_filter_red.activated.connect(self.image_processor.filter_red)
        self.action_filter_green.activated.connect(self.image_processor.filter_green)
        self.action_filter_blue.activated.connect(self.image_processor.filter_blue)
        self.action_grayscale.activated.connect(self.image_processor.grayscale)

        self.iv_original.mouse_moved.connect(self.update_mouse_status)
        self.iv_processed.mouse_moved.connect(self.update_mouse_status)
        self.iv_processed.mouse_dragged.connect(self.images_manager.put_pixel)

        self.action_zoom_in.activated.connect(lambda *args: self.zoom(2))
        self.action_zoom_out.activated.connect(lambda *args: self.zoom(0.5))

        self.action_select_pen_color.activated.connect(self.images_manager.select_pen_color)
        self.action_histogram.activated.connect(self.display_histogram)

        self.action_exp.activated.connect(self.image_processor.exponential_lut)
        self.action_log.activated.connect(self.image_processor.logarithmic_lut)
        self.action_hist_stretch.activated.connect(self.image_processor.hist_stretch)
        self.action_hist_eq.activated.connect(self.image_processor.hist_eq)
        self.action_custom_thresholding.activated.connect(self.image_processor.custom_thresholding)
        self.action_otsu_thresholding.activated.connect(self.image_processor.otsu_thresholding)
        self.action_niblack_thresholding.activated.connect(self.image_processor.niblack_thresholding)

        self.action_linear_filter.activated.connect(self.image_processor.linear_filter)
        self.action_median_filter.activated.connect(self.image_processor.median_filter)
        self.action_kuwahara_filter.activated.connect(self.image_processor.kuwahara_filter)

    def update_mouse_status(self, x, y):
        self.lbl_position.setText("X:%d Y:%d" % (x, y))
        o = self.images_manager.original_img.pixel(x, y)
        self.lbl_original_color.setText("R:%d G:%d B:%d" % (qRed(o), qGreen(o), qBlue(o)))
        p = self.images_manager.processed_img.pixel(x, y)
        self.lbl_processed_color.setText("R:%d G:%d B:%d" % (qRed(p), qGreen(p), qBlue(p)))

    def zoom(self, zoom):
        self._zoom *= zoom
        self.iv_original.scale(zoom, zoom)
        self.iv_processed.scale(zoom, zoom)
        self.lbl_zoom.setText("x" + str(self._zoom))

    def display_histogram(self):
        arr = self.images_manager.processed_img.bits()
        plt.subplot(221)
        plt.hist(arr[2::4], bins=256, color="red", range=(0, 255))
        plt.xlabel("intensity")
        plt.ylabel("red")
        plt.subplot(222)
        plt.hist(arr[1::4], bins=256, color="green", range=(0, 255))
        plt.xlabel("intensity")
        plt.ylabel("green")
        plt.subplot(223)
        plt.hist(arr[0::4], bins=256, color="blue", range=(0, 255))
        plt.xlabel("intensity")
        plt.ylabel("blue")
        plt.subplot(224)
        plt.hist([sum(arr[i:i + 3]) // 3 for i in range(0, len(arr), 4)], bins=256, color="grey", range=(0, 255))
        plt.xlabel("intensity")
        plt.ylabel("(R+G+B)/3")
        # plt.get_current_fig_manager().window.showMaximized()
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    sys.exit(0)
