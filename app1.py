
from tkinter import *
def btnClick(number):
    global operator
    operator += number
    text_input.set(operator)
 
def btnClear():
    global operator
    operator = ""
    text_input.set("")

def btnCalculate():
    global operator
    result = eval(operator)
    text_input.set(result)
    operator = ''


cal = Tk()

operator = ''

cal.title("Simple Calculator")
text_input = StringVar()
text_display = Entry(cal,font=('arial',20,'bold'),insertwidth=4,bg='powder blue',justify="right",textvariable=text_input,bd=30).grid(columnspan=4)

btn7 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='7',command=lambda:btnClick('7')).grid(row=1,column=0)
btn8 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='8',command=lambda:btnClick('8')).grid(row=1,column=1)
btn9 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='9',command=lambda:btnClick('9')).grid(row=1,column=2)
btnPlus = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='+',command=lambda:btnClick('+')).grid(row=1,column=3)

btn4 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='4',command=lambda:btnClick('4')).grid(row=2,column=0)
btn5 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='5',command=lambda:btnClick('5')).grid(row=2,column=1)
btn6 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='6',command=lambda:btnClick('6')).grid(row=2,column=2)
btnMulti = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='*',command=lambda:btnClick('*')).grid(row=2,column=3)


btn3 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='3',command=lambda:btnClick('3')).grid(row=3,column=0)
btn2 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='2',command=lambda:btnClick('2')).grid(row=3,column=1)
btn1 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='1',command=lambda:btnClick('1')).grid(row=3,column=2)
btnDiv = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='/',command=lambda:btnClick('/')).grid(row=3,column=3)

btnC = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='C',command=btnClear).grid(row=4,column=0)
btn0 = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='0',command=lambda:btnClick('0')).grid(row=4,column=1)
btnEqual = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='=',command=btnCalculate).grid(row=4,column=2)
btnMinus = Button(cal,padx=16,pady=16,bd=8,fg='black',font=('arial',20,'bold'),text='-',command=lambda:btnClick('-')).grid(row=4,column=3)

cal.mainloop()