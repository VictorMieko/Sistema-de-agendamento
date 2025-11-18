from view.new_appointment_view import NewAppointmentView

from controllers.new_appointment_controller import NewAppointmentController

from models.interfaces.person_repository_interface import PersonRepositoryInterface
from models.interfaces.appointment_repository_interface import AppointmentRepositoryInterface

from services.interface.notification_service_interface import NotificationServiceInterface

def new_appointment_constructor(appointment_interface: AppointmentRepositoryInterface, person_interface: PersonRepositoryInterface, notification_interface: NotificationServiceInterface) -> None:
    # instancia a view e o controller
    new_appointment_view = NewAppointmentView()
    new_appointment_controller = NewAppointmentController(appointment_interface, person_interface, notification_interface)

    # envia para o controller
    new_appointment_information = new_appointment_view.schedule_appointment_view() # chama a view para agendar a consulta
    response = new_appointment_controller.schedule_appointment(new_appointment_information) # joga as informações para o controller

    # retorna uma resposta para a view
    if response["success"]:
        new_appointment_view.appointment_success(response["message"])
    else:
        new_appointment_view.appointment_error(response["error"])