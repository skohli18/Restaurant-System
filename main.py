from tkinter import *
import random 
import time

root = Tk()
root.geometry("1200x700")
root.title("Restaurant Management System")
frame = Frame(root)
frame.grid(row = 0, column = 0)
frame2 = Frame(root)
frame2.grid(row = 10, column = 0)
frame3 = Frame(root)
frame3.grid(row = 35, column = 0)
frame4 = Frame(root)
frame4.grid(row = 30, column = 150)
frame5 = Frame(root)
frame5.grid(row = 50, column = 150)
frame6 = Frame(root)
frame6.grid(row = 70, column = 150)
frame7 = Frame(root)
frame7.grid(row = 71, column = 150)
frame8 = Frame(root)
frame8.grid(row = 72, column = 150)
frame9 = Frame(root)
frame9.grid(row = 0, column = 0)

title = Label(frame, text = "Restaurant Management System", font = "Times 30 bold")
title.grid(row = 0, column = 100)

localTime = localtime=time.asctime(time.localtime(time.time())) #study this line
date = Label(frame, text = localTime, font = "Times 24")
date.grid(row = 10, column = 100)

orderNumber = Label(frame2, text = "Order Number: ", font = "Times 14")
orderNumber.grid(row = 10, column = 0)

orderVar = StringVar()

orderEntry = Entry(frame2, textvariable = orderVar)
orderEntry.grid(row = 10, column = 10)

fries = Label(frame2, text = "Number of fries: ", font = "Times 14")
fries.grid(row = 20, column = 0)

friesVar = StringVar()
friesVar.set("0")

friesEntry = Entry(frame2, textvariable = friesVar)
friesEntry.grid(row = 20, column = 10)

lunchCombo = Label(frame2, text = "Number of lunch combos: ", font = "Times 14")
lunchCombo.grid(row = 30, column = 0)

lunchComboVar = StringVar()
lunchComboVar.set("0")

lunchComboEntry = Entry(frame2, textvariable = lunchComboVar)
lunchComboEntry.grid(row = 30, column = 10)

burger = Label(frame2, text = "Number of burgers: ", font = "Times 14")
burger.grid(row = 40, column = 0)

burgerVar = StringVar()
burgerVar.set("0")

burgerEntry = Entry(frame2, textvariable = burgerVar)
burgerEntry.grid(row = 40, column = 10)

pizza = Label(frame2, text = "Number of pizzas: ", font = "Times 14")
pizza.grid(row = 50, column = 0)

pizzaVar = StringVar()
pizzaVar.set("0")

pizzaEntry = Entry(frame2, textvariable = pizzaVar)
pizzaEntry.grid(row = 50, column = 10)

cheeseBurger = Label(frame2, text = "Number of cheeseburgers: ", font = "Times 14")
cheeseBurger.grid(row = 60, column = 0)

cheeseBurgerVal = StringVar()
cheeseBurgerVal.set("0")

cheeseBurgerEntry = Entry(frame2, textvariable = cheeseBurgerVal)
cheeseBurgerEntry.grid(row = 60, column =10)

drinks = Label(frame2, text = "Number of drinks: ", font = "Times 14")
drinks.grid(row = 10, column = 50)

drinksVar = StringVar()
drinksVar.set("0")

drinksEntry = Entry(frame2, textvariable=drinksVar)
drinksEntry.grid(row = 10, column = 60)

cost = Label(frame2, text = "Cost: ", font = "Times 14")
cost.grid(row = 20, column = 50)

costVar= StringVar()

costEntry = Entry(frame2, textvariable=costVar)
costEntry.grid(row = 20, column = 60)

serviceCharge = Label(frame2, text = "Service charge: ", font = "Times 14")
serviceCharge.grid(row = 30, column = 50)

serviceChargeVar = StringVar()

serviceChargeEntry = Entry(frame2, textvariable=serviceChargeVar)
serviceChargeEntry.grid(row = 30, column = 60)

tax = Label(frame2, text = "Tax: ", font = "Times 14")
tax.grid(row = 40, column = 50)

taxVar = StringVar()

taxEntry= Entry(frame2, textvariable=taxVar)
taxEntry.grid(row = 40, column = 60)

