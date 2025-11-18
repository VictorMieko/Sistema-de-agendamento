from main.constructor.introduction_process import introduction_process
from main.constructor.people_register_constructor import people_register_constructor
from main.constructor.people_finder_constructor import people_finder_constructor
from main.constructor.new_appointment_constructor import new_appointment_constructor

from models.repository.appointment_repository import AppointmentRepository
from models.repository.person_repository import PersonRepository

from services.notification_console_service import NotificationConsoleService

appointment_repository = AppointmentRepository()
person_repository = PersonRepository()

notification_service = NotificationConsoleService()

def start() -> None:
    while True:
        command = introduction_process()

        if command == "1": people_register_constructor(person_repository)
        elif command == "2": people_finder_constructor(person_repository)
        elif command == "3": new_appointment_constructor(appointment_repository, person_repository, notification_service)
        elif command == "0": exit()
        else: print("\nComando inválido! Tente novamente. \n\n")   