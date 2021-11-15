from fpdf import FPDF
import os

def compilePDF(relpath, pdfname):
    # folder filled with images to be converted
    imagelist = []

    # loop over all pictures and save path to imagelist
    for path in os.listdir(relpath):
        full_path = os.path.join(relpath, path)
        if os.path.isfile(full_path):
            imagelist.append(full_path)

    # append images one by one to combined pdf
    pdf = FPDF()
    for image in imagelist:
        pdf.add_page()
        pdf.image(image)

    # save output pdf 
    pdf.output(relpath+os.sep+pdfname+".pdf", "F")
