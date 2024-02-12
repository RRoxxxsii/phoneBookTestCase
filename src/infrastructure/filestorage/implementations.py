import json

from src.domain.dto.phonebook import ContactsDTO
from src.infrastructure.filestorage.interfaces import AbstractRepository


class JSONRepository(AbstractRepository):

    def read(self) -> list[dict[str]]:
        with open(self.storage_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def create(self, dto: ContactsDTO) -> None:
        with open(self.storage_path, "r+", encoding="utf-8") as file:
            data = json.load(file)
            data["contacts"].append(dto.dict())
            file.seek(0)
            file.write(json.dumps(data, indent=4, ensure_ascii=False))

    def update(self, dto: ContactsDTO, working_mobile: str) -> None:
        with open(self.storage_path, "r+", encoding="utf-8") as file:
            data = json.load(file)
            for contact in data["contacts"]:
                if contact.get("working_mobile") == working_mobile:
                    if dto.name:
                        contact["name"] = dto.name
                    if dto.surname:
                        contact["surname"] = dto.surname
                    if dto.patronymic:
                        contact["patronymic"] = dto.patronymic
                    if dto.company:
                        contact["company"] = dto.company
                    if dto.working_mobile:
                        contact["working_mobile"] = dto.working_mobile
                    if dto.personal_mobile:
                        contact["personal_mobile"] = dto.personal_mobile
                    break
            file.seek(0)
            file.write(json.dumps(data, indent=4, ensure_ascii=False))

    def find(self, dto: ContactsDTO) -> list[dict[str]]:
        with open(self.storage_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            records = []
            for contact in data["contacts"]:
                if (
                    (dto.name == contact["name"] or not dto.name)
                    and (dto.surname == contact["surname"] or not dto.surname)
                    and (dto.patronymic == contact["patronymic"] or not dto.patronymic)
                    and (dto.company == contact["company"] or not dto.company)
                    and (
                        dto.working_mobile == contact["working_mobile"]
                        or not dto.working_mobile
                    )
                    and (
                        dto.personal_mobile == contact["personal_mobile"]
                        or not dto.personal_mobile
                    )
                    and any(
                        (
                            dto.name,
                            dto.surname,
                            dto.patronymic,
                            dto.company,
                            dto.working_mobile,
                            dto.personal_mobile,
                        )
                    )
                ):
                    records.append(contact)
            return records


class CSVRepository(AbstractRepository):
    def read(self) -> list[list[str]]:
        with open(self.storage_path, "r", encoding="utf-8") as file:
            data = file.read()
            table = [r.split(",") for r in data.splitlines()]
            return table

    def create(self, dto: ContactsDTO) -> None:
        with open(self.storage_path, "a", encoding="utf-8") as file:
            file.write(
                f"\n{','.join([str(dto.name), str(dto.surname), str(dto.patronymic), str(dto.company), str(dto.working_mobile), str(dto.personal_mobile)])}"
            )

    def update(self, dto: ContactsDTO, working_mobile: str) -> None:
        with open(self.storage_path, "r+", encoding="utf-8") as file:
            data = file.read()
            table = [r.split(",") for r in data.splitlines()]
            for contact in table[1:]:
                if contact[4] == working_mobile:
                    if dto.name:
                        contact[0] = dto.name
                    if dto.surname:
                        contact[1] = dto.surname
                    if dto.patronymic:
                        contact[2] = dto.patronymic
                    if dto.company:
                        contact[3] = dto.company
                    if dto.working_mobile:
                        contact[4] = dto.working_mobile
                    if dto.personal_mobile:
                        contact[5] = dto.personal_mobile
                    break
            file.seek(0)
            file.write("\n".join([",".join([word for word in row]) for row in table]))

    def find(self, dto: ContactsDTO) -> list[list[str]]:
        with open(self.storage_path, "r+", encoding="utf-8") as file:
            data = file.read()
            table = [r.split(",") for r in data.splitlines()]
            records = []
            for contact in table[1:]:
                if (
                    (dto.name == contact[0] or not dto.name)
                    and (dto.surname == contact[1] or not dto.surname)
                    and (dto.patronymic == contact[2] or not dto.patronymic)
                    and (dto.company == contact[3] or not dto.company)
                    and (dto.working_mobile == contact[4] or not dto.working_mobile)
                    and (dto.personal_mobile == contact[5] or not dto.personal_mobile)
                    and any(
                        (
                            dto.name,
                            dto.surname,
                            dto.patronymic,
                            dto.company,
                            dto.working_mobile,
                            dto.personal_mobile,
                        )
                    )
                ):
                    records.append(contact)
            return records
