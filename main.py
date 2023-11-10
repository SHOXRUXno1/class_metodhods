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

    def __init__(self, ism, familiya, passport, tyil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.__id = uuid4()
        self.bosqich = 1
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

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.__id}"
        return info


Talaba1 = Talaba(f"Shoxrux", "Xasanov", "adAd", 2009, )
Talaba2 = Talaba(f"Azizbek", "Alimov", "aaa242", 2001, )
Talaba3 = Talaba(f"Fazliddin", "Dabuluov", "adsdaa242", 2005)
Talaba4 = Talaba(f"Lziz", "Raxmonov", "aaa242", 2008, )
print(Talaba1.get_talabalarsoni())
print(Talaba1.get_info())
print(Talaba2.get_info())
print(Talaba3.get_info())
print(Talaba4.get_info())
