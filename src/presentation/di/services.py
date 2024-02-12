from src.domain.usecases.phonebook import PhoneBookInteractor
from src.infrastructure.filestorage.interfaces import AbstractRepository
from src.presentation.di.storage import json_storage, csv_storage    # noqa


def phonebook_service(repo: AbstractRepository = json_storage()) -> PhoneBookInteractor:
    return PhoneBookInteractor(repo)
