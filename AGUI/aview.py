from PyQt5 import QtCore, QtGui, QtWidgets
from AGUI import ASkin,ARole

class AView(QtWidgets.QGraphicsView):
    # Rubber band signal
    rectChanged = QtCore.pyqtSignal(QtCore.QRect)
    # Mouse Signals
    mouse_press_event = QtCore.pyqtSignal(QtWidgets.QGraphicsView, QtGui.QMouseEvent)
    mouse_move_event = QtCore.pyqtSignal(QtGui.QMouseEvent)
    mouse_release_event = QtCore.pyqtSignal(QtGui.QMouseEvent)
    # Keyboard Signals
    key_press_event = QtCore.pyqtSignal(QtGui.QKeyEvent)
    key_release_event = QtCore.pyqtSignal(QtGui.QKeyEvent)

    def __init__(self, graph_id):
        QtWidgets.QGraphicsView.__init__(self)
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

