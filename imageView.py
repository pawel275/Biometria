from PySide.QtCore import *
from PySide.QtGui import *


class ImageView(QGraphicsView):
    _scene = None
    _pixmap = None
    _pixmap_item = None
    _painter = None
    _image = None
    mouse_moved = Signal(int, int)
    mouse_dragged = Signal(int, int)
    mouse_pressed = Signal(int, int)

    def __init__(self, parent=None):
        super(ImageView, self).__init__(parent)
        self.setMouseTracking(True)

    def set_image(self, image):
        if self._scene:
            self._scene.removeItem(self._pixmap_item)
            self._painter.end()
        else:
            self._scene = ImageScene(self)
        self._image = image
        self._pixmap = QPixmap(self._image.width(), self._image.height())
        self._pixmap_item = QGraphicsPixmapItem(self._pixmap)
        self._scene.addItem(self._pixmap_item)
        self.setScene(self._scene)
        self._painter = QPainter(self._pixmap)
        self.refresh()

    def refresh(self):
        self._painter.drawImage(0, 0, self._image)
        self._pixmap_item.setPixmap(self._pixmap)


class ImageScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(ImageScene, self).__init__(parent)

    def mouseMoveEvent(self, ev):
        super().mouseMoveEvent(ev)
        x, y = ev.scenePos().x(), ev.scenePos().y()
        if 0 <= x < self.width() and 0 <= y < self.height():
            self.parent().mouse_moved.emit(x, y)
            if ev.buttons().__eq__(Qt.LeftButton):
                self.parent().mouse_dragged.emit(x, y)

    def mousePressEvent(self, ev):
        super().mousePressEvent(ev)
        x, y = ev.scenePos().x(), ev.scenePos().y()
        if 0 <= x < self.width() and 0 <= y < self.height():
            self.parent().mouse_pressed.emit(x, y)
