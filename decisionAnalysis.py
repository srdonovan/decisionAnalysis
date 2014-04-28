class Stock:
	def __init__(self,ticker,name):
		self.ticker = ticker
		self.name =name
		
class Transaction:
	def __init__(self,stock,tranDate,tranType,shares,amount,cost):
		#stock - the stock involved in the transaction
		#date - the date of the transaction
		#type - The type of the transaction - buy or sell
		#shares - The number of shares exchanged
		#amount - The amount invested for a buy transaction, the amount received for a sell transaction
		#cost - The cost of the transaction (brokers fees)
		
		self.stock = stock
		self.tranDate = tranDate
		self.tranType = tranType
		self.shares = shares
		self.amount = amount
		self.cost = cost
		
class Decision:
	def __init__(self,stock,dDate,dType,dResult,price,notes):
		#stock - the stock that is the subject of the decision
		#dDate - date of the decision
		#dType - buy or sell
		#dResult - the decision made, Yes or No
		#price - stock quote at time of decision
		#notes - reason for making the decition
		#transaction - the transaction resulting from the decision (if decision was buy or sell)
		
		self.stock = stock
		self.dDate = dDate
		self.dType = dType
		self.dResult = dResult

		if price < 0:
			price = 0
		else:
			self.price = price

		self.notes = notes
