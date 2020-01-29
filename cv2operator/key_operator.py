import cv2

#
# キーのイベント
#
class KeyOperator:

    # keyin で入ってきたキーを key&0xff した値がこれ
    KEY_ESC = 27
    KEY_RETURN = 13
    KEY_ARROW_UP = 0
    KEY_ARROW_DOWN = 1
    KEY_ARROW_LEFT = 2
    KEY_ARROW_RIGHT = 3

    def __init__(self, quit_key=KEY_ESC):
        self._callbacks = {}
        self._descriptions = []
        self._enabled = True

        if quit_key and isinstance(quit_key, str):
            quit_key = ord(quit_key)

        self._quit_key = quit_key
        self.add_help(quit_key, "Quit")

    def activate(self):
        self._enabled = True

    def deactivate(self):
        self._enabled = False

    # help messagge
    def help(self):
        return "\n".join(self._descriptions)

    def add_help(self, key, desc):
        def _key_to_name(key):
            if isinstance(key, str):
                return key
            elif key == KeyOperator.KEY_ESC:
                return "ESC"
            elif key == KeyOperator.KEY_RETURN:
                return "Return"
            elif key == KeyOperator.KEY_ARROW_UP:
                return "ArrowUp"
            elif key == KeyOperator.KEY_ARROW_DOWN:
                return "ArrowDown"
            elif key == KeyOperator.KEY_ARROW_LEFT:
                return "ArrowLeft"
            elif key == KeyOperator.KEY_ARROW_RIGHT:
                return "ArrowRight"
            else:
                return None

        if isinstance(key, list) or isinstance(key, tuple):
            names = [_key_to_name(k) for k in key]
            names = [name for name in names if name]
            name = ", ".join(names)
        else:
            name = _key_to_name(key)

        self._descriptions.append(f"{name}: {desc}")

    # @param key char or code
    # @param callback fn()
    # @param desc help message
    def add_callback(self, key, callback, desc=None):
        if desc:
            self.add_help(key, desc)

        if isinstance(key, str):
            key = ord(key)

        self._callbacks[key] = callback

    def main_loop(self):
        while True:
            key = cv2.waitKey()
            if self._enabled:
                callback = self._callbacks.get(key)
                if callback:
                    callback()

            if isinstance(self._quit_key, list):
                if key in self._quit_key:
                    return
            elif key == self._quit_key:
                return
