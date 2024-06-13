from setuptools import setup, find_packages
import os
import codecs

VERSION = '1.0.2'
DESCRIPTION = 'A Package to Predict the Gender of a Person based on their Name (Suited for Indian Names)'
# Read the contents of your README file
with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="genderpred_in",
    version=VERSION,
    author="Dhruv Malpani",
    author_email="dhruv.malpani2005@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url="https://github.com/DhrvM/GenderPred-India",  # Update with your GitHub repository
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'tensorflow', 'keras', 'scikit-learn'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='gender, indian, names, LSTM, tensorflow, keras, classify, prediction',
    python_requires='>=3.10',
    include_package_data=True,
    package_data={
        'genderpred_in': ['tokenizer.pickle', 'label_encoder.pickle', 'gender_prediction_model.h5'],
    },
)
