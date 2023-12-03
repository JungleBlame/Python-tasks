
class Employee(object):

    def __init__(self, Name, EmployeeNumber):
        self.__name = Name
        self.__EmployeeNumber= EmployeeNumber


    def get_name(self):
        return self.__name
    
    def get_EmployeeNumber(self):
        return self.__EmployeeNumber
    
    def get_total_pay(self):
        pass

class FullTimeEmployees (Employee):

    def __init__(self, Name, EmployeeNumber,Salary,Years):

        Employee.__init__(self, Name, EmployeeNumber)
        self.__Salary = Salary
        self.__Years = Years

    def get_Years(self):
        return self.__Years
    
    def set_Years(self,Years):
        self.__Years = Years
    
    def get_total_pay(self):
        return self.__Salary * (self.__Years/10 +1)
    
    def get_Salary(self):
        return self.__Salary
    
    def set_salary(self,Salary):
        self.__Salary= Salary


class PartTimeEmployees (Employee):

    def __init__(self, Name, EmployeeNumber,Salary,DaysWorked):

        Employee.__init__(self, Name, EmployeeNumber)

        self.__Salary = Salary
        self.__DaysWorked= DaysWorked

    def get_Salary(self):
        return self.__Salary
    
    def set_salary(self,Salary):
        self.__Salary= Salary

    def set_DaysWorked(self,DaysWorked):
        self.__DaysWorked = DaysWorked

    def get_DaysWorked(self):
        return self.__DaysWorked
    
    def get_total_pay(self):
        return self.__Salary*self.__DaysWorked

PT1= PartTimeEmployees("Steve", 1234, 100, 50)
print(PT1.get_DaysWorked(),PT1.get_total_pay(),PT1.get_EmployeeNumber())



FT1= FullTimeEmployees("Mary", 4321, 42000, 2)
print(FT1.get_Salary(),FT1.get_total_pay(),FT1.get_Years())


