Password Strength Analyzer

A simple desktop application that analyzes password strength and provides feedback on how to improve it. The program also includes password generation and voice feedback to inform the user about the password strength.

Built with Python using Tkinter for the graphical interface and pyttsx3 for text-to-speech functionality.

Features

Password strength analysis (Weak / Medium / Strong)

Shows missing requirements needed to improve password strength

Password generator for creating secure passwords

Text-to-Speech feedback when checking password strength

Show / Hide password checkbox

Simple and clean graphical interface

Password Strength Criteria

The application evaluates passwords based on the following rules:

Minimum 8 characters

Contains lowercase letters

Contains uppercase letters

Contains numbers

Contains special characters

The application will display only the missing requirements so users know how to strengthen their password.

Example feedback:

Password Strength: Medium

Missing:

Add a special character

Technologies Used

Python

Tkinter

pyttsx3

threading

random

string

Installation

Clone the repository

git clone https://github.com/richjon223/password-strength-analyzer.git

Navigate to the project folder

cd password-strength-analyzer

Install the required dependency

pip install pyttsx3

Run the program

python password_checker.py
How to Use

Enter a password into the input field

Click Check Strength

The program will:

Display the password strength

Show what criteria are missing

Speak the result using text-to-speech

You can also:

Click Generate Password to create a random secure password

Enable Show Password to reveal the typed password

Example

Input:

Hello123

Output:

Password Strength: Medium

Missing:

Add a special character

Future Improvements

Possible features that can be added:

Password entropy calculation

Password crack-time estimation

Detection of common weak passwords

Copy password button

Modern UI styling

Web-based version of the application

Author

Richard Jonathan