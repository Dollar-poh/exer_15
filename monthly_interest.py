from class_account import Saver
print("_"*25)
print("Savings Account details")
print("_"*25)

jo_saver = Saver(200, "Jo Kicks", "GU232387T", "address")
bo_saver = Saver(100000, "Bo Jo", "JN93876200B", "address")
jo_saver.deposit(300)
bo_saver.deposit(100000)

# print(Saver.numCreated)
# print(jo_saver.__class__.__name__) can be used to check correct class has been created

# nb this needs formatting
print(jo_saver._account_number)
print("Jo's savings balance before interest is: £", jo_saver.getbalance(),)# uses getbalance() from Account class
print("Jo's updated balance is £", jo_saver.add_monthly_interest()) # uses add_monthly_interest() from Saver class
print("_"*25)
print(bo_saver._account_number)
print("Bo's savings balance before interest is: £", bo_saver.getbalance())
print("Bo's updated balance is £", bo_saver.add_monthly_interest())



