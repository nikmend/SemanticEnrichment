# Readme File: Word Embeddings Project

## Introduction

This project is focused on creating a methodology to add new words to existing semantic domains created from the Spanish Billion Words Corpus and Embeddings Cardellino and other sources. The goal is to create vector representations for these new words from scratch, as they are likely to be infrequent in the corpus. Additionally, we aim to provide an index of membership for these new words to the existing domains and evaluate it. Furthermore, this project allows generating a classification of collocation of terms and evaluating it.

## Requirements

This project is developed in Python, and it requires the following packages:

* NumPy
* Pandas
* Scikit-learn
* Gensim

You can install all the necessary packages using the following command:

```
pip install -r requirements.txt
```

## Usage

The project includes the following files:

* `main.py`: the main script that executes the methodology to add new words to the semantic domains, generates the classification of collocation of terms, and evaluates it.
* `embeddings.py`: the script that contains the methods to create vector representations for new words from scratch.
* `collocation.py`: the script that contains the methods to generate the classification of collocation of terms.
* `data/`: a folder that contains the Spanish Billion Words Corpus and Embeddings Cardellino.
* `output/`: a folder that contains the results of the project.

To run the project, you can execute the `main.py` script:

```
python main.py
```

## Results

The project generates two main outputs:

* `membership_index.csv`: a file that contains the index of membership for the new words to the existing semantic domains.
* `collocation_classification.csv`: a file that contains the classification of collocation of terms.

## Conclusion

This project provides a methodology to add new words to existing semantic domains created from the Spanish Billion Words Corpus and Embeddings Cardellino and other sources. The generated vector representations for new words from scratch and the index of membership for these new words to the existing domains are valuable resources for further research. Additionally, the classification of collocation of terms provides insight into the relationships between different terms in the corpus.