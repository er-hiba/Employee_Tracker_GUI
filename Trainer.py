from Employee import Employee
from datetime import datetime, timedelta
from IR import IR

class Trainer(Employee):
    _overtimeRate = 70.00
    
    def __init__(self, name="", birthDate=datetime(2000, 1, 1), hireDate=datetime.now(), baseSalary=0.0, overtimeHours=0):
        super().__init__(name, birthDate, hireDate, baseSalary)
        self._overtimeHours = overtimeHours
    
    @property
    def OvertimeRate(self):
        return Trainer._overtimeRate

    @property
    def OvertimeHours(self):
        return self._overtimeHours

    @OvertimeHours.setter
    def OvertimeHours(self, value):
        self._overtimeHours = value

    def SalaryToPay(self):
        return (self._baseSalary + self._overtimeHours * Trainer._overtimeRate) * (1 - IR.getIR(self._baseSalary * 12))

    def __str__(self):
        return f"{super().__str__()}-{self._overtimeHours}"
