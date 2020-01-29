import cv2
from cv2operator import KeyOperator, OperartorWindow, LineOperator

def line_cb(p1, p2):
    print(f"line: p1={p1}, p2={p2}")

image = cv2.imread("goru.jpg")
window = OperartorWindow("example", image)

line_op = LineOperator(window, callback=line_cb)

key_op = KeyOperator()
print(key_op.help())
key_op.main_loop()
