#!/usr/bin/env python
import cv2
import numpy as np

from cv2operator import KeyOperator, OperatorWindow
from cv2operator import LineOperator, RectOperator, PolylineOperator, PolygonOperator, BrushOperator

def line_cb(p1, p2):
    print(f"line: p1={p1}, p2={p2}")

def rect_cb(x, y, w, h):
    print(f"rect: x={x}, y={y}, w={w}, h={h}")

active_op = None

original_image = cv2.imread("goru.jpg")
window = OperatorWindow("demo", original_image)

def activate(mouse_op):
    global active_op
    image = original_image.copy()

    text = mouse_op.__class__.__name__
    cv2.putText(image, text, (10,40), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0xff, 0xff))

    # draw image with text
    window.update(image)

    # save image as original
    window.save_image()

    mouse_op.activate()
    active_op = mouse_op

def finish_poly():
    if active_op == polyline_op or active_op == polygon_op:
        points = active_op.finish()
        print(f"polyline/polygon: {points}")

line_op = LineOperator(window, callback=line_cb)
rect_op = RectOperator(window, callback=rect_cb)
polyline_op = PolylineOperator(window)
polygon_op = PolygonOperator(window)
brush_op = BrushOperator(window, brush_size=4)

activate(line_op)

key_op = KeyOperator()
key_op.add_callback("l", lambda : activate(line_op), "input line")
key_op.add_callback("r", lambda : activate(rect_op), "input rectangle")
key_op.add_callback("p", lambda : activate(polyline_op), "input polyline")
key_op.add_callback("g", lambda : activate(polygon_op), "input polygon")
key_op.add_callback("b", lambda : activate(brush_op), "paint by brush")
key_op.add_callback(KeyOperator.KEY_RETURN, finish_poly, "finish to input polyline/polygon")

print(key_op.help())
key_op.main_loop()
