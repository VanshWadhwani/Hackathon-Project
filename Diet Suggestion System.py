
import tkinter as tk
from tkinter import messagebox

def get_diet_plan():
    name = name_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    height = height_entry.get()
    health_status = health_status_var.get()

    if not (name and age and weight and height):
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    diet_plan = generate_diet_plan(health_status)
    result_label.config(text=diet_plan)

def generate_diet_plan(health_status):
    if health_status == "Underweight":
        return (
            "Breakfast: Oatmeal with milk, nuts, and fruits.\n"
            "Snack: Greek yogurt with honey and granola.\n"
            "Lunch: Grilled chicken or tofu with rice.\n"
            "Snack: Smoothie with yogurt and protein powder.\n"
            "Dinner: Salmon or lentil stew with vegetables.\n"
            "Snack: Cottage cheese with pineapple or mixed nuts."
        )
    elif health_status == "Healthy":
        return (
            "Breakfast: Whole-grain cereal with low-fat milk and a banana, orange juice.\n"
            "Snack: A handful of mixed nuts.\n"
            "Lunch: Grilled chicken or tofu wrap with mixed vegetables, fresh fruit.\n"
            "Snack: Sliced cucumber and bell peppers with hummus.\n"
            "Dinner: Baked fish or chicken with quinoa and steamed asparagus, side salad.\n"
            "Snack: Greek yogurt with honey and berries."
        )
    elif health_status == "Overweight":
        return (
            "Breakfast: Scrambled eggs with spinach and tomatoes, whole-grain toast.\n"
            "Snack: A piece of fruit.\n"
            "Lunch: Grilled chicken or tofu salad with mixed greens.\n"
            "Snack: Carrot sticks with hummus.\n"
            "Dinner: Baked salmon or chicken with steamed broccoli and quinoa.\n"
            "Snack: Greek yogurt with berries."
        )

# Initialize Tkinter window
root = tk.Tk()
root.title("Diet Recommendation System")

# Create and place labels and entry widgets for user input
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Weight (kg):").grid(row=2, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Height (cm):").grid(row=3, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Health Status:").grid(row=4, column=0, padx=10, pady=5)
health_status_var = tk.StringVar()
health_status_var.set("Healthy")
health_status_menu = tk.OptionMenu(root, health_status_var, "Underweight", "Healthy", "Overweight")
health_status_menu.grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Get Diet Plan", command=get_diet_plan).grid(row=5, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", wraplength=300)
result_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()