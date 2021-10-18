#!/usr/bin/env python3

# Created by: Rodas Nega
# Created on: October 2021
# This program prints user inputs into their mailing address


def apartment_check(apartment=None):
    # return apartment value

    # process
    live_in_apartment = apartment
    if apartment != None:
        live_in_apartment = live_in_apartment + " " + apartment[0]
    live_in_apartment = ""

    return live_in_apartment


def main():
    # user answers prompts and outputs mailing address
    apartment = None

    # input & output
    full_name = input("Enter your full name: ")
    question_for_user = input("Do you live in an apartment? (y/n): ")
    if question_for_user.upper() == "Y" or question_for_user.upper() == "YES":
        apartment = input("Enter your apartment number: ")
    street_number = input("Enter your street number: ")
    street_name = input("Enter your street name AND type (Main St, Express Pkwy…): ")
    city_name = input("Enter your city name: ")
    province = input("Enter your province (as an abbreviation, ex: ON, BC): ")
    postal_code = input("Enter your postal code (123 456): ")

    if question_for_user.upper() == "Y" or question_for_user.upper() == "YES":
        prompt_list = apartment_check(apartment)
        print("\n" + full_name.upper())
        print(apartment + "-" + street_number.upper(), street_name.upper())
        print(city_name.upper(), province.upper(), "", postal_code.upper())

    else:
        prompt_list = apartment_check(apartment)
        print("\n" + full_name.upper())
        print(street_number.upper(), street_name.upper())
        print(city_name.upper(), province.upper(), "", postal_code.upper())

    print(prompt_list)


if __name__ == "__main__":
    main()
