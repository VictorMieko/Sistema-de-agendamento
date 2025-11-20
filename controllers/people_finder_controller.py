from typing import Dict
from models.interfaces.person_repository_interface import PersonRepositoryInterface
from models.entities.person import Person

class PeopleFinderController:
    def __init__(self, repository_interface=PersonRepositoryInterface):
        self.__repository_interface = repository_interface

    def find_by_cpf(self, person_finder_information: Dict) -> Dict:
        try:
            self.__validade_fields(person_finder_information)
            person = self.__find_person_in_repository(person_finder_information)
            response = self.__format_finder(person)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}
        
    def __validade_fields(self, person_finder_information: Dict) -> None:
        if len(str(person_finder_information["cpf"])) != 14:
            raise Exception("Campo 'cpf' deve conter 14 dígitos (incluindo pontos e traços). ")
        
        cpf = person_finder_information["cpf"]
        if "." not in cpf or "-" not in cpf:
            raise Exception("CPF inválido. Por favor, inclua '.' e '-' (Ex: 123.456.789-00)")
        
    def __find_person_in_repository(self, person_finder_information: Dict) -> Person:
        cpf = person_finder_information["cpf"]
        person = self.__repository_interface.find_person_by_cpf(cpf)
        if not person: raise Exception("Pessoa não encontrada no repositório.")

        return person

    def __format_finder(self, person: Person) -> Dict:
        return {
            "informações": {
                "Nome": person.name,
                "Idade": person.age,
                "Sexo": person.sex,
                "CPF": person.cpf,
                "Endereço": person.address,
                "Telefone": person.phone
            }
        }