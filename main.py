import pyautogui
import time
while True:
    target_image = "./data/click_image.png"
    screenshot = pyautogui.screenshot()
    image_location = pyautogui.locate(target_image, screenshot)
    if image_location is not None:
        target_image: str = "./data/think_image.png"
        image_location = pyautogui.locate(target_image, screenshot)
        if image_location is not None:
            pass
        else:
            target_image = "./data/skip_image.png"
            image_location = pyautogui.locate(target_image, screenshot)
            image_center = pyautogui.center(image_location)
            pyautogui.moveTo(image_center)
            pyautogui.click()
        time.sleep(1)