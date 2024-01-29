class IR:
    incomeBrackets = [0, 30001, 50001, 60001, 80001, 180001]
    taxRates = [0, 0.10, 0.20, 0.30, 0.34, 0.38]

    @staticmethod
    def getIR(salary):
        for i in range(len(IR.incomeBrackets)):
            if salary < IR.incomeBrackets[i]:
                return IR.taxRates[i-1]
        return IR.taxRates[len(IR.taxRates)-1]

