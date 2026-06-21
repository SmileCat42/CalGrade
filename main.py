import tkinter as tk
from tkinter import ttk
import json


def update_grade():

    selected_item = table.selection()

    if not selected_item:
        return

    table.set(
        selected_item[0],
        "grade",
        grade_var.get()
    )

def on_select(event):
    grade_combo.set("กรุณาเลือกเกรด")
    selected_item = table.selection()

    if not selected_item:
        return

    values = table.item(selected_item[0], "values")

    code = values[0]
    name = values[1]

    selected_subject_label.config(
        text=f"วิชาที่เลือก: {code} {name}"
    )

    grade_combo.config(state="readonly")


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

grade_var = tk.StringVar()

grade_combo = ttk.Combobox(
    window,
    textvariable=grade_var,
    values=["", "A", "B+", "B", "C+", "C", "D+", "D", "F"],
    state="readonly"
)

grade_combo.set("กรุณาคลิกเลือกวิชา")

update_button = tk.Button(
    window,
    text="อัปเดตเกรด"
)

update_button = tk.Button(
    window,
    text="อัปเดตเกรด",
    command=update_grade
)

selected_subject_label = tk.Label(
    window,
    text="ยังไม่ได้เลือกวิชา",
    font=("Arial", 11)
)

table.bind("<<TreeviewSelect>>", on_select)


grade_combo.pack(pady=5)
grade_combo.config(state="disabled") 

selected_subject_label.pack()

update_button.pack(pady=5)

table.pack(fill="both", expand=True, padx=20, pady=20)

window.mainloop()