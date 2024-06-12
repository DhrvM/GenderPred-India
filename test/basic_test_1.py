from genderpred_in import classify_name, get_name, get_first_name, get_male_probability, get_female_probability, get_gender

result = classify_name("Rohit")
print(f"Full Name: {get_name(result)}")
print(f"First Name: {get_first_name(result)}")
print(f"Male Probability: {get_male_probability(result)}")
print(f"Female Probability: {get_female_probability(result)}")
print(f"Gender: {get_gender(result)}")
