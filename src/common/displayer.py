import tkinter as tk
from tkinter import ttk
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from models import Student


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
    

class ScreenDisplayer:
    
    @staticmethod
    def display_students_table(students: 'List[Student]', column_config: dict = {}) -> None:
        if students is None or len(students) == 0:
            print('\t< Nothing to display >')
            return
        
        columns = { # Format key: (header name, value function, width)
            'student_id': ('ID', lambda s: s.student_id, 10), 
            'name': ('Name', lambda s: s.name, 20),
            'email': ('Email', lambda s: s.email, 30),
            'subject_count': ('Subject Count', lambda s: len(s.subjects), 15),
            'average_mark': ('Avg. Mark', lambda s: s.average_mark, 15),
            'overall_grade': ('Grade', lambda s: s.overall_grade, 10)
        }

        header, separator = '\t|', '\t-'
        for key, value in columns.items():
            if column_config.get(key, True):
                header += f' {value[0]:<{value[2]}} |'
                separator += '-' * (value[2] + 3)
        print(f'{separator}\n{header}\n{separator}')

        for student in students:
            row = '\t|'
            for key, value in columns.items():
                if column_config.get(key, True):
                    func_value, space = value[1](student), value[2]
                    if type(func_value) == str:
                        row += f' {func_value:<{space}} |'
                    else:
                        row += f' {func_value:>{space}} |'
            print(row)
        print(separator)


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