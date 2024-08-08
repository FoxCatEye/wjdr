import tkinter as tk


def select_all(checkboxes):
    for checkbox in checkboxes:
        checkbox.select()


def main():
    root = tk.Tk()
    root.title("复选框一键全选示例")

    checkbox_vars = [tk.IntVar() for _ in range(3)]  # 创建3个复选框的状态变量
    checkboxes = [tk.Checkbutton(root, text="我", variable=checkbox_vars[0]),
                  tk.Checkbutton(root, text="她", variable=checkbox_vars[1]),
                  tk.Checkbutton(root, text="他", variable=checkbox_vars[2])]

    select_all_button = tk.Button(root, text="一键全选", command=lambda: select_all(checkboxes))

    for checkbox in checkboxes:
        checkbox.grid(row=i//4, column=i%4, sticky=tk.W)
    select_all_button.pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    main()