#!/usr/bin/env python3

# -----------------------------------
# A simple password generator that generates a password between 6-15 characters.
# The generated passwords can include both upper and lowercase letters, numbers 0-9 and some
# special characters from the possible_chars string.
# GUI created with Tkinter module.
# Mikael Widell 2018-01-15
# -----------------------------------

import random
from tkinter import Tk, BOTH, X, LEFT, messagebox
from tkinter.ttk import Frame, Label, Entry, Button

possible_chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789!#%&$'


class PasswordGenerator(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

        self.my_pw = ''

    def initUI(self):
        self.master.title('Simple PasswordGenerator v1.0')
        self.pack(fill=BOTH, expand=False)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text='Input password lenght: (6-15)', width=23)
        lbl1.pack(side=LEFT, padx=5, pady=10)

        self.entry1 = Entry(frame1, width=10)
        self.entry1.pack(side=LEFT, padx=2)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text='Generated password:', width=16)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        self.entry2 = Entry(frame2, width=17)
        self.entry2.pack(side=LEFT, padx=2)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        gen_button = Button(self, text="Generate", command=self.generate)
        gen_button.pack(side=LEFT, padx=5, pady=5)

    def generate(self):
        self.entry2.delete(0, 'end')
        try:
            pw_length = int(self.entry1.get())
            if pw_length >= 6 and pw_length <=15:
                for i in range(pw_length):
                    index = random.randrange(len(possible_chars))
                    self.my_pw += possible_chars[index]
                self.entry2.insert(1, self.my_pw)
                self.my_pw = ''
            else:
                messagebox.showwarning('Error!', 'Password must be 6-15 characters!')
                self.entry1.delete(0, 'end')
        except:
            messagebox.showwarning('Error!', 'Field must contain a number!')
            self.entry1.delete(0, 'end')


def main():
    app_window = Tk()
    app_window.geometry("300x100+300+300")
    app = PasswordGenerator()
    app_window.mainloop()


if __name__ == '__main__':
    main()
