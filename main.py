from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.geometry("200x200")
window.resizable(False, False)


def calculate_bmi_category(bmi):
    bmi_categories = {
        bmi < 18.5: "Zayıf",
        18.5 <= bmi < 24.9: "Normal Kilolu",
        25 <= bmi < 29.9: "Fazla Kilolu",
        bmi >= 30: "Obezite"
    }
    return bmi_categories[True]

def calBMI(weight, height):
    w = float(weight)
    h = float(height)*0.01
    bmi = w / pow(h,2)
    bmi = round(bmi, 1)

    print("bmi:", bmi)
    label = Label(window, text="Vücut Kitle Endeksiniz:" + str(bmi), font=("Arial", 9))
    window.update_idletasks()  # Add this line
    x_pos = 20
    print(x_pos)
    label.place(x=x_pos, y=150)
    cat = calculate_bmi_category(bmi)
    catlabel = Label(window, text=cat, font=("Arial", 9))
    x_pos = 80
    catlabel.place(x=x_pos, y=180)





w_label = Label(window, text='Kilo (kg)', font=('calibre', 10, 'bold'), padx=20, pady=20)
w = Entry(window, width=10)
w.focus_set()

h_label = Label(window, text='Boy (cm)', font=('calibre', 10, 'bold'))
h = Entry(window, width=10)

calcButton = Button(window, text="Calculate", command=lambda: calBMI(w.get(), h.get()))

w_label.grid(row=0, column=0)
w.grid(row=0, column=1)
h_label.grid(row=1, column=0)
h.grid(row=1, column=1)
calcButton.place(x=60, y=100)

window.mainloop()
