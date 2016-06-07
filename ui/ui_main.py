# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_main.ui'
#
# Created: Sat Apr  9 16:26:16 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 482)
        MainWindow.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.iv_original = ImageView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iv_original.sizePolicy().hasHeightForWidth())
        self.iv_original.setSizePolicy(sizePolicy)
        self.iv_original.setObjectName("iv_original")
        self.gridLayout.addWidget(self.iv_original, 2, 0, 1, 1)
        self.iv_processed = ImageView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iv_processed.sizePolicy().hasHeightForWidth())
        self.iv_processed.setSizePolicy(sizePolicy)
        self.iv_processed.setObjectName("iv_processed")
        self.gridLayout.addWidget(self.iv_processed, 2, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.StatusBarLayout = QtGui.QHBoxLayout()
        self.StatusBarLayout.setObjectName("StatusBarLayout")
        self.PositionLayout = QtGui.QHBoxLayout()
        self.PositionLayout.setObjectName("PositionLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.PositionLayout.addWidget(self.label)
        self.lbl_position = QtGui.QLabel(self.centralwidget)
        self.lbl_position.setText("")
        self.lbl_position.setObjectName("lbl_position")
        self.PositionLayout.addWidget(self.lbl_position)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.PositionLayout.addItem(spacerItem)
        self.StatusBarLayout.addLayout(self.PositionLayout)
        self.OriginalColorLayout = QtGui.QHBoxLayout()
        self.OriginalColorLayout.setObjectName("OriginalColorLayout")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.OriginalColorLayout.addWidget(self.label_2)
        self.lbl_original_color = QtGui.QLabel(self.centralwidget)
        self.lbl_original_color.setText("")
        self.lbl_original_color.setObjectName("lbl_original_color")
        self.OriginalColorLayout.addWidget(self.lbl_original_color)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.OriginalColorLayout.addItem(spacerItem1)
        self.StatusBarLayout.addLayout(self.OriginalColorLayout)
        self.ProcessedColorLayout = QtGui.QHBoxLayout()
        self.ProcessedColorLayout.setObjectName("ProcessedColorLayout")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.ProcessedColorLayout.addWidget(self.label_3)
        self.lbl_processed_color = QtGui.QLabel(self.centralwidget)
        self.lbl_processed_color.setText("")
        self.lbl_processed_color.setObjectName("lbl_processed_color")
        self.ProcessedColorLayout.addWidget(self.lbl_processed_color)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ProcessedColorLayout.addItem(spacerItem2)
        self.StatusBarLayout.addLayout(self.ProcessedColorLayout)
        self.SelectedColorLayout = QtGui.QHBoxLayout()
        self.SelectedColorLayout.setObjectName("SelectedColorLayout")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.SelectedColorLayout.addWidget(self.label_7)
        self.lbl_selected_color = QtGui.QLabel(self.centralwidget)
        self.lbl_selected_color.setObjectName("lbl_selected_color")
        self.SelectedColorLayout.addWidget(self.lbl_selected_color)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.SelectedColorLayout.addItem(spacerItem3)
        self.PositionLayout_2 = QtGui.QHBoxLayout()
        self.PositionLayout_2.setObjectName("PositionLayout_2")
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.PositionLayout_2.addWidget(self.label_6)
        self.lbl_zoom = QtGui.QLabel(self.centralwidget)
        self.lbl_zoom.setObjectName("lbl_zoom")
        self.PositionLayout_2.addWidget(self.lbl_zoom)
        self.SelectedColorLayout.addLayout(self.PositionLayout_2)
        self.StatusBarLayout.addLayout(self.SelectedColorLayout)
        self.verticalLayout_2.addLayout(self.StatusBarLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuColors = QtGui.QMenu(self.menubar)
        self.menuColors.setObjectName("menuColors")
        self.menuZoom = QtGui.QMenu(self.menubar)
        self.menuZoom.setObjectName("menuZoom")
        self.menuProcessing = QtGui.QMenu(self.menubar)
        self.menuProcessing.setObjectName("menuProcessing")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_save = QtGui.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_quit = QtGui.QAction(MainWindow)
        self.action_quit.setObjectName("action_quit")
        self.action_select_pen_color = QtGui.QAction(MainWindow)
        self.action_select_pen_color.setObjectName("action_select_pen_color")
        self.action_filter_red = QtGui.QAction(MainWindow)
        self.action_filter_red.setCheckable(False)
        self.action_filter_red.setChecked(False)
        self.action_filter_red.setObjectName("action_filter_red")
        self.action_filter_green = QtGui.QAction(MainWindow)
        self.action_filter_green.setCheckable(False)
        self.action_filter_green.setChecked(False)
        self.action_filter_green.setObjectName("action_filter_green")
        self.action_filter_blue = QtGui.QAction(MainWindow)
        self.action_filter_blue.setCheckable(False)
        self.action_filter_blue.setChecked(False)
        self.action_filter_blue.setObjectName("action_filter_blue")
        self.action_zoom_in = QtGui.QAction(MainWindow)
        self.action_zoom_in.setSoftKeyRole(QtGui.QAction.NoSoftKey)
        self.action_zoom_in.setObjectName("action_zoom_in")
        self.action_zoom_out = QtGui.QAction(MainWindow)
        self.action_zoom_out.setObjectName("action_zoom_out")
        self.action_exp = QtGui.QAction(MainWindow)
        self.action_exp.setObjectName("action_exp")
        self.action_revert = QtGui.QAction(MainWindow)
        self.action_revert.setObjectName("action_revert")
        self.action_histogram = QtGui.QAction(MainWindow)
        self.action_histogram.setObjectName("action_histogram")
        self.action_log = QtGui.QAction(MainWindow)
        self.action_log.setObjectName("action_log")
        self.action_hist_stretch = QtGui.QAction(MainWindow)
        self.action_hist_stretch.setObjectName("action_hist_stretch")
        self.action_hist_eq = QtGui.QAction(MainWindow)
        self.action_hist_eq.setObjectName("action_hist_eq")
        self.action_grayscale = QtGui.QAction(MainWindow)
        self.action_grayscale.setObjectName("action_grayscale")
        self.action_custom_thresholding = QtGui.QAction(MainWindow)
        self.action_custom_thresholding.setObjectName("action_custom_thresholding")
        self.action_otsu_thresholding = QtGui.QAction(MainWindow)
        self.action_otsu_thresholding.setObjectName("action_otsu_thresholding")
        self.action_niblack_thresholding = QtGui.QAction(MainWindow)
        self.action_niblack_thresholding.setObjectName("action_niblack_thresholding")
        self.action_linear_filter = QtGui.QAction(MainWindow)
        self.action_linear_filter.setObjectName("action_linear_filter")
        self.action_median_filter = QtGui.QAction(MainWindow)
        self.action_median_filter.setObjectName("action_median_filter")
        self.action_kuwahara_filter = QtGui.QAction(MainWindow)
        self.action_kuwahara_filter.setObjectName("action_kuwahara_filter")
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_quit)
        self.menuColors.addAction(self.action_select_pen_color)
        self.menuColors.addSeparator()
        self.menuColors.addAction(self.action_filter_red)
        self.menuColors.addAction(self.action_filter_green)
        self.menuColors.addAction(self.action_filter_blue)
        self.menuColors.addAction(self.action_grayscale)
        self.menuColors.addSeparator()
        self.menuColors.addAction(self.action_histogram)
        self.menuZoom.addAction(self.action_zoom_in)
        self.menuZoom.addAction(self.action_zoom_out)
        self.menuProcessing.addAction(self.action_exp)
        self.menuProcessing.addAction(self.action_log)
        self.menuProcessing.addAction(self.action_hist_stretch)
        self.menuProcessing.addAction(self.action_hist_eq)
        self.menuProcessing.addSeparator()
        self.menuProcessing.addAction(self.action_custom_thresholding)
        self.menuProcessing.addAction(self.action_otsu_thresholding)
        self.menuProcessing.addAction(self.action_niblack_thresholding)
        self.menuProcessing.addSeparator()
        self.menuProcessing.addAction(self.action_linear_filter)
        self.menuProcessing.addAction(self.action_median_filter)
        self.menuProcessing.addAction(self.action_kuwahara_filter)
        self.menuEdit.addAction(self.action_revert)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuColors.menuAction())
        self.menubar.addAction(self.menuZoom.menuAction())
        self.menubar.addAction(self.menuProcessing.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Image editor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Original image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Processed image", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Position:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Original color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Processed color:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Selected color:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_selected_color.setText(QtGui.QApplication.translate("MainWindow", "R:255 G:255 B:255", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Zoom:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_zoom.setText(QtGui.QApplication.translate("MainWindow", "x1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuColors.setTitle(QtGui.QApplication.translate("MainWindow", "Colors", None, QtGui.QApplication.UnicodeUTF8))
        self.menuZoom.setTitle(QtGui.QApplication.translate("MainWindow", "Zoom", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProcessing.setTitle(QtGui.QApplication.translate("MainWindow", "Processing", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.action_save.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_quit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.action_select_pen_color.setText(QtGui.QApplication.translate("MainWindow", "Select pen color", None, QtGui.QApplication.UnicodeUTF8))
        self.action_filter_red.setText(QtGui.QApplication.translate("MainWindow", "Filter red", None, QtGui.QApplication.UnicodeUTF8))
        self.action_filter_green.setText(QtGui.QApplication.translate("MainWindow", "Filter green", None, QtGui.QApplication.UnicodeUTF8))
        self.action_filter_blue.setText(QtGui.QApplication.translate("MainWindow", "Filter blue", None, QtGui.QApplication.UnicodeUTF8))
        self.action_zoom_in.setText(QtGui.QApplication.translate("MainWindow", "Zoom in", None, QtGui.QApplication.UnicodeUTF8))
        self.action_zoom_in.setShortcut(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.action_zoom_out.setText(QtGui.QApplication.translate("MainWindow", "Zoom out", None, QtGui.QApplication.UnicodeUTF8))
        self.action_zoom_out.setShortcut(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.action_exp.setText(QtGui.QApplication.translate("MainWindow", "Exponential function", None, QtGui.QApplication.UnicodeUTF8))
        self.action_revert.setText(QtGui.QApplication.translate("MainWindow", "Revert changes", None, QtGui.QApplication.UnicodeUTF8))
        self.action_histogram.setText(QtGui.QApplication.translate("MainWindow", "Show histogram", None, QtGui.QApplication.UnicodeUTF8))
        self.action_log.setText(QtGui.QApplication.translate("MainWindow", "Logarithmic function", None, QtGui.QApplication.UnicodeUTF8))
        self.action_hist_stretch.setText(QtGui.QApplication.translate("MainWindow", "Histogram stretching", None, QtGui.QApplication.UnicodeUTF8))
        self.action_hist_eq.setText(QtGui.QApplication.translate("MainWindow", "Histogram equalization", None, QtGui.QApplication.UnicodeUTF8))
        self.action_grayscale.setText(QtGui.QApplication.translate("MainWindow", "Grayscale", None, QtGui.QApplication.UnicodeUTF8))
        self.action_custom_thresholding.setText(QtGui.QApplication.translate("MainWindow", "Custom thresholding", None, QtGui.QApplication.UnicodeUTF8))
        self.action_otsu_thresholding.setText(QtGui.QApplication.translate("MainWindow", "Otsu thresholding", None, QtGui.QApplication.UnicodeUTF8))
        self.action_niblack_thresholding.setText(QtGui.QApplication.translate("MainWindow", "Niblack thresholding", None, QtGui.QApplication.UnicodeUTF8))
        self.action_linear_filter.setText(QtGui.QApplication.translate("MainWindow", "Linear Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.action_median_filter.setText(QtGui.QApplication.translate("MainWindow", "Median Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.action_kuwahara_filter.setText(QtGui.QApplication.translate("MainWindow", "Kuwahara Filter", None, QtGui.QApplication.UnicodeUTF8))

from imageView import ImageView
