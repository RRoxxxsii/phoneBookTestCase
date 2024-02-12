from abc import ABC, abstractmethod

from src.domain.dto.phonebook import ContactsDTO


class AbstractRepository(ABC):

    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    @abstractmethod
    def read(self) -> list[list[str]] | list[dict[str]]:
        raise NotImplementedError

    @abstractmethod
    def create(self, dto: ContactsDTO) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, dto: ContactsDTO, mobile: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def find(self, dto: ContactsDTO) -> list[list[str]] | list[dict[str]]:
        raise NotImplementedError
