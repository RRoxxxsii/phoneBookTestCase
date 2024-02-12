import os
from dataclasses import dataclass


@dataclass
class Settings:
    JSON_PATH = os.path.join(
        os.path.abspath(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..")
        ),
        "storages/phonebook.json",
    )

    CSV_PATH = os.path.join(
        os.path.abspath(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../..")
        ),
        "storages/phonebook.csv",
    )


def get_settings() -> Settings:
    return Settings()
