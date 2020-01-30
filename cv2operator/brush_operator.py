import cv2
import numpy as np

from .mouse_operator import MouseOperator

#
# ドラッグで塗りつぶしてマスクを作る
#
class BrushOperator(MouseOperator):

    # @param brush_color    (b,g,r) brush color to paint on window
    # @param brush_size     int     brush size [px]
    # @param mask_fg_color  uint8   foreground color for mask
    # @param mask_bg_color  uint8   background color for mask
    # @param callback       fn(mask_image)
    def __init__(self, window, brush_color=(0, 0xff, 0), brush_size=2, 
                                    mask_fg_color=0xff, mask_bg_color=0, callback=None):
        super().__init__(window)
        self.brush_color = brush_color
        self.brush_size = brush_size
        self.mask_fg_color = mask_fg_color
        self.mask_bg_color = mask_bg_color
        self._dragging = False
        self._mask_image = None
        self._drawing_image = None
        self._callback = callback
        self.reset_mask()

    @property
    def mask_image(self):
        return self._mask_image

    # create mask image
    def reset_mask(self):
        self._drawing_image = None
        size = self.window.window_size()
        if size:
            shape = (size[1], size[0])
            self._mask_image = np.full(shape, self.mask_bg_color, dtype=np.uint8)

    def mouse_event(self, event, x, y):
        if self._mask_image is None:
            self.reset_mask()

        if event == cv2.EVENT_LBUTTONDOWN:
            self._paint(x, y)
            self._dragging = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if self._dragging:
                self._paint(x, y)

        elif event == cv2.EVENT_LBUTTONUP:
            self._dragging = False
            if self._callback:
                self._callback(self._mask_image)

    def _paint(self, x, y):
        if self._drawing_image is None:
            self._drawing_image = self.window.image_to_draw()

        image = self._drawing_image

        if self.brush_size == 1:
            image[y,x] = self.color
            self._mask_fg_image[y,x] = self.mask_fg_color
        else:
            cv2.circle(image, (x,y), self.brush_size, self.brush_color, -1)
            cv2.circle(self._mask_image, (x,y), self.brush_size, self.mask_fg_color, -1)

        self.window.update(image)
