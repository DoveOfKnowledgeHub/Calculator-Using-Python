#tkinter is used for GUI
from tkinter import *

# Create the main application window
root = Tk()
root.geometry("1000x500+50+50")     # Set the window size and position
root.resizable(False,False)         # Set the window size and position
root.title("Calculator")            # Set the title of the window


# Function to handle button clicks
def click(event):         
    global EntryValue                       # Access the EntryValue variable globally
    text = event.widget.cget("text")        # Get the text of the button clicked
    
    
    # Check if the 'x' button (remove last character) is clicked
    if text == "=":
        try:
            result = eval(EntryValue.get())   # Evaluate the expression
            EntryValue.set(result)            # Update the entry with the result
        except Exception:
            EntryValue.set("Error")           # Display error if evaluation fails


      # Check if the 'x' button (remove last character) is clicked
    elif text == "x":
        current_text = EntryValue.get()  # Get current text in entry
        EntryValue.set(current_text[:-1])  # Remove the last character
      

    # Check if the 'C' button (clear) is clicked
    elif text == "C":
        EntryValue.set("")
     

    # Append the button text to the entry
    else:
        EntryValue.set(EntryValue.get() + text)
    



# Create a frame for the calculator display
box_width = 250
box_height = 420
box = Frame(root,height=box_height,width=box_width,bg="black")
box.place(relx=0.5,rely=0.5,anchor=CENTER)

EntryValue = StringVar()
EntryValue.set("")
TextE = Entry(root, textvariable=EntryValue,bg='white',fg='black',width=17,bd=0, font=(0.5))
TextE.place(x=400,y=60,height=25)

# Create calculator buttons and bind them to the click function

buttonclr = Button(root,text='C',height=3,width=4)
buttonclr.place(x = 400, y = 105)
buttonclr.bind("<Button-1>",click)      # Bind click event

buttonremove = Button(root,text='x',height=3,width=4)
buttonremove.place(x = 450, y = 105)
buttonremove.bind("<Button-1>",click)

buttonrem = Button(root,text='%',height=3,width=4)
buttonrem.place(x = 500, y = 105)
buttonrem.bind("<Button-1>",click)

buttondiv = Button(root,text='/',height=3,width=4)
buttondiv.place(x = 550, y = 105)
buttondiv.bind("<Button-1>",click)



button7 = Button(root,text='7',height=3,width=4)
button7.place(x = 400, y = 175)
button7.bind("<Button-1>",click)

button8 = Button(root,text='8',height=3,width=4)
button8.place(x = 450, y = 175)
button8.bind("<Button-1>",click)

button9 = Button(root,text='9',height=3,width=4)
button9.place(x = 500, y = 175)
button9.bind("<Button-1>",click)

buttonast = Button(root,text='*',height=3,width=4)
buttonast.place(x = 550, y = 175)
buttonast.bind("<Button-1>",click)




button4 = Button(root,text='4',height=3,width=4)
button4.place(x = 400, y = 245)
button4.bind("<Button-1>",click)

button5 = Button(root,text='5',height=3,width=4)
button5.place(x = 450, y = 245)
button5.bind("<Button-1>",click)

button6 = Button(root,text='6',height=3,width=4)
button6.place(x = 500, y = 245)
button6.bind("<Button-1>",click)

buttonmin = Button(root,text='-',height=3,width=4)
buttonmin.place(x = 550, y = 245)
buttonmin.bind("<Button-1>",click)




button1 = Button(root,text='1',height=3,width=4)
button1.place(x = 400, y = 315)
button1.bind("<Button-1>",click)

button2 = Button(root,text='2',height=3,width=4)
button2.place(x = 450, y = 315)
button2.bind("<Button-1>",click)

button3 = Button(root,text='3',height=3,width=4)
button3.place(x = 500, y = 315)
button3.bind("<Button-1>",click)

buttonadd = Button(root,text='+',height=3,width=4)
buttonadd.place(x = 550, y = 315)
buttonadd.bind("<Button-1>",click)





button0 = Button(root,text='0',height=3,width=11)
button0.place(x = 400, y = 385)
button0.bind("<Button-1>",click)

buttondot = Button(root,text='.',height=3,width=4)
buttondot.place(x = 500, y = 385)
buttondot.bind("<Button-1>",click)

buttonans = Button(root,text='=',height=3,width=4)
buttonans.place(x = 550, y = 385)
buttonans.bind("<Button-1>",click)



# Start the main event loop
root.mainloop()


