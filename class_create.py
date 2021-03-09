class Person(object):
    '''Class Person created'''
    # numCreated = 0
    def __init__(self, name, age, occupation, city):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.city = city


    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_occupation(self):
        return self.occupation

    def get_city(self):
        return self.city


'''
INHERITANCE
1. You "copy" all the properties, methods, everything from one class to another
2. Names that start with __ are not accessible on the subclass (the child class)
3. You have to call the __init__ for the parent class from the __init__ of the child class
4. Names that start with a _ are private but still accessible from the child
'''

class Customer(Person):
    '''
        Attributes
        ----------
        name, age, occupation, city, company
    '''
    def __init__(self, name, age, occupation, city, company):
        # The next line is equivalent to: super(Customer, self).__init__(name, age, occupation, city)
        Person.__init__(self, name, age, occupation, city)
        self.company = company





'''
POLYMORPHISM
1. Replacing methods from the parent class
'''

class Employee(Person):
    def __init__(self, name, age, occupation, city, company):
        Person.__init__(self, name, age, occupation, city)
        self.company = company


cassie = Employee("cassie", 24, "store keeper", "Sutton", "Asda")






        # print("Person record: " + self.name + self.age + self.occupation + self.city)
#
# class Customer(object):
#     '''Class Customer created'''
#
#     def __init__(self, name, age, occupation, city):
#         self.name = name
#         self.age = age
#         self.occupation = occupation
#         self.city = city

