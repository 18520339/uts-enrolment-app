import os
import re
import random
import tkinter as tk
from tkinter import ttk


class Utils:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'students.data')
    EMAIL_PATTERN = r'^[a-zA-Z0-9]+\.[a-zA-Z0-9]+@university\.com$'
    PASSWORD_PATTERN = r'^[A-Z][a-zA-Z]{5,}\d{3,}$'

    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = re.compile(Utils.EMAIL_PATTERN)
        if bool(pattern.match(email.lower())): return True
        # print('Email must be in the form of firstname.lastname@university.com.')
        return False

    @staticmethod
    def validate_password(password: str) -> bool:
        pattern = re.compile(Utils.PASSWORD_PATTERN)
        if bool(pattern.match(password)): return True
        # print('Password must start with UPPERCASE, followed by >= 5 letters and >= 3 digits.')
        return False
    
    
    @staticmethod
    def center_tk_window(window, width=500, height=300) -> None:
        center_x = window.winfo_screenwidth() // 2 - width // 2
        center_y = window.winfo_screenheight() // 2 - height // 2 - 25 # 25 for the title bar
        window.geometry(f'{width}x{height}+{center_x}+{center_y}')
        
        
    @staticmethod
    def render_tk_treeview(root, height=10):
        # Styling for Treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview', rowheight=25, background='white', fieldbackground='white', font=('Century Gothic', 12))
        style.map('Treeview', background=[('selected', 'dodgerblue')])
        
        # Treeview Frame
        frame = tk.Frame(root, bg='beige')
        frame.pack(fill='both', expand=True, padx=30)
        
        # Treeview for subjects
        tree = ttk.Treeview(frame, columns=('Sub. ID', 'Name', 'Mark', 'Grade'), show='headings', height=height)
        tree.heading('Sub. ID', text='Sub. ID')
        tree.heading('Name', text='Name')
        tree.heading('Mark', text='Mark')
        tree.heading('Grade', text='Grade')
        tree.column('Sub. ID', anchor='center', width=50)
        tree.column('Name', anchor='w', width=250)
        tree.column('Mark', anchor='center', width=50)
        tree.column('Grade', anchor='center', width=50)
        tree.pack(side='left', fill='both', expand=True)

        # Scrollbar for the Treeview
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
        scrollbar.pack(side='right', fill='y')
        tree.configure(yscrollcommand=scrollbar.set)
        return tree
    
    
class Color:
    
    @staticmethod
    def make_red(text):
        return f'\033[91m{text}\033[00m'

    @staticmethod
    def make_yellow(text):
        return f'\033[93m{text}\033[00m'
        
    @staticmethod
    def make_cyan(text):
        return f'\033[96m{text}\033[00m'

    @staticmethod
    def make_green(text):
        return f'\033[92m{text}\033[00m'
    
    
class Randomizer:
        
    @staticmethod
    def generate_student_id() -> str:
        return str(random.randint(1, 999999)).zfill(6) # Generate a unique 6-digit student ID

    @staticmethod
    def generate_subject_id() -> str:
        return str(random.randint(1, 999)).zfill(3) # Generate a unique 3-digit subject ID

    @staticmethod
    def generate_subject_name() -> str:
        subject_names = ['Database', 'Network', 'Programming', 'Mathematics', 'Physics', 'Chemistry', 'Biology']
        subject_levels = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
        return random.choice(subject_names) + ' ' + random.choice(subject_levels) # Generate a random subject name

    @staticmethod
    def generate_subject_mark() -> int:
        return random.randint(25, 100) # Generate a random subject mark between 25 and 100