clearfrom class_account import Account

jo_account = Account(1000, "Jo", "GU232387T", "6 The High Street")
bo_account = Account(200, "Bo", "JN93876200B", "28 Hill Rise")

print("_"*25)
print("Current Account details")
print("_"*25)
print("Account number: ", jo_account._account_number)
print("Jo's opening balance: £", jo_account.getbalance(), "\n")
print("Account number: ", bo_account._account_number)
print("Bo's opening balance: £", bo_account.getbalance())
# print(jo_account.__address) returns error jo_account has no attribute '__address' can be accessed with name mangling

jo_account.deposit(10987)
bo_account.withdraw(500)

# call make_charges method
jo_account.makecharges()
bo_account.makecharges()
print("\n")

# check that getbalance updates
print("Jo's current balance: £", jo_account.getbalance())
print("Bo's current balance: £", bo_account.getbalance())
print("_"*25)
print()
