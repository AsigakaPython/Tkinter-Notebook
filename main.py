import os
import tkinter as tk
import tkinter.filedialog as tfd

file_name = ""


def open_file():
    global file_name
    file_name = tfd.askopenfilename()
    if file_name != "":
        with open(file_name, encoding='utf-8') as file:
            file_path["text"] = file_name
            window.title("Блокнот " + os.path.basename(file_name).split('/')[-1])
            content_text.insert(1.0, file.read())


def new_file():
    global file_name
    file_name = ""
    file_path["text"] = file_name
    window.title("Блокнот")
    content_text.delete(1.0, "end")


def save_file():
    global file_name

    if file_name != "":
        with open(file_name, "w", encoding='utf-8') as file:
            file_path["text"] = file_name
            window.title("Блокнот " + os.path.basename(file_name).split('/')[-1])
            file.write(content_text.get(1.0, "end"))
    else:
        save_as_file()


def save_as_file():
    global file_name
    file_name = tfd.asksaveasfilename()
    if file_name != "":
        with open(file_name, "w", encoding='utf-8') as file:
            file_path["text"] = file_name
            window.title("Блокнот " + os.path.basename(file_name).split('/')[-1])
            file.write(content_text.get(1.0, "end"))


def app_exit():
    window.destroy()


window = tk.Tk()
window.geometry('700x500')
window.title("Блокнот")

content_text = tk.Text(window)
content_text.place(relheight=1, relwidth=1)

file_path = tk.Label(window, anchor="w")
file_path.pack(side='bottom', fill='x')

main_menu = tk.Menu(window)
window.configure(menu=main_menu)

file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Открыть", command=open_file)
file_menu.add_command(label="Новый", command=new_file)
file_menu.add_command(label="Сохранить", command=save_file)
file_menu.add_command(label="Сохранить как", command=save_as_file)
file_menu.add_command(label="Выйти", command=app_exit)

window.mainloop()
