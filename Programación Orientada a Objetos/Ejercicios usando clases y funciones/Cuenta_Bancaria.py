class CuentaBancaria:
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance

    def depositar(self, monto):
        self.balance += monto
        print(f"Depósito exitoso. Balance actual: {self.balance}")

    def retirar(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            print(f"Retiro exitoso. Balance actual: {self.balance}")
        else:
            print("Fondos insuficientes")


# crear objeto
cuenta = CuentaBancaria("José", 100000)
cuenta.depositar(10000)
cuenta.retirar(5000)
