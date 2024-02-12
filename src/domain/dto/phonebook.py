from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class ContactsDTO:
    name: str = None
    surname: str = None
    patronymic: str = None
    company: str = None
    working_mobile: str = None
    personal_mobile: str = None

    def dict(self) -> dict:
        return {k: str(v) for k, v in asdict(self).items()}
