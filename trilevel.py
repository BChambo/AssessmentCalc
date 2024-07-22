NORMATIVE_DATA = {
    (16, 34): {
        "m": [3.5, 2.9, 2.4, 1.8, 1.1],
        "f": [3.2, 2.7, 2.2, 1.6, 1.0],
    },
    (35, 44): {
        "m": [3.3, 2.9, 2.3, 1.7, 1.0],
        "f": [3.0, 2.6, 2.0, 1.5, 0.9],
    },
    (45, 54): {
        "m": [3.2, 2.8, 2.2, 1.7, 1.0],
        "f": [2.8, 2.4, 1.9, 1.5, 0.9],
    },
    (55, 120): {
        "m": [2.9, 2.5, 1.9, 1,4, 0.9],
        "f": [2.6, 2.2, 1.8, 1.4, 0.8],
    },
}

def trilevel_results(age, gender, watts_per_kg):
    age_range = ()
    performance = ""

    if 120 < age < 15:
        print("***ERROR*** AGE OUT OF RANGE")
        trilevel_results(age, gender, watts_per_kg)
    elif age > 54:
        age_range = (55, 120)
    elif age > 44:
        age_range = (45, 54)
    elif age > 34:
        age_range = (35, 44)
    else:
        age_range = (16, 34)

    if watts_per_kg > NORMATIVE_DATA[age_range][gender][0]:
        performance = "excellent"
    elif watts_per_kg >= NORMATIVE_DATA[age_range][gender][1]:
        performance = "very good"
    elif watts_per_kg >= NORMATIVE_DATA[age_range][gender][2]:
        performance = "good"
    elif watts_per_kg >= NORMATIVE_DATA[age_range][gender][3]:
        performance = "average"
    elif watts_per_kg >= NORMATIVE_DATA[age_range][gender][4]:
        performance = "fair"
    else:
        performance = "poor"

    print(f"\nThe client scored: ***{watts_per_kg}***\nWhich is ***{performance}*** for their age.")




