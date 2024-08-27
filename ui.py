# ui.py
# GUIの構築を行うファイル

import tkinter as tk
from tkinter import filedialog, messagebox
from graph_generator import GraphGenerator
from data_handler import DataHandler


class GraphApp:
    def __init__(self):
        # メインウィンドウの設定
        self.root = tk.Tk()
        self.root.title("グラフ作成アプリ")
        self.root.geometry("400x200")
        
        # インポートボタンの設定
        self.import_button = tk.Button(self.root, text="CSVをインポート", command=self.import_csv)
        self.import_button.pack(pady=20)
        
        # エクスポートボタンの設定
        self.export_button = tk.Button(self.root, text="グラフをエクスポート", command=self.export_graph)
        self.export_button.pack(pady=20)
        
        # グラフ生成とデータ処理のクラスを初期化
        self.graph_generator = GraphGenerator()
        self.data_handler = DataHandler()
        self.data = None

    def import_csv(self):
        # CSVファイルのインポート
        file_path = filedialog.askopenfilename(filetypes=[("CSVファイル", "*.csv")])
        if file_path:
            self.data = self.data_handler.load_csv(file_path)
            messagebox.showinfo("成功", "CSVファイルをインポートしました")

    def export_graph(self):
        # グラフのエクスポート
        if self.data is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNGファイル", "*.png")])
            if file_path:
                self.graph_generator.generate_graph(self.data, file_path)
                messagebox.showinfo("成功", "グラフをエクスポートしました")
        else:
            messagebox.showwarning("エラー", "まずCSVファイルをインポートしてください")

    def run(self):
        # メインループを開始
        self.root.mainloop()
