from tkinter import *
from textblob import TextBlob
 
def clearAll() :
     word1_field.delete(0, END)
     word2_field.delete(0, END)
 
def correction() :
 
    input_sentence = word1_field.get()
    blob_obj = TextBlob(input_sentence)
    corrected_word = str(blob_obj.correct())
    word2_field.insert(10, corrected_word)
 
if _name_ == "_main_" :
 
    root = Tk()
    root.title("Grammar Correction")
 
    root.configure(background = 'light green')
    root.geometry("400x150")
    root.title("Grammar Corrector")
     
    headlabel = Label(root, text = 'Welcome to Grammar Corrector Application', fg = 'black', bg = "red")
     
    label1 = Label(root, text = "Input Sentence", fg = 'black', bg = 'dark green')
         
    label2 = Label(root, text = "Corrected Sentence", fg = 'black', bg = 'dark green')
     
     
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0)
    label2.grid(row = 3, column = 0, padx = 10)

    word1_field = Entry()
    word2_field = Entry()
         
    word1_field.grid(row = 1, column = 1, padx = 10, pady = 10)
    word2_field.grid(row = 3, column = 1, padx = 10, pady = 10)
 

    button1 = Button(root, text = "Correction", bg = "red", fg = "black",command = correction)
         
    button1.grid(row = 2, column = 1)

    button2 = Button(root, text = "Clear", bg = "red",fg = "black", command = clearAll)
     
    button2.grid(row = 4, column = 1)

    root.mainloop()