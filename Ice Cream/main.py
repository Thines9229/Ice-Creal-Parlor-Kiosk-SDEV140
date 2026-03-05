"""
Ice Cream Parlor Kiosk
-----------------------
Purpose


Author: Tirah Hines
Course: SDEV140 Final Project
"""

import tkinter as tk
from tkinter import*

#--------------------------------------------------------------------------------
# Window that opens after the user clicks the button "order" that adds the total
# number of scoops the user sees as neccesary, following the close button that 
# closes the window entirely.
#--------------------------------------------------------------------------------

#Price per scoop
def button_clicked():
    vanillaTotal = int(vanillasb.get()) * 2.25   # Funtion for the calculation of the sum for the program
    chocoTotal = int(chocosb.get()) * 2.25
    strawTotal = int(strawsb.get()) * 2.25
    manTotal = int(mansb.get()) * 2.25
    mbTotal = int(mbsb.get()) * 2.25
    cacTotal = int(cacsb.get()) * 2.25
    total_bills = vanillaTotal + chocoTotal + strawTotal + manTotal + mbTotal + cacTotal

    total_window = tk.Toplevel(root) 
    total_window.title("Order Total") 
    
    tk.Label(total_window, text=f"Your total is: ${total_bills:.2f}", 
             font=("Arial", 18)).pack(pady=20) 
    tk.Button(total_window, text="Close", command=total_window.destroy).pack(pady=10) 
#Total window
    def open_new_window():
        new_window = tk.Toplevel(root)                                 # The second window
        new_window.title("Total")
        new_window.geometry("300x300") 
        tk.Label(new_window, text="Your total is: ").pack(pady=20)
        tk.Button(new_window, text="close", command=new_window.destroy).pack(pady=20)
        # callback button
        tk.Button(total_window, text="More Info", command=open_new_window).pack()
        
#-------------------------------------------
# Main window that connects all the features
#-------------------------------------------

# Main program window
root = Tk()
root.title("Dreamery Creamery")           
root.maxsize(width=1600, height=900)
root.configure(bg="#B197D3")

# Lables for the main window including title
icName = Label(text='Welcome to\nDreamery Creamery', font=("Lucida Calligraphy", 20, "bold"), bg="#B197D3", relief="raised")
icName.place(x=635, y=50)

quote = Label(text="The Flavors You Dream Of", font=("Lucida Calligraphy", 10, "bold"), bg="#B197D3")
quote.place(x=685, y=125)

iclable = Label(text="Pick a flavor and how many scoops you want", font=("Lucida Calligraphy", 12, "bold"), bg="#B197D3")
iclable.place(x=585, y=150)
iclable2 = Label(text="You may choose up to 3 scoops per flavor", font=("Lucida Calligraphy", 12, "bold"), bg="#B197D3")
iclable2.place(x=600, y=180)

tk.Button(root, text="exit", command=root.destroy).pack(pady=20)

#-----------------------------------------------------------------------------------
# The display of the pictures for the main window including the lable, lable place, 
# Info, info place, spinbox, and spinbox placement with customization. It allows you
# to select the dropdown for the spinbox and select the amount of scoops the user
# perfers from the flavor they perfer.
#-----------------------------------------------------------------------------------

vanilla = PhotoImage(file="vanilla-ice-cream.png")       # Photos 
choco = PhotoImage(file="chocolate-ice-cream.png")
straw = PhotoImage(file="strawberry-ice-cream.png")
man = PhotoImage(file="mango-ice-cream.png")
mb = PhotoImage(file="mixed-berry-ice-cream.png")
cac = PhotoImage(file="cookies-and-cream-ice-cream.png")

vanillalable = Label(root, image=vanilla, height=150, width=150)     # Title lable
chocolable = Label(root, image=choco, height=150, width=150)
strawlable = Label(root, image=straw, height=150, width=150)       
manlable = Label(root, image=man, height=150, width=150)
mblable = Label(root, image=mb, height=150, width=150)
caclable = Label(root, image=cac, height=150, width=150)

vanillalable.place(x=300, y=230)      # Title placement
chocolable.place(x=725, y=230)
strawlable.place(x=1150, y=230)
manlable.place(x=300, y=500)
mblable.place(x=725, y=500)
caclable.place(x=1150, y=500)

vanillainfo = Label(text="Vanilla\n$2.25", font=("Lucida Calligraphy", 10, "bold"), bg="#B197D3")    # Information for the ice cream
chocoinfo = Label(text="Chocolate\n$2.25", font=("Lucida Calligraphy", 10, "bold"), bg="#B197D3")    # including the price.
strawinfo = Label(text="Strawberry\n$2.25", font=("Lucida Calligraphy", 10, "bold"), bg="#B197D3")
maninfo = Label(text="Mango\n$2.25", font=("Lucida Calligraphy", 10, "bold"), bg="#B197D3")
mbinfo = Label(text="Mixed Berry\n$2.25", font=("Lucida Calligraphy", 10, "bold"), bg="#B197D3")
cacinfo = Label(text="Cookies and Cream\n$2.25", font=("Lucida Calligraphy", 10, "bold"), bg="#B197D3")

vanillainfo.place(x=340, y=400)   # Info placement
chocoinfo.place(x=760, y=400)
strawinfo.place(x=1179, y=400)
maninfo.place(x=350, y=670)
mbinfo.place(x=750, y=670)
cacinfo.place(x=1150, y=670)

vanillasb = Spinbox(from_=0, to=3, width=5)  # The spinbox tat lets the user select the amount
chocosb = Spinbox(from_=0, to=3, width=5)    # of scoops they would like to a minumum of 3 scoops
strawsb = Spinbox(from_=0, to=3, width=5)    # at a time.
mansb = Spinbox(from_=0, to=3, width=5)
mbsb = Spinbox(from_=0, to=3, width=5)
cacsb = Spinbox(from_=0, to=3, width=5)

vanillasb.place(x=350, y=440)   # Spinbox placement
chocosb.place(x=780, y=440)
strawsb.place(x=1205, y=440)
mansb.place(x=355, y=710)
mbsb.place(x=780, y=710)
cacsb.place(x=1205, y=710)

#-------------------------------------------------------------------------
# After selecting you amount of scoops and flavor, you can then click the 
# finish button to get your total in the "order total" window.
#-------------------------------------------------------------------------
#The button to get the total of your order
finish = Button(text="Order", command=button_clicked)
finish.place(x= 785, y= 775)


root.mainloop() #Starts program