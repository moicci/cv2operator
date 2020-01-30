import cv2
import numpy as np

from .mouse_operator import MouseOperator


# ポリゴン/ポリライン入力
class _PolyOperator(MouseOperator):

    # @param color line color
    # @param thickness thickness of line
    def __init__(self, window, color=(0, 0xff, 0), thickness=1):
        super().__init__(window)
        self.color = color
        self.thickness = thickness
        self._points = []

    def finish(self):
        points = self._points
        self._points = []
        return points

    def mouse_event(self, event, x, y):
        if event == cv2.EVENT_LBUTTONDOWN:
            self._points.append((x, y))

        elif event == cv2.EVENT_MOUSEMOVE:
            self._update_shape((x, y))

    def _update_shape(self, hover_point):
        with self.window.draw() as image:

            if len(self._points) > 0:
                points = self._make_points(self._points, hover_point)
                p1 = points[0]
                for p2 in points[1:]:
                    cv2.line(image, p1, p2, self.color, self.thickness)
                    p1 = p2
        
            if hover_point:
                cv2.circle(image, hover_point, 2, self.color, -1)

# ポリライン入力
class PolylineOperator(_PolyOperator):

    def _make_points(self, points, hover_point):
        if hover_point:
            return points + [hover_point]
        else:
            return points


# ポリゴン入力
class PolygonOperator(_PolyOperator):

    def _make_points(self, points, hover_point):
        if hover_point:
            return points + [hover_point, self._points[0]]
        else:
            return points + [self._points[0]]

