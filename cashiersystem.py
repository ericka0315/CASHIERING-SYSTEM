class cashieringsystem:

    def __init__(self, a=0, r=0,recieve=0,change=0,temp=0):

        print("WELCOME TO T AMORE MINI CASHIER SYSTEM\n")

        self.a = a
        self.r = r
        self.recieve = recieve
        self.change = change
        self.temp = temp

    def foods(self):

        print("Here is our item list and price list: \n")

        print("----- Foods -----", "\n1. Toast Bread: 10", "\n2. Lumpia: 5", "\n3. Corndog: 30", "\n4. Nachos: 65","\n5. Pastillas: 5", "\n6. Potato with fries: 25","\n7. Pork/Chicken Siomai: 3 for 20","\n8. Cheese Sticks: 3 for 10","\n ----- Drinks -----","\n9. C2 Apple Flavor: 30","\n10. Coca Cola: 21","\n11. Yakult: 12","\n12. Bottled Water: 20","\n13. Boba Milkshake: 30","\n--------------------","\n14. Cash Out","\n15. Exit")    
            
        while (1):

            c = int(input("\nChoose a number: "))

            if (c == 1):

                d = int(input("How much the order quantity: "))
                self.r = self.r + 10 * d

            elif (c == 2):
                d = int(input("How much the order quantity: "))
                self.r = self.r + 5 * d

            elif (c == 3):
                d = int(input("How much the order quantity: "))
                self.r = self.r + 30 * d

            elif (c == 4):
                d = int(input("How much the order quantity: "))
                self.r = self.r + 65 * d
                
            elif ( c == 5):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 5 * d
              
            elif ( c == 6):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 25 * d
                 
            elif ( c == 7):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 20 * d
                                 
            elif ( c == 8):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 10 * d
                 
            elif ( c == 9):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 30 * d
                 
            elif ( c == 10):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 21 * d
             
            elif ( c == 11):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 12 * d
                 
            elif ( c == 12):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 20 * d
                 
            elif ( c == 13):
                 d = int(input("How much the order quantity: "))
                 self.r = self.r + 30 * d

            elif (c == 14):
                print("Your total amount is", self.r)
                if (self.r > 0):
                    recieve = int(input("Input Money Recieve: "))
                    print("Your change is",recieve - self.r)
                    print("Thank You Come Again!")
                    quit()
                    
            elif (c == 15):
                quit()
            else:
                print("Invalid option")

def main():
    a = cashieringsystem()
    while (1):
            a.foods()
main()