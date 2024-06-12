import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dropout, Dense
from tensorflow.keras.models import Sequential
import logging
import re

# Load the tokenizer and label encoder
with open('genderpred_in/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)
with open('genderpred_in/label_encoder.pickle', 'rb') as handle:
    label_encoder = pickle.load(handle)

# Define the LSTM model
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=50))
model.add(LSTM(units=128, return_sequences=False))
model.add(Dropout(0.5))
model.add(Dense(units=3, activation='softmax'))
model = load_model('genderpred_in/gender_prediction_model.h5')
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Ensure max_length matches the training configuration
max_length = 21 

# Classification Function
def classify_name(full_name):
    # Tokenize and pad the input name
    name = clean_name(full_name)
    sequence = tokenizer.texts_to_sequences([name])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding='post')

    # Predict the probabilities
    probabilities = model.predict(padded_sequence)[0]
    
    # Log the probabilities for debugging
    logging.debug(f'Probabilities: {probabilities}')
    
    # Get the class probabilities
    male_index = label_encoder.transform(['m'])[0]
    female_index = label_encoder.transform(['f'])[0]
    male_prob = float(probabilities[male_index])
    female_prob = float(probabilities[female_index])

    # Log the male and female probabilities
    logging.debug(f'Male Probability: {male_prob}')
    logging.debug(f'Female Probability: {female_prob}')
    
    # Apply the threshold logic
    if male_prob > 0.85:
        predicted_gender = 'male'
    elif female_prob > 0.85:
        predicted_gender = 'female'
    else:
        predicted_gender = 'unknown'

    return {
        "name" : full_name,
        "first_name": name,
        "gender": predicted_gender,
        "percent_male": male_prob,
        "percent_female": female_prob
    }

def clean_name(name):
    # Take the first word from the name
    name = name.split()[0]
    # Remove non-alphabetic characters
    name = re.sub('[^a-zA-Z]', '', name)
    # Remove non-printable characters and keep ASCII characters
    name = ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in name])
    # Convert name to uppercase
    name = name.upper()
    # Strip leading and trailing whitespace
    name = name.strip()
    return name
