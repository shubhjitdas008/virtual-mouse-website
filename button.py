import tkinter as tk
import subprocess
import os
import signal

# Global variable to store the process
process = None

def run_script():
    global process
    if process is None:  # Start only if no process is running
        process = subprocess.Popen(["python", "gesture.py"])  # Replace with your script name

def stop_script():
    global process
    if process is not None:
        os.kill(process.pid, signal.SIGTERM)  # Kill the process
        process = None  # Reset process variable

# Create GUI window
root = tk.Tk()
root.title("Run/Stop Python Script")

# Run button
run_button = tk.Button(root, text="Run Script", command=run_script, font=("Arial", 14), padx=20, pady=10)
run_button.pack(pady=10)

# Stop button
stop_button = tk.Button(root, text="Stop Script", command=stop_script, font=("Arial", 14), padx=20, pady=10)
stop_button.pack(pady=10)

# Run GUI loop
root.mainloop()