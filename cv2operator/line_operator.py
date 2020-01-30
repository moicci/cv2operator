import cv2
import numpy as np

from .mouse_operator import DragOperator

#
# Input a line
#
class LineOperator(DragOperator):

    # @param callback fn((x0,y0), (x1,y1))
    # @param color line color
    # @param thickness thickness of line
    def __init__(self, window, callback=None, color=(0, 0xff, 0), thickness=1):
        super().__init__(window, self._drag_event)
        self.color = color
        self.thickness = thickness
        self._callback = callback

    def _drag_event(self, event, p1, p2):
        line = self._update_line(p1, p2)
        if event == cv2.EVENT_LBUTTONUP:
            if line and self._callback:
                self._callback(*line)

    def _update_line(self, p1, p2):
        w = abs(p2[0] - p1[0])
        h = abs(p2[1] - p1[1])

        if w < 1 or h < 1:
            return None

        with self.window.draw() as image:
            cv2.line(image, p1, p2, self.color, self.thickness)

        return p1, p2
