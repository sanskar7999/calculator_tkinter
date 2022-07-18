from tkinter import *


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if svalue.get().isdigit():
            value = int(svalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(screen.get()) 
                value = "Error"

        svalue.set(value)
        screen.update()
# -------to clear screen ------
    elif text == "C":
        svalue.set("")
        screen.update()
    else:
        svalue.set(svalue.get() + text)
        screen.update()

root = Tk()
root.title("calculatar made by Sanskar")
root.geometry("300x300")

#  This is screen commands --------
svalue = StringVar()
svalue.set(" ")
screen  =Entry(root ,textvar = svalue, fg="gray" ,font=(""  ,35 , 'bold') , justify=RIGHT)
screen.place(x=0 , y=0 ,relwidth=1)

#---------- this is a frame of buttons-------

key = Frame(root , bg="red"  )
key.place(x=0, y=70 , width=300 , height=300)
#---------This is a Button command ----------
input = ["7", "8", "9" , "/" ,"C"]
input1 = ["4","5" ,"6" , "*" , "%"]
input2 = ["1" ,"2" ,"3" ,"-" ,"."] 
input3 = ['', '0' , '' , '+' , '=']
for (i ,j ) in zip(range(len(input)) , range(0,241 ,60)): 
        b = Button(key , text=input[i] , font=(" " , 20 , "bold"), border=8 )
        b.place(x=j , y=0 , height=60 ,width=60 )
        b.bind("<Button-1>" , click)    

for (i ,j) in zip(range(len(input1)) , range(0,241 ,60)): 
        b = Button(key , text=input1[i], font=(" " , 20 , "bold"), border=8 )
        
        b.place(x=j , y=60 , height=60 ,width=60 )
        b.bind("<Button-1>" , click)

for (i ,j) in zip(range(len(input2)) , range(0,241 ,60)): 
        b = Button(key , text=input2[i], font=(" " , 20 , "bold"), border=8 )
        b.place(x=j , y=120 , height=60 ,width=60 )
        b.bind("<Button-1>" , click)

for (i ,j) in zip(range(len(input3)) , range(0,241,60)):
    b = Button(key ,  border=8 , font=(" " , 20 , "bold"), text=input3[i] )
    b.place(x=j , y=180 , height=60 ,width=60)
    b.bind("<Button-1>" , click)
    
root.mainloop()