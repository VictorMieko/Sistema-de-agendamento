import os
from typing import Dict

class NewAppointmentView:
    def schedule_appointment_view(self) -> str:
        os.system('cls || clear')

        print("=== Agendamento de Consulta ===\n")
        name = input("Nome do paciente: ")     
        cpf = input("Cpf do paciente: ")   
        doctor_name = input("Nome do Médico: ")
        appointment_date = input("Data da consulta (DD/MM): ")
        appointment_time = input("Hora da consulta (HH:MM): ")

        appointment_information = {
            "name": name,
            "cpf": cpf,
            "doctor_name": doctor_name,
            "appointment_date": appointment_date,
            "appointment_time": appointment_time
        }

        return appointment_information
    
    def appointment_success(self, message: Dict) -> None:
        os.system('cls || clear')

        success_message = f"""
            === Consulta Agendada com Sucesso ===

            Paciente: {message['name']}
            CPF do paciente: {message['cpf']}
            Nome do Médico: {message['doctor_name']}
            Data: {message['appointment_date']}
            Hora: {message['appointment_time']}
        """
        print(success_message)

    def appointment_error(self, error: Dict) -> None:
        os.system('cls || clear')

        error_message = f"""
            === Erro no Agendamento ===

            Motivo: {error}
        """
        print(error_message)