from src.infrastructure.filestorage.implementations import JSONRepository, CSVRepository
from src.infrastructure.filestorage.settings import get_settings


def json_storage():
    return JSONRepository(get_settings().JSON_PATH)


def csv_storage():
    return CSVRepository(get_settings().CSV_PATH)
