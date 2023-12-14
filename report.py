
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
import os
import numpy as np
from reportlab.pdfbase import pdfform
import textwrap
import matplotlib.pyplot as plt

def addPlotSection(c,x,y,plot_path,title):
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x, y, title)

    
    # Draw the plot in the PDF
    c.drawImage(plot_path, x, y-165, width=160, height=160)
    
    return c

def addTextSection(c,x,y,title,text, max_characters_per_line=15):
        
    # Text BOx for Raw Data
    textObjectRawData = c.beginText(x, y)
    textObjectRawData.setFont("Helvetica-Bold", 10)
    textObjectRawData.setFillColor(colors.black)
    textObjectRawData.textLine(title)
    textObjectRawData.textLine("")
    textObjectRawData.setFont("Helvetica", 10)
    
    # split text into lines of max 15 characters
    wrapped_text = textwrap.wrap(text, width=max_characters_per_line)
    for line in wrapped_text:
        textObjectRawData.textLine(line)

    c.drawText(textObjectRawData)
    
    return c

# create pdf with 3x3 plot sections and 3x1 text sections to the right
def create_pdf():
    
    # each plot has size 160x160, each title has height 10 -- plot section is height==180 and width = 180 to ensure proper spacing
    column_1 = 20
    column_2 = 200
    column_3 = 380
    column_4 = 560

    row_1 = 540
    row_2 = 360
    row_3 = 180
    
    spacing_left = 20
    
    # create canvas
    c = canvas.Canvas("content_pdf.pdf", pagesize=landscape(A4)) # create new pdf document with landscape A4 format and name content_pdf.pdf
    
    # set color and font for title
    c.setFillColor(colors.grey)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(spacing_left, 560, "Report Projektorqualität")  # set the title of the pdf document
    
    # Generate a dummy matplotlib plot
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title("Sinus")
    
    # Save the plot as an image file at high resolution
    plot_path = os.path.join(os.getcwd(), "plot.png")
    plt.savefig(plot_path, bbox_inches='tight',dpi=1200)
    
    # add all plot sections
    addPlotSection(c,column_1, row_1, "plot.png", "Raw Data")
    addPlotSection(c,column_1, row_2, "plot.png", "Color Cross Talk")
    addPlotSection(c,column_1, row_3, "plot.png", "Matching Quality")
    
    addPlotSection(c,column_2, row_1, "plot.png", "Raw Data2")
    addPlotSection(c,column_2, row_2, "plot.png", "Color Cross Talk2")
    addPlotSection(c,column_2, row_3, "plot.png", "Matching Quality2")
    
    addPlotSection(c,column_3, row_1, "plot.png", "Raw Data3")
    addPlotSection(c,column_3, row_2, "plot.png", "Color Cross Talk3")
    addPlotSection(c,column_3, row_3, "plot.png", "Matching Quality")
    
    # add all text sections
    addTextSection(c,column_4, row_1,"Raw Data","Beispieltext\nBeispieltext\nBeispieltext\nBeispieltext\nBeispieltext\nBeispieltext", max_characters_per_line=60)
    addTextSection(c,column_4, row_2,"Raw Data","Beispieltext\nBeispieltext\nBeispieltext\nBeispieltext\nBeispieltext\nBeispieltext", max_characters_per_line=60)
    addTextSection(c,column_4, row_3,"Raw Data","Beispieltext\nBeispieltext\nBeispieltext\nBeispieltext\nBeispieltext\nBeispieltext", max_characters_per_line=60)
    
    c.save()


if __name__ == "__main__":
    create_pdf()
