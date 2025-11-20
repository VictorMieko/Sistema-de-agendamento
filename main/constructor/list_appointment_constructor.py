from view.list_appointment_view import ListAppointmentView
from controllers.list_appointment_controller import ListAppointmentController

from models.interfaces.appointment_repository_interface import AppointmentRepositoryInterface

def list_appointment_constructor(appointment_interface: AppointmentRepositoryInterface):
    list_appointment_view = ListAppointmentView()
    list_appointment_controller = ListAppointmentController(appointment_interface)

    response = list_appointment_controller.list_all_appointment()

    if response["success"]:
        list_appointment_view.list_appointment_success(response["message"])
    else:
        list_appointment_view.list_appointment_error(response["error"])