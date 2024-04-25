from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter.filedialog import askopenfile
import os
import subprocess
import threading

top = Tk()
top.title("adb GUI")
top.iconbitmap('adb.ico')
my_list = []
top.geometry("1200x500")
top.configure(bg='blue')

def update_listbox():
    listbox.delete(0, END)
    for element in my_list:
        listbox.insert(END, element)

listbox = Listbox(top, height=15, width=100)
listbox.pack()
listbox.place(x=50, y=0)

listb2 = Listbox(top, height=13, width=100)
listb2.pack()
listb2.place(x=50, y=280)

def onbuttonclick():
    filename = askopenfile()
    if filename:
        name = filename.name
        my_list.append(name)
        update_listbox()

def delete_last():
    if my_list:
        my_list.pop()
        update_listbox()
    else:
        messagebox.showinfo("Error", "Nothing to delete")

def install():
    if len(my_list) == 0:
        messagebox.showinfo("Error", "Nothing to install")
    else:
        for element in my_list:
            t = threading.Thread(target=install_apk, args=(element,))
            t.start()

def install_apk(element):
    command = ("adb", "install", element)
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        lines = result.split('\n')
        for line in lines:
            listb2.insert(END, line)
    except subprocess.CalledProcessError as e:
        listb2.insert(END, f"Error: {e.output}")

def reboot_recovery():
    t = threading.Thread(target=reboot_recovery_thread)
    t.start()

def reboot_recovery_thread():
    try:
        result = subprocess.check_output(["adb", "reboot", "recovery"], shell=True, text=True)
        listb2.insert(END, result)
    except subprocess.CalledProcessError as e:
        listb2.insert(END, f"Error: {e.output}")

def reboot_fastboot():
    t = threading.Thread(target=reboot_fastboot_thread)
    t.start()

def reboot_fastboot_thread():
    try:
        result = subprocess.check_output(["adb", "reboot", "bootloader"], shell=True, text=True)
        listb2.insert(END, result)
    except subprocess.CalledProcessError as e:
        listb2.insert(END, f"Error: {e.output}")

def reboot_download():
    t = threading.Thread(target=reboot_download_thread)
    t.start()

def reboot_download_thread():
    try:
        result = subprocess.check_output(["adb", "reboot", "download"], shell=True, text=True)
        listb2.insert(END, result)
    except subprocess.CalledProcessError as e:
        listb2.insert(END, f"Error: {e.output}")

def send_adb_command():
    command = command_entry_adb.get()
    t = threading.Thread(target=send_adb_command_thread, args=(command,))
    t.start()

def send_adb_command_thread(command):
    try:
        result = subprocess.check_output(["adb", "shell", command], shell=True, text=True)
        listb2.insert(END, result)
    except subprocess.CalledProcessError as e:
        listb2.insert(END, f"Error: {e.output}")

def send_fastboot_command():
    command = command_entry_fastboot.get()
    t = threading.Thread(target=send_fastboot_command_thread, args=(command,))
    t.start()

def send_fastboot_command_thread(command):
    try:
        result = subprocess.check_output(["fastboot", command], shell=True, text=True)
        listb2.insert(END, result)
    except subprocess.CalledProcessError as e:
        listb2.insert(END, f"Error: {e.output}")

def send_adb_shell_command():
    command = command_entry_adb_shell.get()
    t = threading.Thread(target=send_adb_shell_command_thread, args=(command,))
    t.start()

def send_adb_shell_command_thread(command):
    try:
        result = subprocess.check_output(["adb", command], shell=True, text=True)
        listb2.insert(END, result)
    except subprocess.CalledProcessError as e:
        listb2.insert(END, f"Error: {e.output}")

B = Button(top, text="Choose File", command=onbuttonclick)
B.place(x=315, y=250)
B.configure(bg='yellow')

D = delete_button = Button(top, text="Delete Last", command=delete_last)
delete_button.pack()
D.configure(bg = 'red')
D.place(x=200, y=250)

I = install_button = Button(top, text="Install", command=install)
install_button.pack()
I.configure(bg='green')
I.place(x=270, y=250)

R = reboot_button = Button(top, text="Reboot Recovery", command=reboot_recovery)
reboot_button.pack()
R.configure(bg='orange')
R.place(x=400, y=250)

F = fastboot_button = Button(top, text="Reboot Fastboot", command=reboot_fastboot)
fastboot_button.pack()
F.configure(bg='purple')
F.place(x=520, y=250)

D = download_button = Button(top, text="Reboot Download", command=reboot_download)
download_button.pack()
D.configure(bg='blue')
D.place(x=80, y=250)

command_label_adb = Label(top, text="Enter adb shell command:")
command_label_adb.pack()
command_label_adb.place(x=800, y=230)
command_label_adb.configure(bg='blue')

command_entry_adb = Entry(top, width=50)
command_entry_adb.pack()
command_entry_adb.place(x=790, y=250)

send_button_adb = Button(top, text="Send Command", command=send_adb_command)
send_button_adb.pack()
send_button_adb.configure(bg='gray')
send_button_adb.place(x=680, y=245)

command_label_fastboot = Label(top, text="Enter fastboot command:")
command_label_fastboot.pack()
command_label_fastboot.place(x=800, y=330)
command_label_fastboot.configure(bg='blue')

command_entry_fastboot = Entry(top, width=50)
command_entry_fastboot.pack()
command_entry_fastboot.place(x=790, y=350)

send_button_fastboot = Button(top, text="Send Command", command=send_fastboot_command)
send_button_fastboot.pack()
send_button_fastboot.configure(bg='gray')
send_button_fastboot.place(x=680, y=345)

command_label_adb_shell = Label(top, text="Enter adb command:")
command_label_adb_shell.pack()
command_label_adb_shell.place(x=800, y=430)
command_label_adb_shell.configure(bg='blue')

command_entry_adb_shell = Entry(top, width=50)
command_entry_adb_shell.pack()
command_entry_adb_shell.place(x=790, y=450)

send_button_adb_shell = Button(top, text="Send Command", command=send_adb_shell_command)
send_button_adb_shell.pack()
send_button_adb_shell.configure(bg='gray')
send_button_adb_shell.place(x=680, y=445)

top.mainloop()


