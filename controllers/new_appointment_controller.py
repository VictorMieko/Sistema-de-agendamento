from typing import Dict
from datetime import datetime, time
from models.entities.appointement import Appointment
from models.entities.person import Person
from models.interfaces.appointment_repository_interface import AppointmentRepositoryInterface
from models.interfaces.person_repository_interface import PersonRepositoryInterface
from services.notification_console_service import NotificationConsoleService 

class NewAppointmentController:
    def __init__(self, 
                appointment_interface: AppointmentRepositoryInterface,
                person_interface: PersonRepositoryInterface,
                notification_service: NotificationConsoleService) -> None:
        self.__appointment_repository = appointment_interface
        self.__person_repository = person_interface
        self.__notification_service = notification_service

    def schedule_appointment(self, new_appointment_information: Dict) -> Dict:
        try:
            self.__validate_fields(new_appointment_information)
            person_obj = self.__validate_business_rules(new_appointment_information)
            new_appointment = self.__register_appointment_in_repository(person_obj, new_appointment_information)   
            self.__notification_service.send_notification(new_appointment)         
            response = self.__format_response(new_appointment)
            return {"success": True, "message": response} # retorna um dicionario indicando sucesso
        except Exception as exception:
            return {"success": False, "error": str(exception)} # retorna um dicionario indicando o erro
        
    def __validate_fields(self, new_appointment_information: Dict) -> None:
        if not isinstance (new_appointment_information["name"], str):
            raise Exception("Campo 'nome do paciente' incorreto.")
        
        current_year = datetime.now().year
        try: 
            date_str = new_appointment_information["appointment_date"]
            date_obj = datetime.strptime(f"{date_str}/{current_year}", "%d/%m/%Y")
        except ValueError: raise Exception("Campo 'data da consulta' incorreto. Use o formato DD")

        try: datetime.strptime(new_appointment_information["appointment_time"], "%H:%M")
        except ValueError: raise Exception("Campo 'hora da consulta' incorreto. Use o formato HH:MM.")

        is_weekday = date_obj.weekday()
        if is_weekday >= 5: raise Exception("Não é possível marcar em finais de semana. Escolha um dia útil.")

    def __validate_business_rules(self, new_appointment_information: Dict) -> Person:
        name = new_appointment_information["name"]
        date = (new_appointment_information["appointment_date"])
        appoint_time = new_appointment_information["appointment_time"]

        if not name or not date or not appoint_time:
            raise Exception("Todos os campos são obrigatórios para agendar uma consulta.")

        person = self.__person_repository.find_person_by_name(name)
        if not person: raise Exception("Paciente não encontrado no repositório. Por favor, registre o paciente antes de agendar a consulta.")

        existing_appointment = self.__appointment_repository.check_appointments_by_patient_date(date, appoint_time)
        if existing_appointment: raise Exception("Já existe uma consulta agendada para esse paciente.")

        appoint_time_obj = datetime.strptime(appoint_time, "%H:%M").time()
        start_hour = time(8, 0)
        end_hour = time(18, 0)

        if appoint_time_obj < start_hour or appoint_time_obj > end_hour:
            raise Exception("Horário inválido. O horário comercial é das 08:00 às 18:00.")

        return person

    def __register_appointment_in_repository(self, person: Person, new_appointment_information: Dict) -> Appointment:
        appointment_date = new_appointment_information["appointment_date"]
        appointment_time = new_appointment_information["appointment_time"]

        new_appointment = Appointment(person, appointment_date, appointment_time)
        self.__appointment_repository.register_appointment(new_appointment)

        return new_appointment

    def __format_response(self, appointment: Appointment) -> Dict:
        response = {
            "name": appointment.name,
            "appointment_date": appointment.appointment_date,
            "appointment_time": appointment.appointment_time,
        }
        return response