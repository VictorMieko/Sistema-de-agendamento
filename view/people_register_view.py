import os
from typing import Dict

# pagina inicial
class RegisterPeopleView:
    def registry_people_view(self) -> Dict:
        os.system('cls || clear')

        print("=== Formulario de consulta ===")
        name = input("Nome: ")
        age = input("Idade: ")
        sex = input("Sexo (Ex: 'm' ou 'f'): ")
        cpf = input("CPF (Ex: 123.456.789-00): ")
        address = input("Endereço: ")
        phone = input("Numero de telefone: ")

        new_person_information = {
            "name": name, "age": age, "sex": sex, "cpf": cpf,
            "address": address, "phone": phone 
        }

        return new_person_information
    
    # pagina de sucesso no cadastro
    def registry_person_success(self, message: Dict) -> None:
        os.system('cls || clear')

        success_message = f'''
        === Pessoa Cadastrada com Sucesso! ===

            Tipo: { message["type"] }
            Informações: 
                Nome: { message["attributes"]["name"] }
                Idade: { message["attributes"]["age"] }
                Sexo: { message["attributes"]["sex"] }
                CPF: { message["attributes"]["cpf"] }
                Endereço: { message["attributes"]["address"] }
                Telefone: { message["attributes"]["phone"] }
        '''
        print(success_message)

    # pagina de erro no cadastro
    def registry_person_error(self, error: str) -> None:
        os.system('cls || clear')

        error_message_formatted = f'''
        === Erro no Cadastro de Pessoa! ===

            Motivo: { error }
        '''
        print(error_message_formatted)