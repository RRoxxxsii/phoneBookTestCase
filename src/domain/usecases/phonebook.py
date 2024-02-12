from src.domain.dto.phonebook import ContactsDTO
from src.domain.usecases.base import BaseUseCase, BaseInteractor


class ListDataFromPhoneBook(BaseUseCase):

    def __call__(self) -> list[list[str]] | list[dict[str]]:
        data = self.repo.read()
        return data


class AddDataToPhoneBook(BaseUseCase):

    def __call__(self, dto: ContactsDTO):
        self.repo.create(dto)


class UpdateDataFromPhoneBook(BaseUseCase):

    def __call__(self, dto: ContactsDTO, working_mobile: str):
        self.repo.update(dto, working_mobile)


class FindDataFromPhoneBook(BaseUseCase):

    def __call__(self, dto: ContactsDTO) -> list:
        return self.repo.find(dto)


class PhoneBookInteractor(BaseInteractor):

    def list_data(self) -> list[list[str]] | list[dict[str]]:
        return ListDataFromPhoneBook(self.repo)()

    def add_data(self, dto: ContactsDTO):
        return AddDataToPhoneBook(self.repo)(dto)

    def update_data(self, dto: ContactsDTO, working_mobile: str):
        return UpdateDataFromPhoneBook(self.repo)(dto, working_mobile)

    def find_data(self, dto: ContactsDTO) -> list:
        return FindDataFromPhoneBook(self.repo)(dto)
