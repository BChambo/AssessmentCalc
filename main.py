# Ben Chambers

from trilevel import *
from waist_hip import *
replay = True

# Error messages
number_error = "**Error** Make sure you are entering a number."

# Input messages
client = {
	"age": "What is the clients age?: ",
	"weight": "What is the clients weight?: ",
	"waist": "What is the clients waist measurement in cm?: ",
	"hip": "What is the clients weight?: ",
}


# Check to see if input was an int or float. If it wasn't return 1, if it wasn't and == r then restart program.
def input_check_for_int_or_restart(data):
	if data == 0:
		data = 1
		return data
	elif data == "r":
		program()
	elif data == "":
		data = 1
		return data
	else:
		return data


# Main functions
def input_func(text):
	try:
		a = int(input_check_for_int_or_restart(input(f"{text}")))
		return a
	except ValueError:
		print(number_error)
		input_func(text)


def program():
	print(
		'''\n***Assessment calculator***\nThis calculator will first calculate waist and hip ratio.\nThen it will calculate the Tri-level bike test.\n Enter "R" to restart the caculator at any step after gender. Press "enter" to skip step ***warning*** this may break calculations.''')
	gender = input("is the client male or female? Type M or F: ").lower()
	if gender == "m" or gender == "f":
		age = input_func(client["age"])
		print(age)
		weight = input_func(client["weight"])
		print(weight)
		print("\nWaist Measurement = Women - Smallest part of waist. Men - Inline with belly button.")
		waist = input_func(client["waist"])
		print(waist)
		print("\nHip measure = inline with greater trochanter on both sides.")
		hip = input_func(client["hip"])
		print(hip)

		# maths
		waist_hip = round(waist / hip, 2)
		thr = round((220 - age) * 0.75, 2)

		waist_hip_func(gender, waist_hip, waist)

		print(f"\nThe target heart rate for the Tri-level bike test is: ***{thr}***")

		second_last_watt = int(input("What was the SECOND last Watt/Power: "))
		second_last_hr = int(input("What was the SECOND last heart rate: "))
		final_hr = int(input("What was the LAST last heart rate: "))
		# maths 2
		power_at_thr = second_last_watt + (25 * ((thr - second_last_hr) / (final_hr - second_last_hr)))
		watts_per_kg = round(power_at_thr / weight, 2)

		trilevel_results(age, gender, watts_per_kg)
	else:
		print("There has been an input error in the 'gender step' Value must be 'M' or 'F'. Please start again.")


while replay:
	program()


