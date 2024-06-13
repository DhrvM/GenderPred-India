import os
import pickle
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppresses INFO and WARNING messages
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dropout, Dense
from tensorflow.keras.models import Sequential
import logging
import re

# Load the tokenizer and label encoder
with open(os.path.join(os.path.dirname(__file__), 'tokenizer.pickle'), 'rb') as handle:
    tokenizer = pickle.load(handle)
with open(os.path.join(os.path.dirname(__file__), 'label_encoder.pickle'), 'rb') as handle:
    label_encoder = pickle.load(handle)

# Define the LSTM model
model = Sequential()
model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=50))
model.add(LSTM(units=128, return_sequences=False))
model.add(Dropout(0.5))
model.add(Dense(units=3, activation='softmax'))
model = load_model(os.path.join(os.path.dirname(__file__), 'gender_prediction_model.h5'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Ensure max_length matches the training configuration
max_length = 21  # Update this to match your training configuration if different

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
        "name": full_name,
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

# Functions to retrieve name, male probability, female probability, and gender
def get_name(result):
    return result["name"]

def get_first_name(result):
    return result["first_name"]

def get_male_probability(result):
    return result["percent_male"]

def get_female_probability(result):
    return result["percent_female"]

def get_gender(result):
    return result["gender"]
