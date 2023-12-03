import tkinter as tk

class CharaIconButton(tk.Button):
    def __init__(self, master=None, chara_name="", input_var=None, image_path=None, **kwargs):
        self.chara_name=chara_name
        self.input_var=input_var
        self.image=None
        if image_path!=None:
            self.image=tk.PhotoImage(file=image_path)
            kwargs['image']=self.image
        kwargs['borderwidth']=0
        kwargs['highlightthickness']=0
        super().__init__(master, command=self.set_input, **kwargs)

    def set_input(self):
        if self.input_var is not None:
            self.input_var.set(self.chara_name)