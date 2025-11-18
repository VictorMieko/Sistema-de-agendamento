# captura os dados para o banco de dados

from models.entities.person import Person
from models.interfaces.person_repository_interface import PersonRepositoryInterface
from typing import Optional

class PersonRepository(PersonRepositoryInterface):
    def __init__(self):
        self.__people = []

    # Armazena uma nova pessoa no "banco de dados"
    def registry_person(self, person: Person) -> None:
        self.__people.append(person)

    def find_person_by_name(self, name: str) -> Person | None:
        for person in self.__people:
            if person.name == name:
                return person
        return None

person_repository = PersonRepository()