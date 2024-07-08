import tkmacosx
import tkinter as tk
from tkinter import font as tkfont, Toplevel
from common import ScreenDisplayer


class ExceptionWindow:
    def __init__(self, parent, title, message, message_type='error'):
        self.root = Toplevel(parent)
        self.root.title(message_type.title())
        self.root.resizable(False, False)
        self.root.bind('<Return>', lambda e: self.root.destroy())
        ScreenDisplayer.center_tk_window(self.root, 400, 200)

        # This makes the window block other windows until it is closed
        self.root.transient(parent)
        self.root.grab_set()

        # Custom Fonts and Styles
        icon_font = tkfont.Font(family='Century Gothic', size=24, weight='bold')
        title_font = tkfont.Font(family='Century Gothic', size=16, weight='bold')
        message_font = tkfont.Font(family='Century Gothic', size=12, weight='bold')
        
        # Symbols for different message types
        symbols = {
            'info': {'icon': '\u2139', 'title_color': '#1e88e5', 'bg_color': '#e3f2fd'}, # Information sign
            'warning': {'icon': '\u26A0', 'title_color': '#f9a825', 'bg_color': '#fffde7'}, # Warning sign
            'error': {'icon': '\u274C', 'title_color': '#e53935', 'bg_color': '#ffebee'}, # Cross mark
        }
        symbol = symbols.get(message_type, {'icon': '\u2757', 'title_color': 'black', 'bg_color': 'white'}) # Exclamation mark for others
        icon, title_color, bg_color = symbol.values()

        # Title and Message with Icons
        self.root.configure(bg=bg_color)
        header_frame = tk.Frame(self.root, bg=bg_color)
        header_frame.pack(fill='x', padx=10, pady=(20, 10), expand=True)
        tk.Label(header_frame, text=f'{icon}', font=icon_font, bg=bg_color, fg=title_color).pack(side='left', padx=(10, 0))
        tk.Label(header_frame, text=f'{title}!', font=title_font, bg=bg_color, fg=title_color).pack(side='left', padx=10)

        message_frame = tk.Frame(self.root, bg=bg_color)
        message_frame.pack(fill='both', padx=10, pady=5, expand=True)
        tk.Label(message_frame, text=message, font=message_font, wraplength=350, justify='left', bg=bg_color, fg='grey').pack()

        # OK Button to close the dialog
        button_frame = tk.Frame(self.root, bg=bg_color)
        button_frame.pack(fill='x', padx=40, pady=20, expand=True)
        tkmacosx.Button(button_frame, text='OK', command=self.root.destroy, font=message_font, relief='flat', bg=title_color, fg='white', padx=30, pady=5).pack()

        # Ensures the parent cannot be interacted with until this window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.root.destroy) # Ensure it closes properly
        self.root.wait_window()