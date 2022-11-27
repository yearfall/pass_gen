from random import randint
from tkinter import *
from os import getlogin

class pass_gen:
    def __init__(self,master):
        self.but = Button(text = 'Сгенерировать пароль')
        self.lab = Label(text = 'Генератор паролей',
            width=20,
            height=3
            )
        self.lab_resource = Label(text = 'Введите ресурс')
        self.lab_login = Label(text = 'Введите логин или почту')
        self.ent_resourse = Entry()
        self.ent_login = Entry()
        self.lab2 = Label()
        self.but.bind('<Button-1>',self.file_work)
        self.lab.pack()
        self.lab_resource.pack()
        self.ent_resourse.pack()
        self.lab_login.pack()
        self.ent_login.pack()
        self.but.pack()
        self.lab.pack()
        
    def pass_generation(self):
        char = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_/?!@#$%)(*'
        password = ''
        for i in range(25):
            ran_num = randint(0,(len(char)-1))
            password += char[ran_num]
        return password

    def file_work(self,event):
        password = self.pass_generation()
        username = getlogin()
        try:
            with open(f'C:/Users/{username}/Desktop/password.txt', mode ='a') as my_file:
                my_file.write(f'resourse = {self.ent_resourse.get()}, login = {self.ent_login.get()}, password = {password}\n')
        except FileNotFoundError:
            with open(f'C:/Users/{username}/Desktop/password.txt', mode = 'x') as my_file:
                my_file.write('Тут будут храниться ваши пароли!\n')       
        

if __name__ == '__main__':
    root = Tk()
    fg = pass_gen(root)
    root.mainloop()