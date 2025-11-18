from models.entities.person import Person

class Appointment:
    def __init__(self, person: Person, appointment_date: str, appointment_time: str):
        self.name = person.name
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time