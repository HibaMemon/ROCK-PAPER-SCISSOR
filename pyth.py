
from tkinter import *
from random import randint
from tkinter import ttk

root=Tk()
#SETTING THE TITLE
root.title('ROCK......PAPER.....SCISSOR...')
#SETTING THE CANVAS SIZE
root.geometry("500x600")
#SETTING THE BACKGROUND COLOUR
root.config(bg="pink")

# DEFINE IMAGES
rock =PhotoImage(file='rockk.png')
paper=PhotoImage(file='paper.png')
scissor=PhotoImage(file='sc.png')

#ADD  IMAGES TO A LIST
image_list = [rock,paper,scissor]

#PICK A RANDOM NUMBER BETWEEN 0 AND 2
pick_number=randint(0,2)

#THROW UP AN IMAGE WHEN PROGRAM STARTS
image_label = Label(root,image=image_list[pick_number])
image_label.pack(pady=20)



#MAKE OUR CHOICE
user_choice= ttk.Combobox(root,value=("ROCK","PAPER","SCISSORS"))
user_choice.current(0)
user_choice.pack(pady=20)



#CREAT A SPIN FUNCTION
def spin():
    #PICK A RANDOM NUMBER
    pick_number = randint(0,2)
    #SHOW IMAGE
    image_label.config(image=image_list[pick_number])


    #0=ROCCK
    #1=PAPER
    #2=SCISSOR
    #CONVERT DROPDOWN CHOICE TO A NUMBER
    if user_choice.get()=="ROCK":
        user_choice_value=0
    elif user_choice.get()=="PAPER":
        user_choice_value=1
    elif user_choice.get()=="SCISSOR":
        user_choice_value=2


    #DETERMINE WHETHER WE WON OR LOST



    #if user picks rock
    if user_choice_value==0:
        if pick_number==0:
            win_lose_label.config(text="Its A Tie! SPIN AGAIN")
        elif pick_number==1:
            #rock and paper
            win_lose_label.config(text="paper covers rock!...YOU LOSE")
        elif pick_number==2:
            #rock and scissor
            win_lose_label.config(text="Rock smashes Scissor!....YOU WIN")

    #if user picks paper
    if user_choice_value==1:
        if pick_number==0:
            #rock and paper
            win_lose_label.config(text="paper covers rock!...YOU win")
        elif pick_number==1:
            win_lose_label.config(text="Its A Tie! SPIN AGAIN")
        elif pick_number==2:
            #rock and scissor
            win_lose_label.config(text="scissor cuts paper!....YOU lost")


    #if user picks scissor
    if user_choice_value==2:
        if pick_number==0:
            win_lose_label.config(text="rock smashes scissor....YOu lose")
        elif pick_number==1:
            #rock and paper
            win_lose_label.config(text="scissor cuts paper....you win")
        elif pick_number==2:
            #rock and scissor
            win_lose_label.config(text="Its a Tie ....SPIN AGAIN")

#CREATE A SPIN BUTTON
spin_button = Button(root,text="spin me!!",command=spin)
spin_button.pack(pady=10)

#LABEL FOR SHOWING IF YOU WON OR NOT
win_lose_label=Label(root,text="",font=("Helvetica",8))
win_lose_label.pack(pady=50)
root.mainloop()


































