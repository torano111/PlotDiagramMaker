# data_handler.py
# CSVファイルのインポートとデータの処理を行うファイル

import pandas as pd

class DataHandler:
    def load_csv(self, file_path):
        # CSVファイルを読み込み、データフレームに変換
        data = pd.read_csv(file_path)
        return data
