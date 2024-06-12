from genderpred_in import classify_name, get_name, get_first_name, get_male_probability, get_female_probability, get_gender

# Classify the name "Rohit"
result = classify_name("Rohit")

# Retrieve and print the results
full_name = get_name(result)
first_name = get_first_name(result)
male_prob = get_male_probability(result)
female_prob = get_female_probability(result)
gender = get_gender(result)

print(f"Full Name: {full_name}")
print(f"First Name: {first_name}")
print(f"Male Probability: {male_prob}")
print(f"Female Probability: {female_prob}")
print(f"Gender: {gender}")
