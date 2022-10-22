import phonenumbers 
from phonenumbers import timezone, geocoder, carrier
number1 = input("Enter your number which you have to tress +_____________  :-")
phone = phonenumbers.parse(number1)#it is gives national code of this number
time_zone = timezone.time_zones_for_number(phone)#it is gives time of this number cuurent
car = carrier.name_for_number(phone,"en")#it is gives name of this person 
reg = geocoder.description_for_number(phone,"en")#it is gives registraction details
print(phone)
print(time_zone)
print(car)
print(reg)
