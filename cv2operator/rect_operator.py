import cv2
import numpy as np

from .mouse_operator import DragOperator

#
# Input a rectangle
#
class RectOperator(DragOperator):

    # @param callback fn(left, top, width, height)
    # @param color line color
    # @param thickness thickness of line
    def __init__(self, window, callback=None, color=(0, 0xff, 0), thickness=1):
        super().__init__(window, self._drag_event)
        self.color = color
        self.thickness = thickness
        self._callback = callback

    def _drag_event(self, event, p1, p2):
        bbox = self._update_rect(p1, p2)
        if event == cv2.EVENT_LBUTTONUP:
            if bbox and self._callback:
                self._callback(*bbox)

    def _update_rect(self, p1, p2):
        x = min(p1[0], p2[0])
        y = min(p1[1], p2[1])
        w = max(p1[0], p2[0]) - x
        h = max(p1[1], p2[1]) - y

        if w < 1 or h < 1:
            return None

        bbox = (x, y, w, h)

        with self.window.draw() as image:
            p1 = (x, y)
            p2 = (x + w, y + h)
            cv2.rectangle(image, p1, p2, self.color, self.thickness)

        return bbox

