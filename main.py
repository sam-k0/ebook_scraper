import pynput
from PIL import ImageGrab
import time

pages = 1

# instantiate mouse controller for scrolling action
mouse = pynput.mouse.Controller()

print("Waiting 2 seconds before starting. Get ready.")
time.sleep(2)
print("starting...")

# repeat for all pages
for i in range(pages):
    # take a screenshot of the actual page on the screen (edit bounds)
    screenshot = ImageGrab.grab(bbox=(460, 84, 892, 697))
    # save picture to folder
    screenshot.save(f"./out/page_{i}.png")
    print(f"saving picture {i}")
    # scroll to next page (in this case just scrolling on single line down)
    mouse.scroll(0, -1)
    # wait for scrolling animation to finish
    time.sleep(0.2)

print(f"done. Took {pages} pictures! :D")



















































