import pyttsx3
import PyPDF2 as p2
# Get file handle, you want to read-aloud
file = open('./pdf/lipsum.pdf','rb')
# Read contents of file into book object
book = p2.PdfFileReader(file)
# Load first page (page 0 i.e. page 1) contents into page object
page = book.getPage(0)
# Store contents of page in a text object
text = page.extractText()
# Print the text for debugging purpose.
# Sometimes the pyttsx3 package is not able to read all types of pdf files
# You may comment it by addeding the # before the line below, it's your choice
print (text)
# Initialize the read-aloud python package
speaker = pyttsx3.init()
# Read aloud the pdf page selected
speaker.say(text)
# The line below is used to block program execution until the read-aloud command buffer / queue is cleared or read-out
speaker.runAndWait()
print('Program completed.')