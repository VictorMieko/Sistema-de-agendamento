from view.people_finder_view import PeopleFinderView
from controllers.people_finder_controller import PeopleFinderController
from models.interfaces.person_repository_interface import PersonRepositoryInterface

def people_finder_constructor(repository_interface: PersonRepositoryInterface):
    # instancia a view
    people_finder_view = PeopleFinderView()
    people_finder_controller = PeopleFinderController(repository_interface)

    # chama a view para buscar as pessoas
    person_finder_information = people_finder_view.find_people_view()
    response = people_finder_controller.find_by_cpf(person_finder_information)

    if response["success"]:
        people_finder_view.find_person_success(response["message"])
    else:
        people_finder_view.find_person_error(response["error"])