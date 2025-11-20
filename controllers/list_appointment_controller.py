from typing import Dict, List
from models.interfaces.appointment_repository_interface import AppointmentRepositoryInterface
from models.entities.appointement import Appointment

class ListAppointmentController:
    def __init__(self, appointment_interface: AppointmentRepositoryInterface):
        self.__appointment_interface = appointment_interface

    def list_all_appointment(self) -> Dict:
        try:
            appointment = self.__list_appointment_in_repository()
            response = self.__format_list(appointment)
            return {"success": True, "message": response}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __list_appointment_in_repository(self) -> Appointment:
        appointment = self.__appointment_interface.list_all_appointment()
        if not appointment: raise Exception("Nenhuma consulta encontrada no repositório.")

        return appointment

    def __format_list(self, appointments: List[Appointment]) -> List[Dict]:
        formatted_list = []
        for appt in appointments:
            appointment_dict = {
                "informações": {
                    "name": appt.name,
                    "doctor_name": appt.doctor_name,
                    "appointment_date": appt.appointment_date,
                    "appointment_time": appt.appointment_time
                }
            }
            formatted_list.append(appointment_dict)
        return formatted_list
