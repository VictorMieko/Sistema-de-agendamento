import os
from typing import Dict, List

class ListAppointmentView:
    def list_appointment_success(self, appointment_list: List[Dict]) -> None:
        os.system('cls || clear')

        for item in appointment_list:
            info = item["informações"]

            print(f"Nome do paciente: {info['name']}")
            print(f"Médico: {info['doctor_name']}")
            print(f"Data da consulta: {info['appointment_date']}")
            print(f"Hora da consulta: {info['appointment_time']}\n")
            print("-" * 10)

    def list_appointment_error(self, error: Dict) -> None:
        os.system('cls || clear')

        error_message = f"""
        === Erro na busca ===

        Motivo: {error}
        """
        print(error_message)
