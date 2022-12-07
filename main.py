# from replit import clear
import os

def calculate_tax():
    car_value = float(input("Enter Car value($)\n"))
    freight = float(input("Enter freight charges(£)\n"))

    car_value_kes = 141.49 * car_value
    freight_kes = 141.49 * freight

    print(f"Car Value = £{car_value}")
    print(f"Freight charges = £{freight}")

    CIF = float(car_value + freight)
    CIF_kes = 120.75 * CIF

    # print(f"Total CIF Value = £{CIF}")

    import_duty = float(0.25 * CIF)
    import_duty_kes = 120.75 * import_duty

    customs_value = CIF + import_duty
    customs_value_kes = 120.75 * customs_value

    excise_duty = float(0.2 * customs_value)
    excise_duty_kes = 120.75 * excise_duty

    VAT = float(0.16 * (customs_value + import_duty))
    VAT_kes = 120.75 * VAT

    IDF = float(0.035 * CIF)
    IDF_kes = 120.75 * IDF

    rail_levy = float(0.02 * CIF)
    rail_levy_kes = 120.75 * rail_levy

    car_value_after_tax = customs_value + excise_duty + VAT + IDF + rail_levy
    car_value_after_tax_kes = 120.75 * car_value_after_tax

    tax = car_value_after_tax - CIF
    tax_kes = 120.75 * tax

    print(f"Total car value after tax = £{car_value_after_tax}")
    print(f"Total tax = £{tax}")

    total_tax_percent = float(tax / CIF * 100)

    print(f"increment = {total_tax_percent:.2f}%")
    # print(f"Import duty =£{import_duty}")
    # print(f"Excise duty = £{excise_duty}")
    # print(f"Import Declaration Fee = £{IDF}")
    # print(f"V.A.T = £{VAT}")
    # print(f"Railway Levy = £{rail_levy}")



    # print(f"Car Value in KES = KES {car_value_kes:.2f}")
    # print(f"Freight charges in KES = KES {freight_kes:.2f}")
    # print(f"Total CIF Value in KES = KES {CIF_kes:.2f}")
    print(f"Total value in KES after tax = KES {car_value_after_tax_kes:.2f}")
    # print(f"Total tax in KES = KES {tax_kes:.2f}")
    # print(f"Import duty in KES = KES {import_duty_kes:.2f}")
    # print(f"Excise duty in KES = KES {excise_duty_kes:.2f}")
    # print(f"Import Declaration Fee in KES = KES {IDF_kes:.2f}")
    # print(f"V.A.T in KES = KES {VAT_kes:.2f}")
    # print(f"Railway Levy in KES = KES {rail_levy_kes:.2f}")


# def clear():
#     input("Clear terminal? Y or N: ")
#     if clear in ["y", "Y"]:
#         os.system("clear")

calculate_tax()
# clear()

