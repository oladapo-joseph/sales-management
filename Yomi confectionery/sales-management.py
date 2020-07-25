# a sales management application for Yomi confectionery

menu = {'doughnut': [150, 20],
        'cake': [300, 17],
        'cookies': [200, 45],
        'ice-cream': [300, 33],
        'samosa': [250, 11]
       }


class YomiConfectionery:
    def __init__(self, foods):
        self.foods = foods

    # a function that updates new food items to the menu
    def UpdateMenu(self, name, price, quantity):
        self.foods[name] = [price, quantity]
        return self.foods

    # a function to give us the list of items in the menu dictionary
    def AvailableFoods(self):
        print('Foods \t\t Price \t\t Quantity')
        for i in self.foods:
            if len(i)<7:
                print(i,"\t\t",self.foods[i][0], '\t\t', self.foods[i][1] )
            else:
                print(i,"\t",self.foods[i][0], '\t\t', self.foods[i][1] )
        return

    # computing food purchase by the user
    def CustomerPurchases(self):
        self.customerDict = {}
        userStatus = True
        while userStatus:
            print("If you don't have anything else buying kindly enter 'stop'")
            FoodsPurchase = input('What Do you want to buy: ')
            if FoodsPurchase in self.foods.keys():
                Quantity = input(f'How many {FoodsPurchase} do you want to buy: ')
                if int(Quantity) > self.foods[FoodsPurchase][1]:
                    diff = int(Quantity) - self.foods[FoodsPurchase][1]
                    print('We are sorry, we only have ', self.foods[FoodsPurchase][1], ' left, kindly re-order')
                else:
                    # Take in users order
                    self.customerDict[FoodsPurchase] = int(Quantity)
                    self.foods[FoodsPurchase][1] -= int(Quantity)

            elif FoodsPurchase == 'stop':
                userStatus = False
                break


            else:
                print("We don't have " + str(FoodsPurchase) + " in stock")
        return self.customerDict

    # compute the price of food bought
    def ComputePrice(self):
        totalPrice = 0
        for k in self.customerDict.keys():
            totalPrice += self.foods[k][0] * self.customerDict[k]

        # compute 5% VAT and 20% discount
        if 1000> totalPrice >= 500 :
            vatValue = self.deductVAT(totalPrice)
        elif totalPrice >= 1000:
            vatValue = self.discountPurchase(totalPrice)

        else:
            vatValue = totalPrice
        return vatValue

    # display receipt
    def displayReceipt(self):
        print('Food \t \t Quantity \t \t Total Price')
        for k in self.customerDict.keys():
            currentPrice = self.foods[k][0] * self.customerDict[k]
            print(k, '\t \t', str(self.customerDict[k]), '\t \t \t \t', str(currentPrice))

        # Print total price
        VATPrice = self.ComputePrice()
        print("Total Purchases is: ", VATPrice)
        return

    def deductVAT(self, totalPrice):
        # 5% deduction VAT
        return totalPrice - (totalPrice * 0.05)

    def discountPurchase(self, totalPrice):
        # 20% discount
        return totalPrice - (totalPrice * 0.2)

        return


if __name__ == '__main__':
    menu = {'doughnut': [150, 20],
            'cake': [300, 17],
            'cookies': [200, 45],
            'ice cream': [300, 33],
            'samosa': [250, 11]
            }
    yomi = YomiConfectionery(menu)
    yomi.AvailableFoods()
    decision= int(input("To make purchases enter 1\nTo add new Item enter 2\n"))
    while(decision>2):
        decision= int(input("To make purchases enter 1\nTo add new Item enter 2\n"))
        
    if decision == 1:
        customerDict = yomi.CustomerPurchases()
        yomi.displayReceipt()
    if decision == 2:
        item, price , quantity = input("List the details, separate with a space: ").split(' ')
        yomi.UpdateMenu(item, price, quantity)
        yomi.AvailableFoods()



# adding new foods to the database
    # add new foods
    # yomi.addNewFood('rice',50, 300)
