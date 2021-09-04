import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

user_i = input("please enter your phone number:")

def numbertracker(num):
    v_number = phonenumbers.parse(num, 'CH')
    print(geocoder.description_for_number(v_number, 'en'))

def numberprovider(num):
    provider = phonenumbers.parse(num, "RO")
    print(carrier.name_for_number(provider, 'en'))

def fun(num):
    numbertracker(num)
    numberprovider(num)

fun(user_i)