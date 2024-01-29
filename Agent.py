from Employee import Employee
from datetime import datetime, timedelta
from IR import IR

class Agent(Employee):
    def __init__(self, name, birthDate=datetime(2000, 1, 1), hireDate=datetime.now(), baseSalary=0.0, responsibilityBonus=0.0):
        super().__init__(name, birthDate, hireDate, baseSalary)
        self._responsibilityBonus = responsibilityBonus

    @property
    def ResponsibilityBonus(self):
        return self._responsibilityBonus

    @ResponsibilityBonus.setter
    def ResponsibilityBonus(self, value):
        self._responsibilityBonus = value

    def SalaryToPay(self):
        base_salary = float(self._baseSalary)  # Convert baseSalary to float if it's not already
        responsibility_bonus = float(self._responsibilityBonus)  # Convert responsibilityBonus to float if it's not already

        return (base_salary + responsibility_bonus) * (1 - IR.getIR(base_salary * 12))
