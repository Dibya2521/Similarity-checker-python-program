# Similarity-checker-python-program

This repository contains a Python program to identify similar entries within 200 meters of each other in a given dataset. The program uses the geopy and scipy modules, and the Levenshtein distance algorithm to check the similarity of two strings.

Installation
To use this program, you will need to have Python 3 installed on your system. You can download and install Python from the official website: https://www.python.org/downloads/

The program also has the following dependencies:
pandas
geopy
scipy
Levenshtein

You can install these dependencies using pip by running the following command in your terminal:
pip install pandas geopy scipy levenshtein

Usage
To use the program, follow these steps:
Clone this repository to your local machine.
Navigate to the repository directory in your terminal.
Place the input dataset in the repository directory with the name input.csv.
Run the program using the following command:
python main.py
The output will be written to a file named output.csv.
The output file will contain all entries that satisfy the similarity criteria marked as True / 1 in a separate column named is_similar.

Assumptions
The program assumes that the input dataset has the following columns:
latitude: Latitude coordinate in decimal degrees
longitude: Longitude coordinate in decimal degrees
name: Name of the entry as a string
The program also assumes that the entries in the name column are in English and uses the Levenshtein distance algorithm to calculate string similarity. The program uses the cKDTree class from scipy.spatial module to perform fast k-dimensional searches of nearest neighbours.

License
This program is licensed under the MIT License. Feel free to use, modify, and distribute it as you see fit.
