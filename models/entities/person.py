# Simulação de um banco de dados simples para armazenar informações de pessoas

class Person:
    def __init__(self, name: str, age: int, sex: str, cpf: str, address: str, phone: str):
        self.name = name
        self.age = age
        self.sex = sex
        self.cpf = cpf
        self.address = address
        self.phone = phone