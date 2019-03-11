import tkinter as tk


# 登録フォーム
class ResistForm(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("TEST")
        self.geometry("300x200")

# ログインフォーム
class LoginForm(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        tk.Button(text="test",command=self.register).pack()

    # 登録フォームの呼び出し
    def register(self):
        self.screen = ResistForm(self.master)

if __name__ == '__main__':
    root = tk.Tk()
    login_form = LoginForm(master=root)
    login_form.mainloop()
