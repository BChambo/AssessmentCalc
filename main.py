from trilevel import *
from waist_hip import *
from art import logo3
replay = True


print(logo3)
while replay:
	print('''***Assessment calculator***\nThis calculator will first calculate waist and hip ratio.\nThen it will calculate the Tri-level bike test.''')
	gender = input("is the client male or female? Type M or F: ").lower()
	if gender == "m" or gender == "f":
		age = int(input("What is the clients age?: "))
		weight = float(input("What is the clients weight?: "))
		print("\nWaist Measurement = Women - Smallest part of waist. Men - Inline with belly button.")
		waist = int(input("What is the clients waist measurement in cm?: "))
		print("\nHip measure = inline with greater trochanter on both sides.")
		hip = int(input("What is the clients hip measurement in cm?: "))

		# maths
		waistHip = round(waist / hip, 2)
		THR = round((220 - age) * 0.75, 2)

		waist_hip_func(gender, waistHip, waist)

		print(f"\nThe target heart rate for the Tri-level bike test is: ***{THR}***")

		second_last_watt = int(input("What was the SECOND last Watt/Power: "))
		second_last_HR = int(input("What was the SECOND last heart rate: "))
		final_HR = int(input("What was the LAST last heart rate: "))
		# maths 2
		power_at_THR = second_last_watt + (25 * ((THR - second_last_HR) / (final_HR - second_last_HR)))
		watts_per_kg = round(power_at_THR / weight, 2)

		trilevel_results(age, gender, watts_per_kg)
	else:
		print("There has been an input error in the 'gender step' Value must be 'M' or 'F'. Please start again.")
	replay_answer = input("\nType 'Y' to start calculator again or any input to exit").lower()
	if replay_answer != "y":
		replay = False
		print("Goodbye\n\n\n")





# ##TESTING CODE###
# gender = "f"
# watts_per_kg = 2
# age = 27
#
# for i in range(0,4):
# 	age += 10
# 	print(trilevel_results(age, gender, watts_per_kg))
#
# for i in range(0, 4):
# 	watts_per_kg += 0.4
# 	print(trilevel_results(age, gender, watts_per_kg))

