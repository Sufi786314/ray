from tkinter import *
# Rule:- Always pack each component/widget to display it on screen.
# Can't Mix grid and pack.
# Window / Screen set-up in tkinter
window = Tk()
window.title("My Gui")
window.minsize(height=500,width=500)

window.config(padx=100,pady=100)

# Components in tkinter : - 

# Labels in tkinter : - 
my_label = Label(text="This is a label",font=("Arial",25,"bold"))
# try bold,italic,underline
my_label.pack(side="left")
# my_label.pack(side="bottom")
# my_label.pack(side="top")
# my_label.pack(side="right")
# my_label.pack(expand=True)
my_label["text"]="New Text"
my_label.config(text="Hello Advance Learners ")


# Button in tkinter
# button = Button(text="Click me")
# button.pack()

# Providing functionality to the button 
def button_clicked():
    my_label.config(text="Button clicked")
    print("Button Got Clicked")

# pass the name of the function to be executed on click .
# Note do not call the function.
    
button = Button(text="Click me",command=button_clicked)
button.pack()

# Challenge change the label to button got clicked on clicked.
# hint make some changes in the function.

# Entry Component in tkinter.
input = Entry(width=30)
# input.get()
# input.insert(END,string="This is a place-holder")
input.pack()

# Challenge Try to get the text into the label on click of the button.
# hint make changes in the function use all the knowledge.

# Text-Box in tkinter
text_box = Text(height=5,width=30)
# To put the cursor ready in the text-box use focus().
text_box.focus()
# print(text_box.get("1.0",END))
text_box.pack()

# Spin-Box 
# def spinbox_used():
#     # To get the current value in the spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0,to=10,width=5,command=spinbox_used)
# spinbox.pack()

# Scale
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0,to=100,command=scale_used)
# scale.pack()

# CheckButton
# def checkButton_used():
#     # Print 1 if Button is checked
#     # Else 0.
#     print(checked_state.get())
# checked_state = IntVar()
# checkButton = Checkbutton(text="Is ON?",variable =checked_state,command=checkButton_used)
# checkButton.pack()
# Always mainloop will be in the end as we need everything to be holded inside the screen .

# Radio-button
# def radio_used():
#     print(radio_state.get())
# radio_state = IntVar()
# radio_button_1 = Radiobutton(text = "Option1",value=1,variable=radio_state,command=radio_used)
# radio_button_1.pack() 

# radio_button_2 = Radiobutton(text = "Option2",value=2,variable=radio_state,command=radio_used)
# radio_button_2.pack() 

# list-Box
# def listbox_used(event):
#     # To Get current Selection From the list Boxs
#     print(listbox.get(listbox.curselection()))

# listbox = Listbox(height=4)
# fruits = ["Apple","Mangoo","Orange","Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item),item)
# listbox.bind("<<ListBoxSelect>>",
# listbox_used)
# listbox.pack()


# Tkinter Layout Manager 
# 1.Pack 
# 2.Place (x,y)
# 3.Grid  [col,row]

# Canvas in tkinter
# canvas = Canvas(width=500,height=500)
# image = PhotoImage(file="google-logo.png")
# canvas.create_image(250,250,image=image)
# canvas.pack()



window.mainloop()

# import turtle 

# # moves the pen in the 
# # forward direction by 
# # 110 pixels 
# turtle.forward(110) 

# # changes the direction of 
# # the pen by 10 degrees in the 
# # left direction 
# turtle.left(110) 

# # moves the pen in the 
# # forward direction in 
# # the new direction by 
# # 110 pixels 
# turtle.forward(110)

