from typing import Optional
from abc import ABC, abstractmethod
from models.entities.person import Person

class PersonRepositoryInterface(ABC):
    @abstractmethod
    def registry_person(self, person: Person) -> None:
        pass

    @abstractmethod
    def find_person_by_name(self, name: str) -> Optional[Person]:
        pass

    @abstractmethod
    def find_person_by_cpf(self, cpf: str) -> Person | None:
        pass