import time
import picamera
import os

def take_photo():
    with picamera.PiCamera() as camera:
        time.sleep(2)

        # Format the timestamp correctly
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = "/home/picuteness/Pictures"  # Change this to your desired folder
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist

        filename = os.path.join(folder_path, f"photo_{timestamp}.jpg")
        camera.capture(filename)
        print(f"Photo saved as {filename}")

take_photo()