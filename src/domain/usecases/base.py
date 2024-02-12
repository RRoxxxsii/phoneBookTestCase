from src.infrastructure.filestorage.interfaces import AbstractRepository


class BaseUseCase:

    def __init__(self, repo: AbstractRepository) -> None:
        self.repo = repo


class BaseInteractor:

    def __init__(self, repo: AbstractRepository) -> None:
        self.repo = repo
