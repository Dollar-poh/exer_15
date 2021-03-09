from class_account import Annualsaver

print("_"*25)
print("Annual saver details")
print("_"*25)

jo_annualsaver = Annualsaver(1000, "Jo", "GU232387T", "address")
jo_annualsaver = Annualsaver(1000, "Jo", "JN93876200B", address)
jo_annualsaver.withdraw(300)
print(jo_annualsaver.__class__.__name__)
print(jo_annualsaver.getbalance())
print(jo_annualsaver.add_monthly_interest())# overrides add_monthly_interest() from Saver class
print("Jo annual interest is £", jo_annualsaver.add_annual_interest())