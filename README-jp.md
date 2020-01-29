# cv2operator

cv2 (OpenCV) のウィンドウで線、ループなどを入力するためのライブラリです。

![](docs/polygon-op.png)

## 機能

- **LineOperator**: ドラッグで線を入力する
- **PolylineOperator**: 点をクリックして行き折れ線を入力する
- **PolygonOperator**: 点をクリックして行きポリゴンを入力する
- **RectOperator**: ドラッグで矩形を入力する
- **BrushOperator**: ドラッグでマスク領域を塗りつぶす
- **KeyOperator**: ウィンドウでのキー管理

## 使い方

LineOperator の使い方はこんな感じです。

```
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
```

## その他の入力

その他については [examples](https://github.com/moicci/cv2operator/tree/master/examples) の [demo.py](https://github.com/moicci/cv2operator/tree/master/examples/demo.py) を参照してください。

こんな入力が可能です。

### RectOperator

![image](https://raw.githubusercontent.com/moicci/cv2operator/master/docs/rect-op.png)

### LineOperator

![image](https://raw.githubusercontent.com/moicci/cv2operator/master/docs/line-op.png)

### PolylineOperator

![image](https://raw.githubusercontent.com/moicci/cv2operator/master/docs/polyline-op.png)

### PolygonOperator

![image](https://raw.githubusercontent.com/moicci/cv2operator/master/docs/polygon-op.png)

### BrushOperator

![image](https://raw.githubusercontent.com/moicci/cv2operator/master/docs/brush-op.png)
