from tkinter import *
calci=Tk()#crating the calci widget
calci.title('Simple Calculator')#changing the title of calciwidget

#creating the entry widget
e=Entry(calci,width=50,borderwidth=10,fg='black')
e.grid(row=0,column=0,columnspan=4,pady=15)#columnspan tells how many columns comes under the entry widget

def button_clear():#clear button deletes the total text in entry widget 
  e.delete(0,END)#delets from 0th index to end in entry widget
    
def button_click(number):
        #when any number from 0 t0 9 is pressed it is stored in current variable
        current=e.get()
        e.delete(0,END)#after storing clearing it
        e.insert(0,current + str(number))#concating with another digit
        #eg: 1st entry--> 1 ; in 2nd entry --> 2 the 1st entry is cleared and concatinated with 2 displays 12
    
def button_add():
    #creatong global variables to compare he operator and number
    first_num=e.get()#before click on + button the number on enrty widget will be stored in first_num
    global f_num#for displaying results we need global
    global operator#for perform operation we need global
    operator="add"#assign ad when  + symbol is pressed
    f_num=float(first_num)#converting string  into int 
    e.delete(0,END)#clearing the entry widget

#sub mul and div function perform similar operation as add func
def button_sub():
    first_num=e.get()
    global f_num
    global operator
    operator="sub"
    f_num=int(first_num)
    e.delete(0,END)

def button_mul():
    global operator
    first_num=e.get()
    operator="mul"
    global f_num
    f_num=float(first_num)
    e.delete(0,END)

def button_div():
    global operator
    first_num=e.get()
    operator="div"
    global f_num
    f_num=float(first_num)
    e.delete(0,END)


def button_equal():
    second_number=e.get()#before hitting the equal the number on screen will be stored in second_number
    e.delete(0,END)#clears the entry widget
    if operator == 'add':#comparing operators
        e.insert(0,f_num+float(second_number))#inserting result in the entry widget
    elif operator=="sub":
        e.insert(0,f_num - float(second_number))
    elif operator=="mul":
        e.insert(0,f_num * float(second_number))
    elif operator=="div":
        e.insert(0,f_num / float(second_number))

#creating the buttons from 0 to 9 and adjusting their size 
#and also defining the button function in keyword argument command and changing background and fore ground colours 
button_0=Button(calci,text="0",padx=20,pady=30,command=lambda:button_click(0),bg='grey',fg='white')
button_1=Button(calci,text="1",padx=20,pady=30,command=lambda:button_click(1),bg='grey',fg='white')
button_2=Button(calci,text="2",padx=20,pady=30,command=lambda:button_click(2),bg='grey',fg='white')

button_3=Button(calci,text="3",padx=20,pady=30,command=lambda:button_click(3),bg='grey',fg='white')
button_4=Button(calci,text="4",padx=20,pady=30,command=lambda:button_click(4),bg='grey',fg='white')
button_5=Button(calci,text="5",padx=20,pady=30,command=lambda:button_click(5),bg='grey',fg='white')

button_6=Button(calci,text="6",padx=20,pady=30,command=lambda:button_click(6),bg='grey',fg='white')
button_7=Button(calci,text="7",padx=20,pady=30,command=lambda:button_click(7),bg='grey',fg='white')
button_8=Button(calci,text="8",padx=20,pady=30,command=lambda:button_click(8),bg='grey',fg='white')

button_9=Button(calci,text="9",padx=20,pady=30,command=lambda:button_click(9),bg='grey',fg='white')

#displaying the button on the calci widget for each row 3 ,digit button displayed
button_9.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_7.grid(row=1,column=2)
button_6.grid(row=2,column=2)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=0)
button_3.grid(row=3,column=2)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=0)
button_0.grid(row=4,column=1)

#creating the  +,-,*,/ ,= and clear buttons and defining their roles
Plus_button=Button(calci,text="+",padx=20,pady=35,command=button_add,bg='grey',fg='white')
Minus_button=Button(calci,text="-",padx=20,pady=35,command=button_sub,bg='grey',fg='white')
Mul_button=Button(calci,text="*",padx=20,pady=35,command=button_mul,bg='grey',fg='white')
Div_button=Button(calci,text="/",padx=20,pady=35,command=button_div,bg='grey',fg='white')
Equal_button=Button(calci,text="=",padx=20,pady=35,command=button_equal,bg='grey',fg='white')
Clear_button=Button(calci,text="Cls",padx=20,pady=35,command=button_clear,bg='orange',fg='white')

#displaying the operator buttons
Plus_button.grid(row=1,column=5)
Minus_button.grid(row=2,column=5)
Mul_button.grid(row=3,column=5)
Equal_button.grid(row=4,column=2)
Div_button.grid(row=4,column=5)
Clear_button.grid(row=4,column=0)

calci.mainloop()
