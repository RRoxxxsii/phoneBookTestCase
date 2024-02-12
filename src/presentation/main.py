import sys

from src.domain.dto.phonebook import ContactsDTO
from src.presentation.controllers.phonebook import (
    read_data_from_phonebook,
    create_record_in_phonebook,
    find_record_in_phonebook,
    update_record_in_phonebook,
)


def form_data() -> ContactsDTO:
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    company = input("Введите компанию: ")
    working_mobile = input("Введите номер рабочего телефона в числовом формате: ")
    personal_mobile = input("Введите номер личного телефона в числовом формате: ")
    dto = ContactsDTO(
        name=name if name else None,
        surname=surname if surname else None,
        patronymic=patronymic if patronymic else None,
        company=company if company else None,
        working_mobile=working_mobile if working_mobile else None,
        personal_mobile=personal_mobile if personal_mobile else None,
    )
    return dto


def start_app(args: list) -> None:

    if len(args) == 1:
        print("Необходимо ввести действие в качестве второго аргумента")
    else:
        if args[1] == "read":
            read_data_from_phonebook()

        if args[1] == "create":
            create_record_in_phonebook(form_data())

        if args[1] == "update":
            mobile_identifier = input(
                "Введите номер рабочего телефона, для которого необходимо обновить данные: "
            )
            update_record_in_phonebook(form_data(), mobile_identifier)

        if args[1] == "find":
            find_record_in_phonebook(form_data())


if __name__ == "__main__":
    start_app(sys.argv)