subTotal = Label(frame2, text = "Subtotal: ", font = "Times 14")
subTotal.grid(row = 50, column = 50)

subTotalVar = StringVar()

subTotalEntry= Entry(frame2, textvariable=taxVar)
subTotalEntry.grid(row = 50, column = 60)

total = Label(frame2, text = "Total: ", font = "Times 14")
total.grid(row = 60, column = 50)

totalVar= StringVar()

totalEntry = Entry(frame2, textvariable=totalVar)
totalEntry.grid(row =60, column = 60)

def ref():
    x = random.randint(0,100)
    randomRef = str(x)
    orderVar.set(randomRef)
    
    costOfFries = float(friesVar.get())
    costOfLunchCombo = float(lunchComboVar.get())
    costOfBurger = float(burgerVar.get())
    costOfPizza = float(pizzaVar.get())
    costOfCheeseBurger = float(cheeseBurgerVal.get())
    costOfDrinks = float(drinksVar.get())
    
    costOfFries = costOfFries * 2.5
    costOfLunchCombo = costOfLunchCombo * 6.5
    costOfBurger = costOfBurger * 4.5
    costOfPizza = costOfPizza * 7.5
    costOfCheeseBurger = costOfCheeseBurger * 5
    costOfDrinks = costOfDrinks * 2
    
    costOfMeals = "$ ",str('%.2f'%(costOfFries + costOfLunchCombo + costOfBurger + costOfPizza + costOfCheeseBurger + costOfDrinks)) 
    totalCostOfFood = (costOfFries + costOfLunchCombo + costOfBurger + costOfPizza + costOfCheeseBurger + costOfDrinks)
    costOfTax = ((totalCostOfFood)/8)
    serviceCharge = ((totalCostOfFood)/15)
    subtotalTotal = (((totalCostOfFood)/8) + ((totalCostOfFood)/15))
    tax = "$ ", str('%.2f'%costOfTax)
    service = "$ ", str('%.2f'%serviceCharge)
    overAllCost = (totalCostOfFood + subtotalTotal)
    overAllCost = "$ ", str('%.2f'%overAllCost)
    subtotalTotal = "$ ", str('%.2f'%(subtotalTotal))
    
    costVar.set(costOfMeals)
    serviceChargeVar.set(service)
    taxVar.set(tax)
    subTotalVar.set(subtotalTotal)
    totalVar.set(overAllCost)
    

def restaurantPrices():
    top = Toplevel(frame9)
    top.geometry("300x200")
    top.title("Prices for Restaurant Menu")
    label = Label(top, text = "Prices of All Items at this Restaurant", font = "Times 14 bold")
    label.grid(row = 0, column = 0)
    friesPrice = Label(top, text = "Fries - 2.50", font = "Times 14 ")
    friesPrice.grid(row = 10, column = 0)
    lunchPrice = Label(top, text = "Lunch Meal - 6.50", font = "Times 14")
    lunchPrice.grid(row = 20, column = 0)
    burgerPrice = Label(top, text = "Burger - 4.50", font = "Times 14")
    burgerPrice.grid(row = 30, column = 0)
    pizzaPrice = Label(top, text = "Pizza - 7.50", font = "Times 14")
    pizzaPrice.grid(row = 40, column = 0)
    cheeseBurgerPrice = Label(top, text = "Cheeseburger - 5.00", font = "Times 14")
    cheeseBurgerPrice.grid(row = 50, column = 0)
    drinksPrice = Label(top, text = "Drinks - 2.00", font = "Times 14")
    drinksPrice.grid(row = 60, column = 0)
    
    
def reset():
    orderVar.set("")
    friesVar.set("")
    lunchComboVar.set("")
    burgerVar.set("")
    pizzaVar.set("")
    cheeseBurgerVal.set("")
    drinksVar.set("")
    costVar.set("")
    serviceChargeVar.set("")
    taxVar.set("")
    subTotalVar.set("")
    totalVar.set("")
    
def quit():
    root.destroy()

priceButton = Button(frame3, text = "PRICE", font = "Times 16", command = restaurantPrices)
priceButton.grid(row = 1, column = 0)

priceTotal = Button(frame3, text = "TOTAL", font = "Times 16", command = ref)
priceTotal.grid(row = 1, column = 30)

