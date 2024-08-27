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
        self.root.geometry("800x600")  # ウィンドウサイズを拡大
        
        # フレームを作成してボタンを配置
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        # インポートボタンの設定
        self.import_button = tk.Button(button_frame, text="インポート", command=self.import_csv)
        self.import_button.grid(row=0, column=0, padx=10)

        # エクスポートボタンの設定
        self.export_button = tk.Button(button_frame, text="エクスポート", command=self.export_graph)
        self.export_button.grid(row=0, column=1, padx=10)
        
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
        self.canvas.get_tk_widget().pack(pady=10, expand=True, fill='both')

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
