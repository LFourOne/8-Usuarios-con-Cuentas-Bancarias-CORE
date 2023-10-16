class usuario:
    def __init__(self, name, email, cuenta):
        self.name = name
        self.email = email
        self.cuenta = cuenta
    def ver_cuenta(self):
        print(f"Usuario: {self.name}, Email: {self.email}, Interes: {self.cuenta.interes}, Balance: {self.cuenta.balance}")
class cuenta:
    def __init__(self, interes, balance):
        self.interes = interes
        self.balance = balance
    def deposito(self, amount):
        self.balance += amount
        return self
    def retiro(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Error Ultra Mega Super Duper Fatal: La cantidad a retirar es mayor a la cantidad actual de dinero en la cuenta")
        return self
    def aplicar_interes(self):
        intereses = (self.interes / 100) * self.balance
        self.balance += intereses
        return self

usuario1 = usuario("Terry", "ChicoTerry@gmail.com", cuenta(5, 10))
usuario1.cuenta.deposito(20).deposito(20).retiro(20).aplicar_interes()
usuario1.ver_cuenta()