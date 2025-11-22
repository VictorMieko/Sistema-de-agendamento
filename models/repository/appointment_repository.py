from models.entities.appointement import Appointment
from models.interfaces.appointment_repository_interface import AppointmentRepositoryInterface
from typing import Optional, List

class AppointmentRepository(AppointmentRepositoryInterface):
    def __init__(self):
        self.__appointments = []

    def register_appointment(self, appointment: Appointment) -> None:
        self.__appointments.append(appointment)
    
    def check_appointments_by_patient_date(self, date: str, time: str) -> Optional[Appointment]:
        for appointment in self.__appointments:
            if appointment.appointment_date == date and appointment.appointment_time == time:
                return appointment
        return None
    
    def list_all_appointment(self) -> list[Appointment]:
        return self.__appointments
    
appointment_repository = AppointmentRepository()
    