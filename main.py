import pyttsx3
import PyPDF2 as p2
file = open('./pdf/lipsum.pdf','rb')
book = p2.PdfFileReader(file)
page = book.getPage(0)
text = page.extractText()
print (text)
speaker = pyttsx3.init()
speaker.say(text)
speaker.runAndWait()
print('Program completed.')

