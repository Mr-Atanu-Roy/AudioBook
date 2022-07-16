import pyttsx3
import PyPDF2


speaker=pyttsx3.init()
#setting the speaking speed of speaker
speaker.setProperty("rate", 130)

book=open('Physics.pdf', 'rb')
reader=PyPDF2.PdfFileReader(book)
pages=reader.numPages
print("The pdf contains",pages,"pages")

speaker.say("Please Enter the page number")
speaker.runAndWait()

pageNum=int(input("Please Enter the page number : "))
page=reader.getPage(pageNum-1)
text=page.extractText()
speaker.say(text)
speaker.runAndWait()


a=input("Press Enter To Exit")

