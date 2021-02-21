import time
from dataclasses import dataclass

import cv2
import numpy
import pyautogui
from mss import mss


@dataclass
class GameWindow:
    x: int = 0
    y: int = 0


gameWindow = GameWindow()


def loop():
    with mss() as sct:
        mon = {"top": 40, "left": 0, "width": 1024, "height": 768}
    title = "[MSS] FPS benchmark"
    fps = 0
    last_time = time.time()
    while True:
        img = numpy.asarray(sct.grab(mon))
