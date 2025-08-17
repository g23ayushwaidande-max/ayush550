from pymongo import MongoClient

# connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["schoolDB"]
collection = db["students"]

print("✅ Connected to MongoDB!")
import tkinter as tk
from tkinter import messagebox

# GUI window
root = tk.Tk()
root.title("School Management - CRUD App")
root.geometry("500x450")

# Labels & Entry boxes
tk.Label(root, text="Roll No").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Grade").pack()
grade_entry = tk.Entry(root)
grade_entry.pack()

tk.Label(root, text="Passed (yes/no)").pack()
passed_entry = tk.Entry(root)
passed_entry.pack()
# CREATE
def add_student():
    roll_no = roll_entry.get()
    name = name_entry.get()
    age = int(age_entry.get())
    grade = grade_entry.get()
    passed = True if passed_entry.get().lower() == "yes" else False

    collection.insert_one({
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "grade": grade,
        "passed": passed
    })
    messagebox.showinfo("Success", "Student Added!")

# READ
def view_students():
    students = collection.find()
    data = ""
    for s in students:
        data += f"Roll: {s['roll_no']} | {s['name']} | Age: {s['age']} | Grade: {s['grade']} | Passed: {s['passed']}\n"
    messagebox.showinfo("Students", data if data else "No students found")

# UPDATE
def update_student():
    roll_no = roll_entry.get()
    new_grade = grade_entry.get()
    collection.update_one({"roll_no": roll_no}, {"$set": {"grade": new_grade}})
    messagebox.showinfo("Updated", "Grade Updated!")

# DELETE
def delete_student():
    roll_no = roll_entry.get()
    collection.delete_one({"roll_no": roll_no})
    messagebox.showinfo("Deleted", "Student Deleted!")
tk.Button(root, text="Add Student", command=add_student).pack(pady=5)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)
tk.Button(root, text="Update Student", command=update_student).pack(pady=5)
tk.Button(root, text="Delete Student", command=delete_student).pack(pady=5)

root.mainloop()