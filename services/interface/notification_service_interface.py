from abc import ABC, abstractmethod
from models.entities.appointement import Appointment

class NotificationServiceInterface(ABC):
    @abstractmethod
    def send_notification(self, appointment: Appointment) -> None:
        pass