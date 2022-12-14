class Usuario:

    def __init__(self,nombre,email):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = 0


    def hacer_deposito(self, cantidad):
        self.balance_cuenta += cantidad
        return self

    def hacer_retiro(self,amount):
        self.balance_cuenta -= amount
        return self
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance_cuenta}")
        return self

    def transfer_dinero(self,other_user,amount):
        self.balance_cuenta -= amount
        other_user.balance_cuenta += amount
        return self
