import numpy as np 
import mss
import cv2
import time

TOP = 919
LEFT = 997
WIDTH = 69
HEIGHT = 47

monitor = {
    "top": TOP,
    "left": LEFT,
    "width": WIDTH,
    "height": HEIGHT,
}

sct = mss.mss()

print("程式執行中")

while True:
    start_time = time.time()
    sct_img = sct.grab(monitor)

    img_np = np.array(sct_img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)

    cv2.imshow("遊戲截圖（按 q 退出）", frame)

    fps = 1 / (time.time() - start_time)
    print(f"FPS: {fps:.2f}", end="\r")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
print("\n程式結束")
