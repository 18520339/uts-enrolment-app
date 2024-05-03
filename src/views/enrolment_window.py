import tkinter as tk
from tkinter import font as tkfont, messagebox

from models import Subject
from common import Utils, Randomizer
from subject_window import SubjectsWindow
from exception_window import ExceptionWindow


class EnrolmentWindow:
    def __init__(self, root, student_controller):
        self.root = root
        self.root.title('University Enrollment System - Enrolment Window')
        self.root.configure(bg='white')
        self.subjects_root = None 
        self.subjects_window = None
        self.student_controller = student_controller
        Utils.center_tk_window(self.root, 500, 500)
        
        # Custom fonts
        title_font = tkfont.Font(family='Century Gothic', size=23, weight='bold', slant='italic')
        button_font = tkfont.Font(family='Century Gothic', size=12, weight='bold')
        
        # Title and Treeview
        tk.Label(self.root, text='Select Your Subjects', font=title_font, bg='#fefefe', fg='#00796b').pack(pady=20)
        self.tree = Utils.render_tk_treeview(self.root)

        # Populate tree with subjects
        self.available_subjects = {}
        for _ in range(15):
            subject = Subject(name=Randomizer.generate_subject_name())
            self.available_subjects[subject.subject_id] = subject
            self.tree.insert('', 'end', values=(subject.subject_id, subject.name, subject.mark, subject.grade))
            
        # Button Panel
        buttons_frame = tk.Frame(self.root, bg='white')
        buttons_frame.pack(padx=30, fill='x', expand=True)

        tk.Button(buttons_frame, text='Enroll', command=self.enroll_subjects, relief='flat', 
                  font=button_font, bg='#29b6f6', fg='white', padx=10).pack(side='left', padx=10)

        tk.Button(buttons_frame, text='Clear', command=self.clear_selections, relief='flat',
                  font=button_font, bg='#ef5350', fg='white', padx=10).pack(side='left', padx=10)

        tk.Button(buttons_frame, text='View Enrolled', command=self.open_subjects_window, relief='flat',
                  font=button_font, bg='#ab47bc', fg='white', padx=10).pack(side='left', padx=10)

        tk.Button(buttons_frame, text='Logout', command=self.logout, relief='flat',
                  font=button_font, bg='#26a69a', fg='white', padx=10).pack(side='left', padx=10)


    def enroll_subjects(self):
        selected_rows = self.tree.selection()
        if not selected_rows:
            ExceptionWindow(self.root, 'Selection Missing', 'Please select a subject to enroll', 'warning')
            return
        
        enrolled_details_str = ''
        if len(self.student_controller.current_student.subjects) + len(selected_rows) <= 4:
            for row in selected_rows:
                subject_details = self.tree.item(row, 'values')
                subject_to_enroll = self.available_subjects[subject_details[0]]
                self.student_controller.current_student.enroll_subject(subject_to_enroll)
                enrolled_details_str += str(subject_to_enroll) + '\n'
                
            if self.subjects_window and self.subjects_root.winfo_exists(): self.subjects_window.load_subjects()
            self.clear_selections()
            messagebox.showinfo(
                'Enrollment Successful', 
                f'You are now enrolled in {len(self.student_controller.current_student.subjects)} ' 
                f'out of 4 subjects:\n{enrolled_details_str}')
        else: ExceptionWindow(self.root, 'Enrollment Failed', 'Students are allowed to enrol in 4 subjects only', 'error')


    def clear_selections(self):
        self.tree.selection_remove(self.tree.selection())
        
        
    def open_subjects_window(self):
        self.subjects_root = tk.Toplevel(self.root)
        self.subjects_window = SubjectsWindow(self.subjects_root, self.student_controller) 
            
        
    def logout(self):
        from login_window import LoginWindow
        for widget in self.root.winfo_children(): widget.destroy() 
        self.student_controller.logout_student()
        LoginWindow(self.root)