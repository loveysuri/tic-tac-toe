from tkinter import *
from tkinter.messagebox import *
tkWindow = Tk()
tkWindow.geometry('350x300')
turn=0
flag=0
def changeText1():
    global turn
    if button1['text']==' ':
        if turn==0:
            turn=1
            button1['text'] = 'X'
        elif turn==1:
            turn=0
            button1['text'] = 'O'
    checkwin()
def changeText2():
    global turn
    if button2['text']==' ':
        if turn == 0:
            turn = 1
            button2['text'] = 'X'
        elif turn == 1:
            turn = 0
            button2['text'] = 'O'
    checkwin()
def changeText3():
    global turn
    if button3['text']==' ':
        if turn == 0:
            turn = 1
            button3['text'] = 'X'
        elif turn == 1:
            turn = 0
            button3['text'] = 'O'
    checkwin()
def changeText4():
    global turn
    if button4['text']==' ':
        if turn == 0:
            turn = 1
            button4['text'] = 'X'
        elif turn == 1:
            turn = 0
            button4['text'] = 'O'
    checkwin()
def changeText5():
    global turn
    if button5['text']==' ':
        if turn == 0:
            turn = 1
            button5['text'] = 'X'
        elif turn == 1:
            turn = 0
            button5['text'] = 'O'
    checkwin()
def changeText6():
    global turn
    if button6['text'] == ' ':
        if turn == 0:
            turn = 1
            button6['text'] = 'X'
        elif turn == 1:
            turn = 0
            button6['text'] = 'O'
    checkwin()
def changeText7():
    global turn
    if button7['text'] == ' ':
        if turn == 0:
            turn = 1
            button7['text'] = 'X'
        elif turn == 1:
            turn = 0
            button7['text'] = 'O'
    checkwin()
def changeText8():
    global turn
    if button8['text'] == ' ':
        if turn == 0:
            turn = 1
            button8['text'] = 'X'

        elif turn == 1:
            turn = 0
            button8['text'] = 'O'
    checkwin()
def changeText9():
    global turn
    if button9['text'] == ' ':
        if turn == 0:
            turn = 1
            button9['text'] = 'X'
        elif turn == 1:
            turn = 0
            button9['text'] = 'O'
    checkwin()
def checkwin():
    global flag
    flag=flag+1
    b1 = button1['text']
    b2 = button2['text']
    b3= button3['text']
    b4= button4['text']
    b5 = button5['text']
    b6 = button6['text']
    b7 = button7['text']
    b8 = button8['text']
    b9 = button9['text']
    if b1==b2==b3=="X" or b4==b5==b6=="X" or b7==b8==b9=="X" or b1==b4==b7=="X" or b2==b5==b8=="X" or b3==b6==b9=="X" or b1==b5==b9=="X" or b3==b5==b7=="X" :
        showinfo("huraaayy!!!!","player X wins")
    elif b1==b2==b3=="O" or b4==b5==b6=="O" or b7==b8==b9=="O" or b1==b4==b7=="O" or b2==b5==b8=="O" or b3==b6==b9=="O" or b1==b5==b9=="O" or b3==b5==b7=="O" :
        showinfo("huraaayy!!!!","player O wins")
    elif flag==9:
        showinfo("well played both","its a tie!!!")
def reset():
    global turn
    turn=0
    button1["text"]=" "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "
def exit():
    tkWindow.destroy()

button1 = Button(tkWindow,text=' ',command=changeText1,height=5,width=10,bg="brown",fg="yellow")
button2 = Button(tkWindow,text=' ',command=changeText2,height=5,width=10,bg="brown",fg="yellow")
button3 = Button(tkWindow,text=' ',command=changeText3,height=5,width=10,bg="brown",fg="yellow")
button4 = Button(tkWindow,text=' ',command=changeText4,height=5,width=10,bg="brown",fg="yellow")
button5 = Button(tkWindow,text=' ',command=changeText5,height=5,width=10,bg="brown",fg="yellow")
button6 = Button(tkWindow,text=' ',command=changeText6,height=5,width=10,bg="brown",fg="yellow")
button7 = Button(tkWindow,text=' ',command=changeText7,height=5,width=10,bg="brown",fg="yellow")
button8 = Button(tkWindow,text=' ',command=changeText8,height=5,width=10,bg="brown",fg="yellow")
button9 = Button(tkWindow,text=' ',command=changeText9,height=5,width=10,bg="brown",fg="yellow")
button1.grid(column=1,row=0)
button2.grid(column=2,row=0)
button3.grid(column=3,row=0)
button4.grid(column=1,row=1)
button5.grid(column=2,row=1)
button6.grid(column=3,row=1)
button7.grid(column=1,row=2)
button8.grid(column=2,row=2)
button9.grid(column=3,row=2)
button10= Button(tkWindow,text='PLAY AGAIN',command=reset,bg="grey",fg="black")
button10.grid(column=4,row=0)
button11= Button(tkWindow,text='EXIT',command=exit,bg="grey",fg="black")
button11.grid(column=4,row=2)
l1=Label(tkWindow,text="TIC TAC TOE ")
l1.grid(column=4,row=1)
l2=Label(tkWindow,text="1st turn:X ")
l2.grid(column=1,row=6)
tkWindow.mainloop()