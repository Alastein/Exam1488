from datetime import datetime, timedelta


class Persona:
    def __init__(self, fio, birthdate, address):
        self.fio = fio
        self.birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
        self.address = address

    def days_until_next_birthday(self):
        today = datetime.today()
        next_birthday = self.birthdate.replace(year=today.year)

        if next_birthday < today:
            next_birthday = next_birthday.replace(year=today.year + 1)

        delta = next_birthday - today
        return delta.days


# Пример использования
person = Persona("Иван Иванов", "1990-06-26", "ул. Пушкина, д. 10")
print(f"Количество дней до следующего дня рождения: {person.days_until_next_birthday()}")
