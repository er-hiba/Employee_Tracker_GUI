from abc import ABC, abstractmethod

class IEmployee(ABC):
    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def seniority(self):
        pass

    @abstractmethod
    def retirementDate(self, retirementAge):
        pass
