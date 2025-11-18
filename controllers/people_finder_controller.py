from typing import Dict
from models.interfaces.person_repository_interface import PersonRepositoryInterface
from models.entities.person import Person

class PeopleFinderController:
    def __init__(self, repository_interface=PersonRepositoryInterface):
        self.__repository_interface = repository_interface

    def find_by_name(self, person_finder_information: Dict) -> Dict:
        try:
            self.__validade_fields(person_finder_information)
            person = self.__find_person_in_repository(person_finder_information)
            response = self.__format_finder(person)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
        
    def __validade_fields(self, person_finder_information: Dict) -> None:
        if not isinstance(person_finder_information["name"], str):
            raise Exception("Nome inválido para busca.")
        
    def __find_person_in_repository(self, person_finder_information: Dict) -> Person:
        name = person_finder_information["name"]
        person = self.__repository_interface.find_person_by_name(name)
        if not person: raise Exception("Pessoa não encontrada no repositório.")

        return person

    def __format_finder(self, person: Person) -> Dict:
        return {
            "count": 1,
            "type": "Person",
            "informações": {
                "Nome": person.name,
                "Idade": person.age,
                "Sexo": person.sex,
                "CPF": person.cpf,
                "Endereço": person.address,
                "Telefone": person.phone
            }
        }