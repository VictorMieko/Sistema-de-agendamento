from abc import ABC, abstractmethod
from typing import Optional, List
from models.entities.appointement import Appointment

class AppointmentRepositoryInterface(ABC):
    @abstractmethod
    def register_appointment(self, appointment: Appointment) -> None:
        pass

    @abstractmethod
    def check_appointments_by_patient_date(self, date: str, time: str) -> Optional[Appointment]:
        pass

    @abstractmethod
    def list_all_appointment(self) -> list[Appointment]:
        pass