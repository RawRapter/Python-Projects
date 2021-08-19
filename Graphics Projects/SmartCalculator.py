"""
This Project is smart calculator , we write line explaining what needs to be required and it calculates as per the input.
"""

from tkinter import *

"""Creating all mathematical calculation definations"""
#Addition
def add(a,b):
    return a + b

#Subtraction
def sub(a,b):
    return a - b

#Multiplication
def mul(a,b):
    return a * b

#Division
def div(a,b):
    return a / b

#Modulo
def mod(a,b):
    return a % b

#LCM
def lcm(a,b):
    L = a if a>b else b
    while L <= a*b:
        if L%a == 0 and L%b == 0:
            return L
        L+=1

#HCF
def hcf(a,b):
    H = a if a<b else b
    while H >= 1:
        if a%H == 0 and b%H == 0:
            return H
        H-=1
#All calcuation function end here

"""Extracting important details from text"""
def extract_from_text(text):
    l = [] #creating empty list to store numbers
    #run loop for all the words in the input
    for t in text.split(' '):
        #try block such that only number string is type casted to float
        try:
            l.append(float(t))
        #Not a good way to pass exception but
        #it is useful here when characters can be type casted into float
        except ValueError:
            pass
    return l

"""Function for main calculation functionality in a project"""
def calculate():
    text = textin.get() #getting text from input entry
    #run loop for all the words in the input
    for word in text.split(' '):
        #checking if any word matches with the operation
        if word.upper() in operations.keys():
            try:
                #extracting the numerical values here
                l = extract_from_text(text)
                #applying the mathematical function on the numerical values
                r = operations[word.upper()](l[0] , l[1])
                #getting result in listbox
                list.delete(0,END)
                list.insert(END,r)
            except:
               #if something went wrong
                list.delete(0,END)
                list.insert(END,'Something went wrong please enter again')
            finally:
                break
         #if no word in operation
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'Something went wrong please enter again')

"""Defining dictionary of operations"""
operations = {'ADD':add , 'ADDITION':add , 'SUM':add , 'PLUS':add , '+':add,
                'SUB':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub, 'SUBTRACTION':sub, '-':sub,
                'LCM':lcm , 'HCF':hcf , 'PRODUCT':mul , 'MULTIPLICATION':mul, 'ISTO':mul, '*':mul,
                'MULTIPLY':mul , 'DIVISION':div , 'DIV':div ,'DIVIDE':div, 'MOD':mod ,
                'REMANDER':mod , 'MODULUS':mod}

"""Tkinter Code for frames and functionality starts here"""
win = Tk()
win.geometry('500x300') #giving frame size
win.title("Anant's Smart Calcy") #Tile for project
win.configure(bg='floral white') #providing background color

#Labels for simple information
l1 = Label(win , text='I am a smart calculator',width=20 , padx=3)
l1.place(x=170,y=10)
l2 = Label(win , text='Just Write what calculation you want to perform' , padx=3)
l2.place(x=110,y=40)
l3 = Label(win , text='How can i help you??' , padx=3)
l3.place(x=180,y=100)

#Creating entry for the input
textin = StringVar()
e1 = Entry(win , width=50 , textvariable = textin)
e1.place(x=100,y=160)

#Button to perform calculation
b1 = Button(win , text='Click for Result' ,command=calculate)
b1.place(x=210,y=190)

#Creating box for the result
list = Listbox(win,width=50,height=3)
list.place(x=100,y=230)

win.mainloop() #tkinter code ends here