import pytest
from unittest.mock import MagicMock
from controllers.new_appointment_controller import NewAppointmentController
from models.entities.person import Person
from models.entities.appointement import Appointment

# Importamos as INTERFACES para criar os Mocks
from models.interfaces.person_repository_interface import PersonRepositoryInterface
from models.interfaces.appointment_repository_interface import AppointmentRepositoryInterface
from services.interface.notification_service_interface import NotificationServiceInterface

# === FIXTURES (Configuração Inicial) ===
# Isso roda antes de cada teste para preparar o terreno
@pytest.fixture
def mock_person_repo():
    return MagicMock(spec=PersonRepositoryInterface)

@pytest.fixture
def mock_appointment_repo():
    return MagicMock(spec=AppointmentRepositoryInterface)

@pytest.fixture
def mock_notification_service():
    return MagicMock(spec=NotificationServiceInterface)

@pytest.fixture
def controller(mock_person_repo, mock_appointment_repo, mock_notification_service):
    # Injeta os Mocks no Controller em vez das classes reais
    return NewAppointmentController(
        mock_appointment_repo,
        mock_person_repo,
        mock_notification_service
    )

# === TESTES (Cenários) ===

def test_schedule_appointment_success(controller, mock_person_repo, mock_appointment_repo, mock_notification_service):
    """
    Cenário: Dados válidos, pessoa existe, horário livre.
    Resultado Esperado: Sucesso e métodos chamados corretamente.
    """
    # ARRANGE (Preparação)
    # 1. Simulamos que o repositório de pessoas encontra o "Jose"
    person_fake = Person("Jose", 30, "M", "123.123.123.12", "Rua A", "12312312312")
    mock_person_repo.find_person_by_name.return_value = person_fake
    
    # 2. Simulamos que NÃO há conflito de horário (retorna None)
    mock_appointment_repo.find_person_by_name.return_value = None

    input_data = {
        "name": "Jose",
        "appointment_date": "20/11",
        "appointment_time": "10:00"
    }

    # ACT (Ação)
    response = controller.schedule_appointment(input_data)

    # ASSERT (Verificação)
    assert response["success"] is True
    assert response["message"]["name"] == "Jose"
    
    # Verificamos se o registro foi chamado 1 vez
    mock_appointment_repo.register_appointment.assert_called_once()
    
    # Verificamos se a notificação foi enviada
    mock_notification_service.send_notification.assert_called_once()


def test_schedule_appointment_person_not_found(controller, mock_person_repo, mock_appointment_repo):
    """
    Cenário: Pessoa não existe no banco.
    Resultado Esperado: Erro e NÃO deve tentar salvar consulta.
    """
    # ARRANGE
    # Simulamos que o repositório NÃO encontra ninguém (retorna None)
    mock_person_repo.find_person_by_name.return_value = None

    input_data = {
        "name": "Fantasma",
        "appointment_date": "20/11",
        "appointment_time": "10:00"
    }

    # ACT
    response = controller.schedule_appointment(input_data)

    # ASSERT
    assert response["success"] is False
    assert "Paciente não encontrado" in response["error"]
    
    # Importante: Garante que NÃO tentou salvar nada no banco
    mock_appointment_repo.register_appointment.assert_not_called()


def test_schedule_appointment_conflict(controller, mock_person_repo, mock_appointment_repo):
    """
    Cenário: Pessoa existe, mas horário já está ocupado.
    Resultado Esperado: Erro de conflito.
    """
    # ARRANGE
    person_fake = Person("Jose", 30, "M", "123", "Rua A", "999")
    mock_person_repo.find_person_by_name.return_value = person_fake

    # Simulamos que JÁ EXISTE uma consulta nesse horário
    conflict_appointment = Appointment(person_fake, "20/11", "10:00")
    mock_appointment_repo.check_appointments_by_patient_date.return_value = conflict_appointment

    input_data = {
        "name": "Jose",
        "appointment_date": "20/11/",
        "appointment_time": "10:00"
    }

    # ACT
    response = controller.schedule_appointment(input_data)

    # ASSERT
    assert response["success"] is False
    assert "Já existe uma consulta agendada para esse paciente." in response["error"]
    
    mock_appointment_repo.register_appointment.assert_not_called()