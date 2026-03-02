🔐 Password Strength Analyzer

A simple desktop application that evaluates password strength and helps users create more secure passwords.

The application analyzes passwords based on security criteria and provides feedback on what is missing to improve the password.

Built using Python with a graphical interface powered by Tkinter and voice feedback using pyttsx3.

✨ Features

✅ Password strength classification

Weak

Medium

Strong

✅ Displays missing requirements needed to improve the password

✅ Password generator for creating secure passwords

✅ Voice feedback (Text-to-Speech) when checking password strength

✅ Show / Hide password toggle

✅ Clean and simple desktop interface

🧠 How Password Strength Is Calculated

The password is evaluated using the following criteria:

Requirement	Description
Length	At least 8 characters
Lowercase	Contains a–z
Uppercase	Contains A–Z
Numbers	Contains 0–9
Special Characters	Contains symbols like ! @ # $ %

The program will only display the requirements that are missing, helping users understand how to strengthen their password.

📋 Example Output
Input
Hello123
Output
Password Strength: Medium

Missing:
• Add a special character
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/password-strength-analyzer.git
2️⃣ Navigate into the folder
cd password-strength-analyzer
3️⃣ Install dependencies
pip install pyttsx3
4️⃣ Run the program
python password_checker.py
🖥️ How To Use

Enter a password into the input field

Click Check Strength

The program will:

Display the password strength

Show missing criteria

Speak the result using text-to-speech

Optional actions:

Click Generate Password to create a random secure password

Enable Show Password to reveal the typed password

🛠️ Technologies Used

Python

Tkinter

pyttsx3

threading

random

string

🚀 Future Improvements

Possible features for future development:

Password entropy calculation

Password crack-time estimation

Detection of common weak passwords

Copy password button

Modern UI styling

Web-based version

👤 Author

Richard Jonathan

⭐ If you like this project

Feel free to star the repository and use it as a reference for learning about password security and Python GUI applications.
