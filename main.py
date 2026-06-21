import tkinter as tk
from tkinter import ttk
import json


window = tk.Tk()

window.title("โปรแกรมบันทึกผลการเรียน")
window.geometry("800x600")

title_label = tk.Label(
    window,
    text="โปรแกรมบันทึกผลการเรียน",
    font=("Kanit", 20)
)

title_label.pack(pady=20)

table = ttk.Treeview(
    window,
    columns=("code", "name", "credit", "grade"),
    show="headings"
)

table.heading("code", text="รหัสวิชา")
table.heading("name", text="ชื่อวิชา")
table.heading("credit", text="หน่วยกิต")
table.heading("grade", text="เกรด")

table.column("code", width=120)
table.column("name", width=450)
table.column("credit", width=100)
table.column("grade", width=100)

with open("course.json", "r", encoding="utf-8") as file:
    subjects = json.load(file)

for subject in subjects:
    table.insert("", tk.END, values=(
            subject["code"],
            subject["name"],
            subject["credit"],
            subject["grade"]
        ))

table.pack(fill="both", expand=True, padx=20, pady=20)

window.mainloop()