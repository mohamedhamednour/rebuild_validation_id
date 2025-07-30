from .conf import VALIDYEARS, EGYPT_GOVERNORATES
from datetime import datetime

class NationalIdValidator:

    def __init__(self, id_number: str):
        self.id_number = id_number
        self.birthdate = None

    def __str__(self):
        return f"NationalIdValidator(id_number={self.id_number})"

    def __repr__(self):
        return f"NationalIdValidator(id_number={self.id_number})"
   
    def valid_id(self) -> None:
        if len(self.id_number) != 14 or not self.id_number.isdigit():
            raise ValueError("The ID number must be 14 digits long and contain only numbers.")

    def calculate_birth_year(self) -> int:
        if self.id_number[0] not in VALIDYEARS:
            raise ValueError(f"The first digit must be either {', '.join(VALIDYEARS)}.")
        first_digit = int(self.id_number[0])
        year_prefix = 1900 if first_digit == 2 else 2000
        return year_prefix + int(self.id_number[1:3])


    def extract_birthdate_is_valid(self) -> str:
        year = self.calculate_birth_year()
        month = int(self.id_number[3:5])
        day = int(self.id_number[5:7])
        
        if month < 1 or month > 12:
            raise ValueError("Invalid month in ID number.")
        
        if day < 1 or day > 31:
            raise ValueError("Invalid day in ID number.")

        self.birthdate = datetime(year, month, day).strftime('%Y-%m-%d')
        
    def check_governorates(self) -> None:
        code = self.id_number[7:9]
        if code not in EGYPT_GOVERNORATES:
            raise ValueError('Invalid governorate code')

    def build(self) :
        self.valid_id()
        self.extract_birthdate_is_valid()
        self.check_governorates()
        self.calculate_birth_year()

        return self
