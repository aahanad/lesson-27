from tkinter import*
from gtts import gTTS
from translate  import Translator
import os
screen=Tk()
screen.title("text to speech")
Title=Label(screen,text="Text to speech",font=("Brush Script Std",20,"bold"))
Title.place(x=500,y=100)
text=Entry(screen)
text.place(x=500,y=200)
def make():
    translator=Translator(to_lang="ja")
    text_to_translate=text.get()
    translated_text=translator.translate(text_to_translate)
    language="ja"
    myText=gTTS(text=translated_text,lang=language,slow=True)
    myText.save("translated text.mp3")
translate=Button(screen,text="translate to speech",fg="black",bg="white",font=("Brush Script Std",10,"bold"),command=make)
translate.place(x=500,y=300)
screen.mainloop()