from .interface.notification_service_interface import NotificationServiceInterface
from models.entities.appointement import Appointment

class NotificationConsoleService(NotificationServiceInterface):
    def send_notification(self, appointment: Appointment) -> None:
        print("\n=== Notificação de Consulta Agendada ===")
        print(f"Consulta agendada com sucesso para {appointment.name}!")
        print(f"Data da Consulta: {appointment.appointment_date}")
        print(f"Hora da Consulta: {appointment.appointment_time}")
        print("========================================\n")