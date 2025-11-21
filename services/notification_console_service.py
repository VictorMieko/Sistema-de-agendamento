from .interface.notification_service_interface import NotificationServiceInterface
from models.entities.appointement import Appointment

# simula service de email
class NotificationConsoleService(NotificationServiceInterface):
    def send_notification(self, appointment: Appointment) -> None:

        success_message = f"""
            \n=== Notificação de Consulta Agendada de Console ===

            Consulta agendada com sucesso para {appointment.name}
            Médico marcado: {appointment.doctor_name}
            Data da Consulta: {appointment.appointment_date}
            Hora da Consulta: {appointment.appointment_time}
        """
        print("-" * 10)
        print(success_message)