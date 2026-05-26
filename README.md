# Phishing Email Detection

## Overview
This project is a Machine Learning-based Phishing Email Detection system built using Python and Scikit-learn. The model analyzes email content and identifies whether an email is **Phishing** or **Safe** based on textual patterns and suspicious indicators like URLs and keywords.

## Features
- Train on phishing and legitimate email datasets
- Extract email text and URL-based features
- Classify emails as Phishing or Safe
- Display prediction accuracy
- Generate confusion matrix visualization
- Allow users to test custom email inputs

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Regular Expressions (re)

## Project Structure

Phishing_Email_Detection/
│
├── phishing_detection.py
├── emails.csv
├── requirements.txt
└── README.md


## Installation

Install dependencies:

pip install -r requirements.txt

Run the project:

python phishing_detection.py

## Dataset
The dataset contains two categories:

- Phishing emails
- Safe/Legitimate emails

Examples include suspicious messages containing urgent requests, fake rewards, login links, and normal communication emails.

## Model Workflow
1. Load email dataset  
2. Extract features from email text  
3. Convert text using TF-IDF Vectorization  
4. Train model using Multinomial Naive Bayes  
5. Predict phishing or safe emails  
6. Evaluate using accuracy and confusion matrix

## Example Output

Input:
Urgent! Click http://verify-account.com

Output:
⚠ Phishing Email Detected

Input:
Team meeting scheduled tomorrow at 2 PM

Output:
✓ Safe Email

## Expected Outcome
The system successfully classifies emails as Phishing or Safe with good accuracy based on textual content and suspicious URL patterns.
