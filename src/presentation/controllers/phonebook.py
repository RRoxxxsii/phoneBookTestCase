from src.domain.dto.phonebook import ContactsDTO
from src.domain.usecases.phonebook import PhoneBookInteractor
from src.presentation.di.services import phonebook_service


def read_data_from_phonebook(
    service: PhoneBookInteractor = phonebook_service()
) -> None:
    data = service.list_data()
    print(data)


def create_record_in_phonebook(
    dto: ContactsDTO, service: PhoneBookInteractor = phonebook_service()
) -> None:
    service.add_data(dto)


def update_record_in_phonebook(
    dto: ContactsDTO,
    working_mobile: str,
    service: PhoneBookInteractor = phonebook_service(),
) -> None:
    service.update_data(dto, working_mobile)


def find_record_in_phonebook(
    dto: ContactsDTO, service: PhoneBookInteractor = phonebook_service()
) -> None:
    data = service.find_data(dto)
    print(data)
