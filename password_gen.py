from tkinter import *

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title('Calculator')
        
        self.entry = Entry(self.root,width=30,justify='left', font=("Arial",20))
        self.entry.grid(row=0,column=0, columnspan=4, padx=10, pady=10)
        
        
    def create_button(self, text, row, column):
        button = Button(self.root,text=text,width=5,height=2,font=("Arial", 16),command=lambda:self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)
    
    def button_click(self, text):
        if text == "==":
            return 
        
if __name__  == "__main__":
    root = Tk()
    calculator = Calculator(root)
    root.mainloop()