def waist_hip_func(gender, waistHip, waist):
    # waist to hip responses
    risk1 = "increased risk of cardiovascular disease."
    risk2 = "significantly increased risk of cardiovascular disease."
    risk0 = "Client has no increased risk of cardiovascular disease."
    result = f"The clients waist to hip ratio is: ***{waistHip}*** "

    if gender == "m":
        if waist >= 94 and waist <= 101:
            print("\n" + result + "\n" + risk1 + " Because waist measurement is greater than 94cm")
        elif waist > 102:
            print("\n" + result + "\n" + risk2 + " Because waist measurement is greater than 102cm")
        elif waistHip < 0.90:
            print("\n" + result + "\n" + risk0)
        elif waistHip >= 0.90 and waistHip < 0.95:
            print("\n" + result + "\n" + risk1)
        else:
            print("\n" + result + "\n" + risk2)

    if gender == "f":
        if waist >= 80 and waist <= 87:
            print("\n" + result + "\n" + risk1 + " Because waist measurement is greater than 80cm")
        elif waist > 88:
            print("\n" + result + "\n" + risk2 + " Because waist measurement is greater than 88cm")
        elif waistHip < 0.80:
            print("\n" + result + "\n" + risk0)
        elif waistHip > 0.80 and waistHip < 0.85:
            print("\n" + result + "\n" + risk1)
        else:
            print("\n" + result + "\n" + risk2)
