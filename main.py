# # 1 misol
# # class Getlower:
# #     def __init__(self, name):
# #         self.name = name
# #     def __get__(self, instance, owner):
# #         return instance.__dict__.get(self.name)
# #     def __set__(self, instance, value):
# #         instance.__dict__[self.name] = value.lower() if isinstance(value, str) else value
# #     def __delete__(self, instance):
# #         del instance.__dict__[self.name]
# # class Car:
# #     attribute = Getlower("a")
# # class Animal:
# #     attribute = Getlower("a")
# # a = Car()
# # b = Animal()
# # a.attribute = "BMW"
# # b.attribute = "Dog"
# # print(a.attribute)
# # print(b.attribute)
# import time
# #  2 misol
# # class Musbat:
# #     def __init__(self):
# #         self._value = None
# #     def __get__(self, instance, owner):
# #         return self._value
# #     def __set__(self, instance, value):
# #         if value < 0:
# #             raise ValueError("Qiymat manfiy bo'lishi mumkin emas.")
# #         self._value = value
# #     def __delete__(self, instance):
# #         del self._value
# # class Number:
# #     numer = Musbat()
# # son = Number()
# # son.numer=-1
# # print(son.numer)
# #
# #
# #
# # 1 misol
# # from datetime import datetime, timedelta
# # bugung = datetime.now()
# # oldingi_sana = bugung - timedelta(days=7)
# # print("7 kun oldingi sana:", oldingi_sana.strftime("%Y-%m-%d"))
# #
# # 2 misol
# # from datetime import datetime
# # def get_age(birth_date):
# #     today = datetime.today()
# #     age = today.year - birth_date.year
# #
# #     if (today.month, today.day) < (birth_date.month, birth_date.day):
# #         age -= 1
# #     return age
# # def main():
# #     birth_year = input("Enter your birth year (YYYY): ")
# #     birth_month = input("Enter your birth month (MM): ")
# #     birth_day = input("Enter your birth day (DD): ")
# #     birth_date = datetime(int(birth_year), int(birth_month), int(birth_day))
# #     age = get_age(birth_date)
# #     if birth_date.month == datetime.today().month and birth_date.day == datetime.today().day:
# #         print("Happy Birthday!")
# #     else:
# #         print(f"Your age is: {age}")
# # if __name__ == "__main__":
# #     main()
# #3 misol
#
# # from datetime import datetime
# # vaqt1 = input("sanani kiriying : ")
# # vaqt1 = datetime.strptime(vaqt1,"%Y-%m-%d")
# # vaqt2 = input("ikkinchi sanani kiriying  :;")
# # vaqt2 =  datetime.strptime(vaqt2,"%Y-%m-%d")
# # kunlar = (vaqt2 - vaqt1)
# # print ("oraliq mudat ",kunlar)
#
#
# #  Math modulli bilan ishlash
#
# # 1 misol
# # import math
# # def aylana_yuzasi(diametr):
# #     radius = diametr / 2
# #     yuzasi = math.pi * (radius ** 2)
# #     return yuzasi
# # diametr = float(input("Aylananing diametrini kiriting: "))
# # yuza = aylana_yuzasi(diametr)
# # print(f"Aylananing yuzasi: {yuza:2}")
#
# #  2 misol]
# #
# import math
# # a = 4
# # if a > 0:
# #     b= (pow(a,2))
# #     c= (pow(a, 3))
# #     print(f"kvadrat { b } kub { c}")
# # else:
# #     raise ValueError("Son 0 dan kichik bolmasligi zarur")
#
# #  Random moduli bilan ishlash
#
# #  1 msiol
# # import random
# # a = [random.randint(1, 100) for _ in range(5)]
# # b = [round(random.uniform(0, 1), 1) for _ in range(3)]
# # son = a + b
# # qiymat = sum(son) / len(son)
# # print("Butun sonlar:", a)
# # print("Haqiqiy sonlar:", b)
# # print("O'rtacha qiymat:", qiymat)
