import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tkmacosx
import tkinter as tk
from tkinter import font as tkfont
from common import Utils
from controllers import StudentController
from exception_window import ExceptionWindow


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('University Enrollment System - Login Window')
        self.root.configure(bg='white')
        self.root.resizable(False, False)

        self.root.bind('<Return>', lambda e: self.login())
        self.student_controller = StudentController()
        Utils.center_tk_window(self.root)

        # Custom fonts
        title_font = tkfont.Font(family='Century Gothic', size=23, weight='bold')
        label_font = tkfont.Font(family='Century Gothic', size=12, weight='bold')
        entry_font = tkfont.Font(family='Century Gothic', size=11)

        # Title and Frame for form elements
        tk.Label(self.root, text='🎓Welcome to GUIUniApp', font=title_font, bg='white', fg='#00796b').pack(pady=(25, 20))
        form_frame = tk.Frame(self.root, bg='beige')
        form_frame.pack(padx=40, pady=(5, 40), fill='both', expand=True)

        # Email and Password entries with decorative elements
        tk.Label(form_frame, text='Email:', font=label_font, bg='beige', fg='red').grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky='w')
        self.email_entry = tk.Entry(form_frame, width=35, font=entry_font, bg='white', fg='black')
        self.email_entry.grid(row=0, column=1, padx=(0, 20), pady=(20, 5), sticky='e')
        self.email_entry.focus_set()

        tk.Label(form_frame, text='Password:', font=label_font, bg='beige', fg='red').grid(row=1, column=0, padx=(20, 10), pady=10, sticky='w')
        self.password_entry = tk.Entry(form_frame, show='*', width=35, font=entry_font, bg='white', fg='black')
        self.password_entry.grid(row=1, column=1, padx=(0, 20), pady=5, sticky='e')

        tkmacosx.Button(
            form_frame, text='Login', command=self.login, relief='flat', font=label_font, bg='dodgerblue', fg='white'
        ).grid(row=2, column=1, columnspan=1, padx=20, pady=10, ipadx=30, ipady=5, sticky='e')
        
        
    def login(self):
        email = self.email_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        if not email or not password:
            ExceptionWindow(self.root, 'Error', 'Please enter both email and password', 'error')
            return
        
        # quan.dang@university.com -- Helloworld123
        try:
            if Utils.validate_email(email) and Utils.validate_password(password):
                student = self.student_controller.login_student(email, password)
                if student:
                    ExceptionWindow(self.root, 'Login Successful', f'Welcome back, {student.name}!', 'info')
                    self.open_enrolment_window()
            else: ExceptionWindow(self.root, 'Login Failed', 'Invalid email or password format', 'error')
        except Exception as e:
            ExceptionWindow(self.root, 'Login Failed', str(e).replace('\t', ''), 'error')
    
    
    def open_enrolment_window(self):
        from enrolment_window import EnrolmentWindow
        for widget in self.root.winfo_children(): widget.destroy() 
        EnrolmentWindow(self.root, self.student_controller)


if __name__ == '__main__':
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()
