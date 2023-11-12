from uuid import uuid4


class Shaxs:
    """Shaxslar haqida ma'lumot"""

    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f" Passport: {self.passport}, {self.tyil}-yilda tug`ilgan"
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    __talaba_soni = 0

    def __init__(self, ism, familiya, passport, tyil, bosqich):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil, )
        self.__id = uuid4()
        self.bosqich = bosqich
        Talaba.__talaba_soni += 1

    @classmethod
    def get_talabalarsoni(cls):
        return f"Talabalar soni:{cls.__talaba_soni}"

    def get_id(self):
        """Talabaning ID raqami"""
        return self.__id

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def __le__(self, boshqa_talabalar):
        return self.bosqich < boshqa_talabalar.bosqich

    def __eq__(self, boshqa_talabalar):
        return self.bosqich == boshqa_talabalar.bosqich

    def __lt__(self, boqshqa_talabalar):
        return self.bosqich < boqshqa_talabalar.bosqich

    def __repr__(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.__id}"
        return info


talaba1 = Talaba("Shoxurx", "Xasanov", "fsrrf242", 2009, 1)
talaba2 = Talaba("Xumoyun", "Baxadirov", "adcd213", 2009, 1)
print(talaba1 == talaba2)
talaba3 = Talaba("Aziz", "Lazizov", "fsrrfrf", 2005, 3)
talaba4 = Talaba("Temur", "Tajibayev", "fsrrfrf", 2004, 4)
print(talaba3 <= talaba4)
talaba5 = Talaba("Jonibek", "Uralov", "3grgq3", 2001, 4)
print(talaba5>talaba1)
print(talaba3<talaba1)