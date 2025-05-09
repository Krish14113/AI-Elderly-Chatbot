import tkinter as tk
from tkinter import scrolledtext, ttk
from PIL import Image, ImageTk
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-2.0-flash')

conversation_history = []

settings = {
    "font_size": 14,
    "bg_color": "#e0f2f7"
}

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return "I'm having trouble responding right now. Please try again later."

def send_message():
    user_input = user_input_entry.get()
    user_input_entry.delete(0, tk.END)

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\n")

    history_text = "\n".join(
        [f"{msg['role']}: {msg['text']}" for msg in conversation_history]
    )

    prompt = f"""
    You are a compassionate and patient companion for elderly people. Respond to the following with empathy and understanding. Avoid medical or financial advice.
    Previous conversation:
    {history_text}

    User: {user_input}
    """

    response = get_gemini_response(prompt)
    chat_log.insert(tk.END, f"Chatbot: {response}\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.see(tk.END)

    conversation_history.append({"role": "user", "text": user_input})
    conversation_history.append({"role": "chatbot", "text": response})

def open_settings():
    settings_window = tk.Toplevel(root)
    settings_window.title("Settings")

    # Font Size
    tk.Label(settings_window, text="Font Size:").grid(row=0, column=0, padx=5, pady=5)
    font_size_var = tk.IntVar(value=settings["font_size"])
    font_size_spinbox = tk.Spinbox(settings_window, from_=10, to=20, textvariable=font_size_var)
    font_size_spinbox.grid(row=0, column=1, padx=5, pady=5)

    # Background Color
    tk.Label(settings_window, text="Background Color:").grid(row=1, column=0, padx=5, pady=5)
    bg_color_var = tk.StringVar(value=settings["bg_color"])
    bg_color_entry = tk.Entry(settings_window, textvariable=bg_color_var)
    bg_color_entry.grid(row=1, column=1, padx=5, pady=5)

    def apply_settings():
        settings["font_size"] = font_size_var.get()
        settings["bg_color"] = bg_color_var.get()
        root.configure(bg=settings["bg_color"])
        chat_log.configure(font=("Arial", settings["font_size"]), bg="white")
        input_label.configure(bg=settings["bg_color"], font=("Arial", settings["font_size"]))
        input_frame.configure(bg=settings["bg_color"])
        if send_button_image:
            send_button.configure(bg=settings["bg_color"])
        else:
            send_button.configure(bg=settings["bg_color"], font=("Arial", settings["font_size"]))
        title_label.configure(bg=settings["bg_color"], font=("Arial", 18, "bold"))

    tk.Button(settings_window, text="Apply", command=apply_settings).grid(row=2, column=0, columnspan=2, pady=10)

root = tk.Tk()
root.title("Elderly Chatbot")

style = ttk.Style()
style.theme_use('clam')

root.configure(bg=settings["bg_color"])
title_label = tk.Label(root, text="Elderly Companion", font=("Arial", 18, "bold"), bg=settings["bg_color"])
title_label.pack(pady=(10, 5))

chat_log = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", settings["font_size"]), bg="white")
chat_log.pack(padx=20, pady=(0, 10), fill=tk.BOTH, expand=True)

input_frame = tk.Frame(root, bg=settings["bg_color"])
input_frame.pack(padx=20, pady=(0, 10), fill=tk.X)

input_label = tk.Label(input_frame, text="Enter your message:", font=("Arial", settings["font_size"]), bg=settings["bg_color"])
input_label.pack(side=tk.LEFT)

user_input_entry = tk.Entry(input_frame, font=("Arial", settings["font_size"]))
user_input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

send_button_image = None
try:
    send_image = Image.open("send_icon.png")
    send_image = send_image.resize((30, 30), Image.LANCZOS)
    send_icon = ImageTk.PhotoImage(send_image)
    send_button = tk.Button(input_frame, image=send_icon, command=send_message, bg=settings["bg_color"])
    send_button.image = send_icon
    send_button_image = True
    send_button.pack(side=tk.RIGHT)
except FileNotFoundError:
    send_button = tk.Button(input_frame, text="Send", command=send_message, font=("Arial", settings["font_size"]), bg=settings["bg_color"])
    send_button_image = False
    send_button.pack(side=tk.RIGHT)

user_input_entry.bind("<Return>", lambda event=None: send_button.invoke())

settings_button = tk.Button(root, text="Settings", command=open_settings)
settings_button.pack(pady=5)

root.mainloop()