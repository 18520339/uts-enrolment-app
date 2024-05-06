import tkmacosx
import tkinter as tk
from tkinter import font as tkfont, messagebox
from common import Utils
from exception_window import ExceptionWindow


class SubjectsWindow:
    def __init__(self, root, student_controller):
        self.root = root
        self.root.title('University Enrollment System - Subjects Window')
        self.root.configure(bg='white')
        self.root.geometry('500x300')
        self.student_controller = student_controller

        # Custom Fonts
        title_font = tkfont.Font(family='Century Gothic', size=18, weight="bold", slant="italic")
        button_font = tkfont.Font(family='Century Gothic', size=12, weight='bold')
        
        # Title and Treeview Frame
        tk.Label(self.root, text="Your Enrolled Subjects", bg='white', fg='#00796b', font=title_font).pack(pady=10)
        self.tree = Utils.render_tk_treeview(self.root, height=4)
        self.load_subjects()
    
        # Button Panel
        buttons_frame = tk.Frame(self.root, bg='white')
        buttons_frame.pack(padx=30, fill='x', expand=True)

        tkmacosx.Button(buttons_frame, text='Refresh List', command=self.load_subjects, relief='flat', 
                  font=button_font, bg='#26a69a', fg='white', padx=10, pady=5).pack(side='left', padx=3)
        
        tkmacosx.Button(buttons_frame, text='Remove Selected', command=self.remove_subjects, relief='flat', 
                  font=button_font, bg='#ef5350', fg='white', padx=10, pady=5).pack(side='left', padx=3)
        

    def load_subjects(self):
        self.enrolled_subjects = {}
        self.tree.delete(*self.tree.get_children()) # Clear existing entries
        for subject in self.student_controller.current_student.subjects:
            self.enrolled_subjects[subject.subject_id] = subject
            self.tree.insert('', 'end', values=(subject.subject_id, subject.name, subject.mark, subject.grade))


    def remove_subjects(self):
        selected_rows = self.tree.selection()
        if not selected_rows:
            ExceptionWindow(self.root, 'Selection Missing', 'Please select a subject to remove', 'warning')
            return
        
        removed_details_str = ''
        for row in selected_rows:
            subject_details = self.tree.item(row, 'values')
            subject_to_remove = self.enrolled_subjects.pop(subject_details[0])
            self.student_controller.current_student.remove_subject_by_id(subject_to_remove.subject_id)
            removed_details_str += str(subject_to_remove) + '\n'
        
        self.load_subjects()
        messagebox.showinfo(
            'Remove Successful', 
            f'You are now enrolled in {len(self.student_controller.current_student.subjects)} ' 
            f'out of 4 subjects:\n{removed_details_str}')
        