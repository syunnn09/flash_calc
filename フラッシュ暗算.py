import tkinter as tk
from tkinter import ttk
import time
import numpy as np

class prev():
    def __init__(self):
        # 画面作成
        self.root = tk.Tk()
        self.root.title('フラッシュ暗算')
        self.root.geometry('350x330')
        
        # 中央配置
        self.root.update_idletasks()
        ww=self.root.winfo_screenwidth()
        lw=self.root.winfo_width()
        wh=self.root.winfo_screenheight()
        lh=self.root.winfo_height()
        self.root.geometry(str(lw) + 'x' + str(lh) + '+' + str(int(ww/2 - lw/2)) + '+' + str(int(wh/2 - lh/2)))
        
        # タイトル
        self.main_label = tk.Label(self.root, pady=17, text='フラッシュ暗算', font=('bold', 20))
        self.main_label.pack()
                
        # 初期化
        self.sum = 0
        self.create_time = 0
        
        # 数字表示
        self.label = tk.Label(text='', pady=15, width=7, fg='lime', bg='black', font=('bold', 35, 'italic'))
        self.label.pack()
        
        # 再生ボタン
        self.run_button = tk.Button(self.root, text='実行', command=self.create)
        self.run_button.pack(pady=5)
        
        # 解答入力
        self.answer_frame = tk.Frame(self.root)
        self.answer_frame.pack()
        self.answer = tk.Entry(self.answer_frame, fg='red', width=10)
        self.answer.pack(padx=10, side='left')
        self.answer_button = tk.Button(self.answer_frame, text='解答', width=6, command=self.check_num)
        self.answer_button.pack(pady=15, side='left')
        
        # 設定フレーム
        self.main_frame = tk.Frame(self.root, height=50, width=70)
        self.main_frame.pack()
        
        # 表示速度
        self.speed_frame = tk.Frame(self.main_frame, height=30)
        self.speed_label = tk.Label(self.speed_frame, text='速度')
        self.speed_box = ttk.Combobox(self.speed_frame, values=[0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], width=5)
        self.speed_frame.pack(side=tk.LEFT)
        self.speed_label.pack(padx=15)
        self.speed_box.pack(padx=15)
        self.speed_box.set(0.8)
        
        # 表示桁数
        self.digits_frame = tk.Frame(self.main_frame, height=30)
        self.digits_label = tk.Label(self.digits_frame, text='桁数')
        self.digits_box = ttk.Combobox(self.digits_frame, values=[1, 2, 3], width=5)
        self.digits_frame.pack(side=tk.LEFT)
        self.digits_label.pack(padx=15)
        self.digits_box.pack(padx=15)
        self.digits_box.set(2)
        
        # 表示回数
        self.times_frame = tk.Frame(self.main_frame, height=30)
        self.times_label = tk.Label(self.times_frame, text='回数')
        self.times_box = ttk.Combobox(self.times_frame, values=[3, 4, 5, 6, 7, 8, 9, 10], width=5)
        self.times_frame.pack(side=tk.LEFT)
        self.times_label.pack(padx=15)
        self.times_box.pack(padx=15)
        self.times_box.set(5)
        
        self.root.mainloop()

    # 乱数生成用
    def keta(self):
        digits = int(self.digits_box.get())
        if digits == 1:
            self.randnum = 9
            self.plusnum = 0
        elif digits == 2:
            self.randnum = 90
            self.plusnum = 10
        else:
            self.randnum = 900
            self.plusnum = 100
            
        
    # 乱数生成
    def create(self):
        self.answer.delete(0, tk.END)
        self.create_limit = int(self.times_box.get())
        self.keta()
        while self.create_time < self.create_limit:
            num = np.random.randint(self.randnum) + self.plusnum
            self.sum += num
            self.label.configure(text=num)
            self.label.update()
            self.create_time += 1
            time.sleep(float(self.speed_box.get()))

        self.label.configure(text='?')
        self.label.update()
        self.create_time = 0
        

    # 正解チェック
    def check_num(self):
        self.ans = int(self.answer.get())
        if self.ans == self.sum:
            self.label.configure(text='正解')
            self.label.update()
        else:
            self.label.configure(text=self.sum)
            self.label.update()
        self.sum = 0

        
if __name__ == '__main__':
    prev()