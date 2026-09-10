# BMI Calculator

def get_positive_number(message):
    while True:
        try:
            number = float(input(message))

            if number <= 0:
                print("Please enter a value greater than 0.")
                continue

            return number

        except ValueError:
            print("Please enter numbers only.")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("===== BMI Calculator =====")

    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number("Enter your height in meters: ")

    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)

    print("\n===== Result =====")
    print(f"BMI: {bmi:.2f}")
    print(f"Category: {category}")


main()