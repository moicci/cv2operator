import cv2
import contextlib

#
# common window
#
class OperatorWindow:

    # @param name window name
    # @param image np.array
    def __init__(self, name, image=None):
        self._name = name
        self._mouse_operator = None
        self._original_image = None
        self._current_image = None

        if image is not None:
            self.update(image)

    # @return (w, h)
    def window_size(self):
        if self._original_image is None:
            return None
        return self._original_image.shape[1], self._original_image.shape[0]

    # register mouse callbak
    # @param callback fn(event, x, y)
    def activate_mouse_operator(self, operator):
        self._mouse_operator = operator

    # register mouse callbak
    # @param callback fn(event, x, y)
    def deactivate_mouse_operator(self, operator):
        if self._mouse_operator == operator:
            self._mouse_operator = None

    # return active mouse operator
    def active_mouse_operator(self):
        return self._mouse_operator

    # fire mouse event from external
    def fire_mouse_event(self, event, x, y):
        if self._mouse_operator:
            self._mouse_operator.mouse_event(event, x, y)

    # update window image
    def update(self, image):
        cv2.imshow(self._name, image)
        self._current_image = image

        def _callback(event, x, y, int_arg, void_p_arg):
            if x is None and y is None:
                return

            self.fire_mouse_event(event, x, y)

        if self._original_image is None:
            self._original_image = image.copy()
            cv2.setMouseCallback(self._name, _callback)

    # refresh window image passed to self.update
    def clear(self):
        if self._original_image is not None:
            self.update(self._original_image.copy())

    def image_to_draw(self):
        if self._original_image is not None:
            return self._original_image.copy()
        return None

    # start to draw for operation
    @contextlib.contextmanager
    def draw(self):
        image = self.image_to_draw()
        if image is not None:
            yield image
            self.update(image)

    # save current image as original image
    def save_image(self):
        if self._current_image is not None:
            self._original_image = self._current_image

    # reset original image
    def reset_image(self, image):
        self._original_image = image
