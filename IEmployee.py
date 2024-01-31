from abc import ABC, abstractmethod

class IEmployee(ABC):
    @abstractmethod
    def Age(self):
        pass

    @abstractmethod
    def Seniority(self):
        pass

    @abstractmethod
    def RetirementDate(self, retirementAge):
        pass
