class StockTrade:

    def __init__(self, scrip, date, price, quantity, trade_type):

        self.scrip = scrip
        self.date = date
        self.price = price
        self.quantity = quantity
        self.trade_type = trade_type


trade = list()

trade.append(StockTrade('INFY', '2024-09-01', 1614.76, 25, 'Buy'))
trade.append(StockTrade('RELIANCE', '2024-09-02', 117.11, 10, 'Buy'))
trade.append(StockTrade('FACT', '2024-09-03', 6333.45, 10, 'Buy'))
trade.append(StockTrade('NIIT', '2024-09-04', 10.12, 500, 'Buy'))
trade.append(StockTrade('INFY', '2024-10-04', 1699.99, 25, 'Sell'))
trade.append(StockTrade('NIIT', '2024-10-05', 13.66, 250, 'Sell'))

# for item in trade:
#    print("{} {} ₹{}".format(item.trade_type.upper(), item.scrip, round(item.price * item.quantity)))


print(trade[0].__dict__)





class School:
    gender = "female"
    def __init__(self, student):
        self.student = student
    
    def display(self):
        print("ping!")
        return

s1 = School("Anu Sharma")
s2 = School("Manu Bhaker")
s3 = School("Manu Chandra")




map(lambda x: ((x**3)%2==0,x**3),[4,5,6])

[64, 216]