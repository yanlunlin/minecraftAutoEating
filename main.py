import numpy as np 
import mss
import cv2
import time
import os 

TOP = 919
LEFT = 997
WIDTH = 69
HEIGHT = 47

SAVE_FOLDER = "picture"

monitor = {
    "top": TOP,
    "left": LEFT,
    "width": WIDTH,
    "height": HEIGHT,
}

sct = mss.mss()

print("程式執行中")

if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

frame_count = 0
while True:
    start_time = time.time()
    sct_img = sct.grab(monitor)

    img_np = np.array(sct_img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)

    cv2.imshow("遊戲截圖（按 q 退出）", frame)

    fps = 1 / (time.time() - start_time)
    frame_count += 1
    if not frame_count % 100:
        filename = os.path.join(SAVE_FOLDER, f"capture_{frame_count}.jpg")
        cv2.imwrite(filename, frame)
        print("儲存圖片")
    print(f"FPS: {fps:.2f}", end="\r")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
print("\n程式結束")
