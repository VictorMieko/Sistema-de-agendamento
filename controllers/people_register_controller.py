from typing import Dict
from models.interfaces.person_repository_interface import PersonRepositoryInterface
from models.entities.person import Person

class PeopleRegisterController:
    def __init__(self, repository_interface=PersonRepositoryInterface):
        self.__repository_interface = repository_interface

    def register_person(self, new_person_information: Dict) -> Dict:
        try:
            self.__validate_fields(new_person_information)
            self.__register_person_in_repository(new_person_information)
            response = self.__format_response(new_person_information)
            return {"success": True, "message": response} # retorna um dicionario indicando sucesso
        except Exception as exception:
            return {"success": False, "error": str(exception)} # retorna um dicionario indicando o erro

    # método para validação dos campos
    def __validate_fields(self, new_person_information: Dict) -> None:
        if not isinstance (new_person_information["name"], str):
            raise Exception("Campo 'nome' incorreto.")
        
        try: int(new_person_information["age"])
        except: raise Exception("Campo 'idade' incorreto.")

        if int(new_person_information["age"]) <= 0:
            raise Exception("Campo 'idade' deve ser maior que zero.")
        
        if int(new_person_information["age"]) >= 100:
            raise Exception("Campo 'idade' deve ser menor que zero.")
        
        if not isinstance (new_person_information["sex"], str):
            raise Exception("Campo 'sexo' incorreto.")
        
        if new_person_information["sex"] not in ["m", "f", "M", "F", "Masculino", "Feminino"]:
            raise Exception("Campo 'sexo' deve ser 'm', 'f', 'M', 'F', 'Masculino' ou 'Feminino'.")

        if len(str(new_person_information["cpf"])) != 14:
            raise Exception("Campo 'cpf' deve conter 14 dígitos (incluindo pontos e traços). ")
        
        cpf = new_person_information["cpf"]
        if "." not in cpf or "-" not in cpf:
            raise Exception("CPF inválido. Por favor, inclua '.' e '-' (Ex: 123.456.789-00)")
                
        try: int(new_person_information["phone"])
        except: raise Exception("Campo 'telefone' incorreto.")

        if len(str(new_person_information["phone"])) < 9:
            raise Exception("Campo 'telefone' deve conter no mínimo 10 dígitos.")

    # método para registrar a pessoa no repositório 
    def __register_person_in_repository(self, new_person_information: Dict) -> None:
        name = new_person_information["name"]
        age = int(new_person_information["age"])
        sex = new_person_information["sex"]
        cpf = new_person_information["cpf"]
        address = new_person_information["address"]
        phone = new_person_information["phone"]

        new_person = Person(name, age, sex, cpf, address, phone)
        self.__repository_interface.registry_person(new_person)

    # função para formatar a resposta e mandar para a view
    def __format_response(self, new_person_information: Dict) -> Dict:
        return {
            "type": "Person",
            "attributes": new_person_information
        }