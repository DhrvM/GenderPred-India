
# GenderPred-IN
GenderPred-IN is a Python package designed to predict the gender of a person based on their name. It is specifically tailored for Indian names, leveraging advanced machine learning techniques to provide accurate predictions.
[PyPI](https://pypi.org/project/genderpred-in)

### Features
- LSTM Model: Utilizes a Long Short-Term Memory (LSTM) neural network model to understand the sequential patterns in names.
- Tokenizer and Label Encoder: Processes names through a trained tokenizer and label encoder to convert names into a format suitable for the LSTM model.
- Pre-trained Model: Comes with a pre-trained model, eliminating the need for extensive training and setup.
- User-friendly: Simple and easy-to-use functions to get predictions with minimal setup.


## Getting Started
### Installation
**You can install the package using pip (easy-peasy way):**
```bash
pip  install  genderpred_in
```
**or you can use **github** to install (harder way):**

 1. Clone the repository:
 ```bash
 git clone https://github.com/DhrvM/GenderPred-India.git
cd GenderPred-India
 ```
 3. Install the package:
 ```bash
 pip install .
```
 5. Verify the installation:
 ```bash
 pip show genderpred_in
 ```

### Usage

**Import Package**
```python
from genderpred_in import classify_name, get_name, get_first_name, get_male_probability, get_female_probability, get_gender
```
**Here is an example of how to use the package:**
```python
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
```

### Example Output:

```bash
Full Name: Rohit
First Name: ROHIT
Male Probability: 0.9916077852249146
Female Probability: 0.008392222225666046
Gender: male
```

### Functions
-   `classify_name(full_name)`: Classifies the given full name and returns a dictionary with the name, first name, gender, and probabilities.
-   `get_name(result)`: Retrieves the full name from the classification result.
-   `get_first_name(result)`: Retrieves the first name from the classification result.
-   `get_male_probability(result)`: Retrieves the male probability from the classification result.
-   `get_female_probability(result)`: Retrieves the female probability from the classification result.
-   `get_gender(result)`: Retrieves the predicted gender from the classification result. (Output: *male, female, unknown*)

## Versions
`Version 1.0.2` Fixed Model loading error for Windows.\
`Version 1.0.1` Uses LSTM model with a tokenized First-Name to Generate Predictions of Gender.


## Built With

-   [TensorFlow](https://www.tensorflow.org/) - The machine learning framework used
-   [Keras](https://keras.io/) - High-level neural networks API
-   [NumPy](https://numpy.org/) - Used for numerical computing
-   [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis

## Authors
**Dhruv Malpani** - Initial Work
[LinkedIn](https://www.linkedin.com/in/dhruv-malpani/)
[GitHub](https://github.com/DhrvM)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments
[**Praneeth Vasarla**](https://medium.com/@praneethvaasarla)
Your article helped me create the initial model using Logistic Regression and n-grams. ([article](https://medium.com/@praneethvaasarla/how-i-used-nlp-to-predict-the-gender-for-indian-names-df0ae30c275b))
