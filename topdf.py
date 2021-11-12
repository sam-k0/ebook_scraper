from fpdf import FPDF
import os

# folder filled with images to be converted
d = "./out"

imagelist = []

# loop over all pictures and save path to imagelist
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        imagelist.append(full_path)

# append images one by one to combined pdf
pdf = FPDF()
for image in imagelist:
    pdf.add_page()
    pdf.image(image)

# save output pdf 
pdf.output("combined.pdf", "F")
