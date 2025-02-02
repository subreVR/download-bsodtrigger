import tkinter as tk
import winsound
import time
import threading
import os

# Function to play the waveboi.wav sound
def play_buzzing_sound():
    # Path to the waveboi.wav file (assuming it's in the "Downloads" folder)
    buzzing_sound_path = os.path.expanduser('~') + r'\\Downloads\\waveboi.wav'
    while True:
        # Play the .wav file in a loop
        winsound.PlaySound(buzzing_sound_path, winsound.SND_FILENAME | winsound.SND_LOOP)

# Create the main window
root = tk.Tk()

# Fullscreen mode
root.attributes("-fullscreen", True)
root.config(bg="#1E90FF")  # Light blue background color

# Hide the mouse cursor
root.config(cursor="none")

# BSOD text for Windows 11 (excluding the sad face)
bsod_text = """
Your PC ran into a problem and needs to restart.

We're just collecting some error info, and then we'll restart for you.

Stop Code: CRITICAL_PROCESS_DIED

For more information about this issue and possible fixes, visit:
https://support.microsoft.com
"""

# Create a frame to hold both the sad face and the BSOD message
frame = tk.Frame(root, bg="#1E90FF")
frame.pack(expand=True, anchor="nw", padx=50, pady=50, fill="both")

# Create a label for the larger sad face :( at the top left
label_sad_face = tk.Label(frame, text=":(", font=("Segoe UI", 48), fg="white", bg="#1E90FF")
label_sad_face.pack(side="top", anchor="nw")

# Create a label for the rest of the BSOD text
label_bsod = tk.Label(frame, text=bsod_text, font=("Segoe UI", 18), fg="white", bg="#1E90FF", padx=10, pady=10, anchor="nw", justify="left")
label_bsod.pack(side="top", anchor="nw", pady=10)

# Start the buzzing sound in a separate thread
sound_thread = threading.Thread(target=play_buzzing_sound, daemon=True)
sound_thread.start()

# Close the window with a keypress (Esc key)
root.bind("<Escape>", lambda e: root.quit())

# Start the tkinter event loop
root.mainloop()
