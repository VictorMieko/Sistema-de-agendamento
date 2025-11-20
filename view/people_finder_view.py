import os
from typing import Dict

class PeopleFinderView:
    def find_people_view(self) -> str:
        os.system('cls || clear')

        print("=== Consulta de Pessoas ===\n")
        cpf = input("CPF da pessoa a ser consultada: ")

        people_finder_information = {
            "cpf": cpf
        }

        return people_finder_information
    
    def find_person_success(self, message: Dict) -> None:
        os.system('cls || clear')

        success_message = f"""
            === Pessoa Encontrada ===

            Informações:
                Nome: {message['informações']['Nome']}
                Idade: {message['informações']['Idade']}
                sexo: {message['informações']['Sexo']}
                cpf: {message['informações']['CPF']}
                Endereço: {message['informações']['Endereço']}
                Telefone: {message['informações']['Telefone']}
        """
        print(success_message)

    def find_person_error(self, error: Dict) -> None:
        os.system('cls || clear')

        error_message = f"""
            === Erro na Consulta ===

            Motivo: {error}
        """
        print(error_message)