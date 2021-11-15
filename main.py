import pynput
from PIL import ImageGrab
import time
from nhentei import nfunctions
import sys
import api
import topdf



if(len(sys.argv) < 2):
    print("Please launch with startup parameter")
    exit()

# Get hentaiID as startup param
hentaiID = sys.argv[1]

hentaiDict = nfunctions.getByID(hentaiID) # API call to dict
hentaiPages = hentaiDict['num_pages'] # Get page count
hentaiMediaID = hentaiDict['media_id'] # To get the images
hentaiImages = list()                 # To store the image links

# populate image array with links
hentaiImages = api.fillImageLinks(hentaiMediaID, hentaiPages)

# Download images
dlpath = "./"+str(hentaiDict['id']) # Relative store path
api.downloadImageLinks(hentaiImages, dlpath) # Download and save

# Compile pdf
topdf.compilePDF(dlpath, hentaiDict['title']['english'])



















































