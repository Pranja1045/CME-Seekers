import tkinter as tk
from tkinter import ttk


def fetch_data():
    selected_year = int(date_entry.get())

    column_frequency = {}

    file_path = ''  # define the path

    with open(file_path, 'r') as file:
        for line in file:

            columns = line.strip().split()

            if columns:
                first_column = columns[0]

                column_frequency[first_column] = column_frequency.get(first_column, 0) + 1

    listbox.delete(0, tk.END)

    for item_text, item_value in column_frequency.items():
        if int(item_text) == selected_year:
            listbox.insert(tk.END, f"Year: {item_text}")
            listbox.insert(tk.END, f"No. of magnetic reconnections: {item_value}")


root = tk.Tk()
root.title("Magnetic Reconnection Frequency")

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

date_label = ttk.Label(frame, text="Enter Year:")
date_label.grid(row=0, column=0, padx=5, pady=5)

date_entry = ttk.Entry(frame)
date_entry.insert(0, 'data year range 2000-2019')
date_entry.grid(row=0, column=1, padx=5, pady=5)

fetch_button = ttk.Button(frame, text="Fetch Data", command=fetch_data)
fetch_button.grid(row=0, column=2, padx=5, pady=5)

listbox = tk.Listbox(frame)
listbox.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
