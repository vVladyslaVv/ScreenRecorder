import threading
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pyautogui
import cv2
import numpy as np

# Define the screen resolution
resolution = pyautogui.size()

# Define video codec and output file name
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "my_screen_recording.avi"

# Define frames per second
fps = 30

# Define the length of time to record in seconds
record_time = 10

# Calculate the number of frames to record based on the record time and fps
num_frames = record_time * fps

firefox_driver_path = 'C:/Users/BOROV/Desktop/geckodriver/geckodriver.exe'

# Path to the Firefox binary file
firefox_binary_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'

# Create a new Service object for the Firefox driver
service = Service(executable_path=firefox_driver_path)

# Define Firefox options and set the path to the Firefox binary
firefox_options = webdriver.FirefoxOptions()
firefox_options.binary_location = firefox_binary_path

# Create a new instance of the Firefox driver using the Service object and Firefox options
driver = webdriver.Firefox(service=service, options=firefox_options)

# Maximize the window
driver.maximize_window()


def get_website(website_):
    # Navigate to a website and do some automation
    driver.get(website_)

    # Wait for the page to load
    time.sleep(2)


class ScreenRecordingThread(threading.Thread):
    def run(self):
        # Create a VideoWriter object to write the video to file
        out = cv2.VideoWriter(filename, codec, fps, resolution)

        # Record the specified number of frames
        for i in range(num_frames):
            # Capture a screenshot of the screen
            img = pyautogui.screenshot()

            # Convert the screenshot to a numpy array
            frame = np.array(img)

            # Convert it from BGR (Blue, Green, Red) to RGB (Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Write the frame to the output video file
            out.write(frame)

        # Release the VideoWriter object
        out.release()

        # Destroy all windows
        cv2.destroyAllWindows()


# Start the screen recording thread
screen_recording_thread = ScreenRecordingThread()
screen_recording_thread.start()

# Do other tasks in the main thread

get_website("https://drducuclinics.com/")

# Wait for the screen recording thread to finish
screen_recording_thread.join()

# Continue with other tasks in the main thread
print("Screen recording finished.")