resetButton = Button(frame3, text = "RESET", font = "Times 16", command = reset)
resetButton.grid(row = 1, column = 60)

exitButton = Button(frame3, text = "EXIT", font = "Times 16", command = quit)
exitButton.grid(row = 1, column = 90)


def click(event): #when you making a function there is an automatic parameter called event if you are binding it, the event we are referring to is <"Button-1">
    global scValue 
    text = event.widget.cget("text") #event.widget provides the button you just clicked, c.get() takes the text from a widget
    if text == "=":
        if scValue.get().isdigit():
            value= int(scValue.get())
        else:
            value = eval(screen.get()) #eval evaluates the expression
            
        scValue.set(value)
        screen.update()
    elif text == "CE":
        scValue.set("") #sets screen to blank
        screen.update() #update screen for it to be blank
    else:
        scValue.set(scValue.get()+text) #this takes "" and the number of the button you pressed and updates the screen if you click 3 and 2 it concatenates so the screen is updated to 32
        screen.update() #you don't need to specify scValue, because in the screen there is a text variable of scValue already set
            

scValue = StringVar()
scValue.set("") #allows you to set the value of a variable # 
screen = Entry(root, textvariable=scValue, font = "Lucida 40 bold", bg = "white", fg = "black")
screen.grid(row = 10, column = 150) 
#your buttons can have the same name
button = Button(frame4, text = "9",font = "lucida 35 bold") #the padding adds the white space inside of the button
button.grid(row = 30, column = 200) 
button.bind("<Button-1>", click) #when using bind we pass in the event, action, binding is able to relate the event of a widget to a function# 
button = Button(frame4, text = "8", font = "lucida 35 bold")
button.grid(row = 30, column = 220)
button.bind("<Button-1>", click)
button = Button(frame4, text = "7", font = "lucida 35 bold")
button.grid(row = 30, column = 240)
button.bind("<Button-1>", click)
button = Button(frame4, text = "+", font = "lucida 35 bold")
button.grid(row = 30, column = 260)
button.bind("<Button-1>", click)
button = Button(frame5, text = "6", font = "lucida 35 bold")
button.grid(row = 50, column = 200)
button.bind("<Button-1>", click)
button = Button(frame5, text = "5", font = "lucida 35 bold")
button.grid(row = 50,column = 220)
button.bind("<Button-1>", click)
button = Button(frame5, text = "4", font = "lucida 35 bold")
button.grid(row = 50, column = 240)
button.bind("<Button-1>", click)
button = Button(frame5, text = "-", font = "lucida 35 bold")
button.grid(row = 50, column = 260)
button.bind("<Button-1>", click)
button = Button(frame6, text = "3", font = "lucida 35 bold")
button.grid(row = 70, column = 200)
button.bind("<Button-1>", click) 
button = Button(frame6, text = "2", font = "lucida 35 bold")
button.grid(row = 70, column = 220)
button.bind("<Button-1>", click)
button = Button(frame6, text = "1", font = "lucida 35 bold")
button.grid(row = 70, column = 240)
button.bind("<Button-1>", click)
button = Button(frame6, text = "*", font = "lucida 35 bold")
button.grid(row = 70, column = 260)
button.bind("<Button-1>", click)
button = Button(frame7, text = "CE", font = "lucida 35 bold")
button.grid(row = 90, column = 200)
button.bind("<Button-1>", click) 
button = Button(frame7, text = "0", font = "lucida 35 bold")
button.grid(row = 90, column = 220)
button.bind("<Button-1>", click) 
button = Button(frame7, text = "/", font = "lucida 35 bold")
button.grid(row = 90, column = 240)
button.bind("<Button-1>", click) 
button = Button(frame7, text = "=", font = "lucida 35 bold")
button.grid(row = 90, column = 260)
button.bind("<Button-1>", click)
button = Button(frame8, text = "%", font = "lucida 35 bold")
button.grid(row = 110, column = 220)
button.bind("<Button-1>", click)
button = Button(frame8, text = ".", font = "lucida 35 bold")
button.grid(row = 110, column = 240)
button.bind("<Button-1>", click) 
root.mainloop()
