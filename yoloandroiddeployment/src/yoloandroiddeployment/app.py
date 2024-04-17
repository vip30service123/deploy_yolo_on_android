"""
Deploy Yolo (Object Detection Model) on Android
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import numpy as np
import cv2 as cv
from PIL import Image


class YoloAndroidDeployment(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.view = toga.ImageView()
        main_box.add(self.view)

        capture_button = toga.Button(
            "Capture",
            on_press=self.capture,
        )
        main_box.add(capture_button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def capture(self, widget):
        cap = cv.VideoCapture(0)

        ret, frame = cap.read()

        im = Image.fromarray(frame)
        
        self.view.image = im
    

def main():
    return YoloAndroidDeployment()

