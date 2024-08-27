# ui.py
# GUIの構築を行うファイル

import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph_generator import GraphGenerator
from data_handler import DataHandler

class GraphApp:
    def __init__(self):
        # メインウィンドウの設定
        self.root = tk.Tk()
        self.root.title("グラフ作成アプリ")
        self.root.geometry("600x400")
        
        # インポートボタンの設定
        self.import_button = tk.Button(self.root, text="CSVをインポート", command=self.import_csv)
        self.import_button.pack(pady=20)
        
        # エクスポートボタンの設定
        self.export_button = tk.Button(self.root, text="グラフをエクスポート", command=self.export_graph)
        self.export_button.pack(pady=20)
        
        # キャンバスの初期化
        self.canvas = None

        # グラフ生成とデータ処理のクラスを初期化
        self.graph_generator = GraphGenerator()
        self.data_handler = DataHandler()
        self.data = None
        self.fig = None

    def import_csv(self):
        # CSVファイルのインポート
        file_path = filedialog.askopenfilename(filetypes=[("CSVファイル", "*.csv")])
        if file_path:
            try:
                self.data = self.data_handler.load_csv(file_path)
                self.display_graph()  # グラフを表示するメソッドを呼び出し
            except Exception as e:
                messagebox.showwarning("エラー", f"CSVファイルのインポートに失敗しました: {str(e)}")

    def display_graph(self):
        # 既存のキャンバスをクリア
        if self.canvas:
            self.canvas.get_tk_widget().pack_forget()

        # グラフを作成
        self.fig = self.graph_generator.generate_graph(self.data)

        # キャンバスにグラフを描画
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=10)

    def export_graph(self):
        # グラフのエクスポート
        if self.data is not None and self.fig is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNGファイル", "*.png")])
            if file_path:
                try:
                    self.graph_generator.save_graph(self.fig, file_path)
                except Exception as e:
                    messagebox.showwarning("エラー", f"グラフのエクスポートに失敗しました: {str(e)}")
        else:
            messagebox.showwarning("エラー", "まずCSVファイルをインポートしてください")

    def run(self):
        # メインループを開始
        self.root.mainloop()
