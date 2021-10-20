#!/usr/bin/env python3

# Created by: Rodas Nega
# Created on: October 2021
# This program prints user inputs into their mailing address


def apartment_check(
    full_name,
    street_number,
    street_name,
    city_name,
    province,
    postal_code,
    apartment=None,
):

    # process
    if apartment is not None:
        live_in_apartment = "{0} \n{1}-{2} {3} \n{4} {5}  {6}".format(
            full_name,
            apartment,
            street_number,
            street_name,
            city_name,
            province,
            postal_code,
        )
    else:
        live_in_apartment = "{0} \n{1} {2} \n{3} {4}  {5}".format(
            full_name, street_number, street_name, city_name, province, postal_code
        )

    return live_in_apartment.upper()


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

    try:
        apartment_int = int(apartment)
        street_number_int = int(street_number)

        if apartment_int or street_number_int < 0:
            print("")
            print("That is an invalid number.")

        if apartment is not None:
            prompt_list = apartment_check(
                full_name,
                street_number,
                street_name,
                city_name,
                province,
                postal_code,
                apartment,
            )

        else:
            prompt_list = apartment_check(
                full_name, street_number, street_name, city_name, province, postal_code
            )

    except Exception:
        print("")
        print("That is an invalid number.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
