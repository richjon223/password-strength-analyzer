import tkinter as tk
import pyttsx3
import random
import string
import threading

# ---------- TTS ----------

def speak(text):
    threading.Thread(target=_speak, args=(text,), daemon=True).start()

def _speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# ---------- Password Strength Checker ----------

def check_strength():

    password = entry.get()

    if len(password) > 40:
        result_label.config(text="Like you will remember this...", fg="blue")
        speak("Like you will remember this")
        return

    score = 0
    missing = []

    if len(password) >= 8:
        score += 1
    else:
        missing.append("At least 8 characters")

    if any(c.islower() for c in password):
        score += 1
    else:
        missing.append("Add a lowercase letter")

    if any(c.isupper() for c in password):
        score += 1
    else:
        missing.append("Add an uppercase letter")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        missing.append("Add a number")

    if any(c in "!@#$%^&*()_+-=[]{}|;:',.<>?/" for c in password):
        score += 1
    else:
        missing.append("Add a special character")

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    message = f"Password Strength: {strength}"

    if missing:
        message += "\n\nMissing:\n• " + "\n• ".join(missing)

    result_label.config(text=message, fg=color)

    speak(f"Password strength is {strength}")


# ---------- Password Generator ----------

def generate_password():

    length = 12

    characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*"
    )

    password = ''.join(random.choice(characters) for i in range(length))

    entry.delete(0, tk.END)
    entry.insert(0, password)


# ---------- Show / Hide Password ----------

def toggle_password():

    if show_password_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")


# ---------- GUI ----------

window = tk.Tk()
window.title("Password Strength Analyzer")
window.geometry("420x300")
window.configure(bg="#2c3e50")


title = tk.Label(
    window,
    text="Password Strength Analyzer",
    font=("Arial", 16, "bold"),
    bg="#2c3e50",
    fg="white"
)
title.pack(pady=10)


# Password Entry

entry = tk.Entry(window, width=30, show="*", font=("Arial", 12))
entry.pack(pady=10)


# Show password checkbox

show_password_var = tk.BooleanVar()

show_checkbox = tk.Checkbutton(
    window,
    text="Show Password",
    variable=show_password_var,
    command=toggle_password,
    bg="#2c3e50",
    fg="white",
    selectcolor="#2c3e50"
)

show_checkbox.pack()


# Buttons

button_frame = tk.Frame(window, bg="#2c3e50")
button_frame.pack(pady=10)


check_button = tk.Button(
    button_frame,
    text="Check Strength",
    command=check_strength,
    width=15
)
check_button.grid(row=0, column=0, padx=5)


generate_button = tk.Button(
    button_frame,
    text="Generate Password",
    command=generate_password,
    width=15
)
generate_button.grid(row=0, column=1, padx=5)


# Result Label

result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="#2c3e50",
    fg="white",
    justify="left"
)
result_label.pack(pady=15)


window.mainloop()