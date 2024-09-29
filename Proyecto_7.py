class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


persona = Persona('Ivan', 'Moreno')

class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        # Cuando se pida imprimir cliente poner todos sus datos, incluyendo incluyendo el balance de su cuenta
        return f'Cliente: {self.nombre}, {self.apellido}\nBalance de cuenta: {self.numero_cuenta}: ${self.balance}'


    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print('Deposito aceptado')

    def retirar(self,monto_retirar):
        if self.balance >= monto_retirar:
            self.balance -= monto_retirar
            print('Retiro aceptado')
        else:
            print('Fondos insuficientes')


def crear_cliente():
    nombre_cl = input('Ingresa tu nombre: ')
    apellido_cl = input('Ingresa tu apellido: ')
    numero_cuenta = input('Ingresa tu numero de cuenta: ')
    cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0

    while opcion != 'S':
        print('Elije: Depositar (D), Retirar (R), Salir (S)')
        opcion = input()

        if opcion == 'D':
            monto_dep = int(input('Monto a depositar: $'))
            mi_cliente.depositar(monto_dep)
        elif opcion == 'R':
            monto_ret = int(input('Monto a retirar: $'))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)

    print('Gracias por usar el Banco')


inicio()





