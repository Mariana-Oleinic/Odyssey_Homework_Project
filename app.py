import tkinter as tk
from tkinter import font
from data_processing import *
from scraper import extract_movie_data_for_year


root = tk.Tk()
root.title("Popular Movies Checker")
root.eval("tk::PlaceWindow . center")
bold_font = font.Font(weight="bold")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


def on_check():
    """When clicking on "Check" button, this function updates the result_label"""
    year = year_entry.get()
    movies_text_data = extract_movie_data_for_year(year)
    movies_sublists_list = arrange_each_movie_in_sublist(movies_text_data)
    movies_json = arrage_movie_data_in_json_structure(movies_sublists_list)
    save_movies(movies_json) 
    records = load_movies()
    first_six_records = records[:6]
    formatted_json = json.dumps(first_six_records, indent=4, ensure_ascii=False)
    result_label.config(text=formatted_json)


def reset():
    """Clear the offers result label"""
    result_label.config(text="")

label = tk.Label(frame, text="Check popular movie:", font=bold_font)
label.pack(pady=5)

year_label = tk.Label(frame, text="Year:")
year_label.pack()
year_entry = tk.Entry(frame)
year_entry.pack(padx=10)

tk.Button(
    frame,
    text="Check",
    font=("System", 14),
    fg="violet",
    cursor='hand2',
    command=on_check
).pack(pady=5)

tk.Button(
    frame,
    text="Reset",
    font=("System", 14),
    fg="red",
    cursor='hand2',
    command=reset,
).pack()

result_label = tk.Label(frame, text="")
result_label.pack(padx=20, pady=10)

root.mainloop()
