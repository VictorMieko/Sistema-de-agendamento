from view.people_register_view import RegisterPeopleView
from controllers.people_register_controller import PeopleRegisterController
from models.interfaces.person_repository_interface import PersonRepositoryInterface

def people_register_constructor(repository_interface: PersonRepositoryInterface):
    # instancia a view e o controller
    people_register_view = RegisterPeopleView()
    people_register_controller = PeopleRegisterController(repository_interface)

    # envia para o controller
    new_people_information = people_register_view.registry_people_view() # chama a view para registras as pessoas
    response = people_register_controller.register_person(new_people_information) # joga as informações para o controller

    # retorna uma resposta para a view
    if response["success"]:
        people_register_view.registry_person_success(response["message"])
    else:
        people_register_view.registry_person_error(response["error"])