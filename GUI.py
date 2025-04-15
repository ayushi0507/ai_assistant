from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
root = Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg='#6F8FAF')

#ask function
def ask():
    user_val = speech_to_text.speech_to_text()
    bot_val = action.action(user_val)
    text.insert(END, "User: " + user_val + "\n")
    if bot_val != None:
        text.insert(END, "Assistant: " + bot_val + "\n")
    if bot_val == "Goodbye! Have a great day!":
        root.destroy()

#send function
def send():
    send = entry.get()
    bot = action.action(send)
    text.insert(END, "User: " + send + "\n")
    if bot != None:
        text.insert(END, "Assistant: " + send + "\n")
    if bot == "Goodbye! Have a great day!":
        root.destroy()
    entry.delete(0, END)

#delete function
def del_text():
    text.delete(1.0, END)
    
    
#frame

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#356696")
frame.grid(row=0, column=1, padx=55, pady=10)

#text label

text_label = Label(frame, text="AI Assistant", font=("Arial", 14 , "bold"), bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)

#image

image = ImageTk.PhotoImage(Image.open("img/assistant.jpg"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0, pady=20)


#text

text = Text(root, font =("courier", 10 , "bold"), bg="#356696")
text.grid(row=2, column=0)
text.place(x=100, y=375, height=100, width=375)

#entrywidgit

entry = Entry(root , justify=CENTER)
entry.place(x=100, y=500, height=30, width=350)

#button1

Button1 = Button(root, text="Ask", font=("Arial", 10), bg="#356696", fg="white" , padx=40 , pady=16 , borderwidth=1 , relief=SOLID , command=ask)
Button1.place(x=70, y=550)

#button2

Button2 = Button(root, text="Send", font=("Arial", 10), bg="#356696", fg="white" , padx=40 , pady=16 , borderwidth=1, relief=SOLID , command=send)
Button2.place(x=400, y=550)

#button3

Button3 = Button(root, text="Delete", font=("Arial", 10), bg="#356696", fg="white" , padx=40 , pady=16 , borderwidth=1 , relief=SOLID , command=del_text)
Button3.place(x=225, y=550)



root.mainloop()
