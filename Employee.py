from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta
from IEmployee import IEmployee

class Employee(IEmployee):
    _counter = 0
    def __init__(self, name, birthDate=datetime(2000, 1, 1), hireDate=datetime.now(), baseSalary=0.0):
        self._name = name
        self._birthDate = birthDate
        self._hireDate = hireDate
        self._baseSalary = baseSalary
        Employee._counter += 1
        self._employeeNumber = Employee._counter

    @property
    def EmployeeNumber(self):
        return self._employeeNumber

    @EmployeeNumber.setter
    def EmployeeNumber(self, value):
        self._employeeNumber = value

    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def BirthDate(self):
        return self._birthDate

    @BirthDate.setter
    def BirthDate(self, value):
        self._birthDate = value

    @property
    def HireDate(self):
        return self._hireDate

    @HireDate.setter
    def HireDate(self, value):
        age_at_hire = (value - self._birthDate).days / 365
        if age_at_hire < 20:
            raise Exception("The age at hiring must be greater than 16 years.")
        self._hireDate = value

    @property
    def EmployeeCount():
        return Employee._counter

    @property
    def BaseSalary(self):
        return self._baseSalary

    @BaseSalary.setter
    def BaseSalary(self, value):
        self._baseSalary = value

    @abstractmethod
    def SalaryToPay(self):
        pass

    def Age(self):
        days_passed = datetime.now() - self._birthDate
        return int(days_passed.days / 365)

    def Seniority(self):
        days_worked = datetime.now() - self._hireDate
        return int(days_worked.days / 365)

    def RetirementDate(self, retirementAge):
        retirement_date = datetime(self._birthDate.year + retirementAge, self._birthDate.month, self._birthDate.day)
        return retirement_date

    def __str__(self):
        return f"{self._employeeNumber}-{self._name}-{self._birthDate.strftime('%d/%m/%Y')}\
-{self._hireDate.strftime('%d/%m/%Y')}-{self._baseSalary}"

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self._employeeNumber == other._employeeNumber
