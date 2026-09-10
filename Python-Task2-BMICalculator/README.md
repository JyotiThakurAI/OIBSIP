# BMI Calculator

A simple Python command-line program that calculates Body Mass Index (BMI) using weight and height.

## Features

* Takes weight in kilograms and height in metres.
* Calculates BMI using the standard formula.
* Displays BMI rounded to two decimal places.
* Classifies BMI into different categories.
* Handles invalid, zero, and negative inputs.

## How to Run

Open the project folder in VS Code or a terminal and run:

```powershell
py bmi_calculator.py
```

Then enter:

* Weight in kilograms, for example `70`
* Height in metres, for example `1.75`

The program will display the calculated BMI and its category.

## BMI Formula

```text
BMI = Weight / (Height × Height)
```

## BMI Categories

| BMI          | Category    |
| ------------ | ----------- |
| Below 18.5   | Underweight |
| 18.5 – 24.9  | Normal      |
| 25 – 29.9    | Overweight  |
| 30 or higher | Obese       |

## Example

```text
===== BMI Calculator =====
Enter your weight in kg: 65
Enter your height in meters: 1.70

===== Result =====
BMI: 22.49
Category: Normal
```

## Input Validation

The program asks the user to enter the value again when:

* The input is not a number.
* The input is zero.
* The input is negative.
