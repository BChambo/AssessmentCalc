def trilevel_results(age, gender, watts_per_kg):
	if age > 14 and age <= 34:
		if gender == "m":
			if watts_per_kg > 3.5:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 2.4:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.8:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 1.1:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")
		elif gender == "f":
			if watts_per_kg > 3.2:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.7:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 2.2:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.6:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 1:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")


	elif age >= 35 and age <= 44:
		if gender == "m":
			if watts_per_kg > 3.3:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 2.3:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.7:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 1:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")
		elif gender == "f":
			if watts_per_kg > 3:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.6:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 2:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.5:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 0.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")


	elif age >= 45 and age <= 54:
		if gender == "m":
			if watts_per_kg > 3.2:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.8:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 2.2:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.7:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 1:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")
		elif gender == "f":
			if watts_per_kg > 2.8:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.4:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 1.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.5:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 0.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")


	else:
		if gender == "m":
			if watts_per_kg > 2.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.5:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 1.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.4:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 0.9:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")
		elif gender == "f":
			if watts_per_kg > 2.6:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Elite*** for their age.")
			elif watts_per_kg > 2.2:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Excellent*** for their age.")
			elif watts_per_kg > 1.8:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Very Good*** for their age.")
			elif watts_per_kg > 1.4:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Average*** for their age.")
			elif watts_per_kg > 0.8:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Fair*** for their age.")
			else:
				print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***Poor*** for their age.")

