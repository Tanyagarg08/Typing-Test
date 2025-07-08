import tkinter as tk
import random
import time

words = [
    "python", "Gaming", "Specialization","COER","Hostels", "Toxic"
    ,"Tanya Garg","Btech","College","Whatever " ,"Starting ","Learning","Everyone"
    ,"Test","Coding","Java","Typing"
]


score = 0
time_left = 60
current_word = ""
start_time = None

# Update the word display
def next_word():
    global current_word
    current_word = random.choice(words)
    word_label.config(text=current_word)
    entry.delete(0, tk.END)

# Start the game
def start_game(event=None):
    global start_time
    if start_time is None:
        start_time = time.time()
        countdown()
    check_word()

# Check the entered word
def check_word():
    global score
    typed = entry.get().strip()
    if typed == current_word:
        score += 1
        score_label.config(text=f"Score: {score}")
    next_word()

# Countdown timer
def countdown():
    global time_left
    if time_left > 0:
        time_left_display.config(text=f"Time: {time_left}s")
        time_left -= 1
        root.after(1000, countdown)
    else:
        word_label.config(text="Time's up!")
        entry.config(state='disabled')
        result_label.config(text=f"Your WPM: {score}")

# GUI 
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("400x300")
root.resizable(False, False)

# Widgets
instructions = tk.Label(root, text="Type the word below and press Space or Enter", font=("Arial", 12))
instructions.pack(pady=10)

word_label = tk.Label(root, text="", font=("Helvetica", 24), fg="blue")
word_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 16))
entry.pack()
entry.focus_set()

score_label = tk.Label(root, text="Score: 0", font=("Arial", 12))
score_label.pack(pady=5)

time_left_display = tk.Label(root, text="Time: 60s", font=("Arial", 12))
time_left_display.pack()

result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
result_label.pack(pady=10)

# Bind keys
root.bind('<space>', start_game)
root.bind('<Return>', start_game)

# Start with the first word
next_word()

# Run the app
root.mainloop()
