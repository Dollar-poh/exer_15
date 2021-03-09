from class_create import Person, Customer

'''
Person Record
------------
'''
jane_record = Person('Jane Doe', 34, 'Doctor', 'Birmingham')
john = Person("john", 12, "student", "Brussels")
june = Person("june", 18, "diver", "Paris")

'''
Customer Record
---------------
'''
george = Customer('George Smith', 76, 'Trader', 'London', "Sainsbury")
jake = Customer("jake", 12, "student", "otwock", "microsoft")

'''
Employee Record
---------------
'''

# jane = Person('Jane Doe', 34, 'Doctor', 'Birmingham')
# george = Person('George', 27, 'Engineer', 'Glasgow')

print(jane_record.get_name())
print(jane_record.get_age())
print(jane_record.get_occupation())
print(jane_record.get_city())


print(george.get_name)

# print("Person record: " + self.name + self.age + self.occupation + self.city)
