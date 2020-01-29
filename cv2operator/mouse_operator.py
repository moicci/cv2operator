import cv2
import numpy as np
import contextlib

#
# superclass
#
class MouseOperator:

    # @param window (OperatorWindow)
    # @param enabled (bool)
    def __init__(self, window, enabled=True):
        self._window = window
        if enabled:
            window.activate_mouse_operator(self)

    @property
    def window(self):
        return self._window

    # mouse event from window
    # subclass overrides this method
    def mouse_event(self, event, x, y):
        pass

    # activate mouse event
    def activate(self):
        self._window.activate_mouse_operator(self)

    # deactivate mouse event
    def deactivate(self):
        self._window.deactivate_mouse_operator(None)

    # start to draw for operation
    @contextlib.contextmanager
    def draw(self):
        image = self._window.image_to_draw()
        if image is None:
            return

        yield image

        self._window.update(image)

#
# ただのドラッグ操作(図形は描かない)
#
class DragOperator(MouseOperator):

    # @param window (OperatorWindow)
    # @param drag_cb fn(event, p1, p2)
    # @param enabled (bool)
    def __init__(self, window, drag_cb, enabled=True):
        super().__init__(window, enabled)
        self._drag_cb = drag_cb
        self._anchor_point = None

    def mouse_event(self, event, x, y):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._anchor_point = (x, y)

        elif event == cv2.EVENT_MOUSEMOVE:
            if self._anchor_point and self._callback:
                self._drag_cb(event, self._anchor_point, (x, y))

        elif event == cv2.EVENT_LBUTTONUP:
            if self._anchor_point and self._callback:
                self._drag_cb(event, self._anchor_point, (x, y))
            self._anchor_point = None
