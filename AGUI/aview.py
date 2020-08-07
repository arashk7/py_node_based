from PyQt5 import QtCore, QtGui, QtWidgets
from AGUI import ASkin, ARole, APortType, AScene, AConfig


class AView(QtWidgets.QGraphicsView):
    """AView is a Custom Graphic View for our node based"""

    rectChanged = QtCore.pyqtSignal(QtCore.QRect)
    """ Rubber band signal"""

    mouse_press_event = QtCore.pyqtSignal(QtWidgets.QGraphicsView, QtGui.QMouseEvent)
    """Mouse Signals"""
    mouse_move_event = QtCore.pyqtSignal(QtGui.QMouseEvent)
    """Mouse Signals"""
    mouse_release_event = QtCore.pyqtSignal(QtGui.QMouseEvent)
    """Mouse Signals"""

    key_press_event = QtCore.pyqtSignal(QtGui.QKeyEvent)
    """Keyboard Signals"""
    key_release_event = QtCore.pyqtSignal(QtGui.QKeyEvent)
    """Keyboard Signals"""

    def __init__(self, graph_id):
        QtWidgets.QGraphicsView.__init__(self)

        ASkin.init_default()
        """Default skin has to be loaded here
        But since this program is under development, we consider to just initialize the skin and save it as default"""

        # Setting up all the parameters regards QGraphicsView
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setBackgroundBrush(QtGui.QBrush(ASkin.color(ARole.BACKGROUND)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setDragMode(False)
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)

        # Active AntiAliasing
        self.setRenderHint(QtGui.QPainter.Antialiasing, True)

        # Add Custom Scene to our view
        self.__scene = AScene(self)
        self.__scene.setSceneRect(QtCore.QRectF(0, 0, 5000, 3500))
        self.setScene(self.__scene)



        self.draw_grid()
        a = APortType.INPUT

    # This function is called every time the window size changed
    def resizeEvent(self, event: QtGui.QResizeEvent):
        self.updateSceneRect(QtCore.QRectF(0, 0, self.__scene.width(), self.__scene.height()))
        super(AView, self).resizeEvent(event)
    def draw_grid(self):
        """The draw function in this app is different from Qt
        This draw means draw fixed object on scene (Not a rendering)."""

        pen = QtGui.QPen(ASkin.color(ARole.GRID))
        width = self.scene().sceneRect().width()
        height = self.scene().sceneRect().height()
        # Draw horizontal lines
        for i in range(0, int(width + 0), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.scene().addLine(i, 0, i, height + 00, pen)
            line.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
            line.setZValue(-1)
            line.setData(0, 'grid')
            line.setActive(False)
            line.setEnabled(False)

        # Draw vertical lines
        for i in range(0, int(height + 00), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.scene().addLine(0, i, width + 0, i, pen)
            line.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
            line.setZValue(-1)
            line.setData(0, 'grid')
            line.setActive(False)
