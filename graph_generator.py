# graph_generator.py
# グラフ生成のロジックを扱うファイル

import matplotlib.pyplot as plt
from matplotlib import font_manager
import textwrap
import re

class GraphGenerator:
    def __init__(self):
        # 日本語フォントの設定
        self.font_path = 'C:/Windows/Fonts/meiryo.ttc'  # Meiryoフォントを使用
        self.font_prop = font_manager.FontProperties(fname=self.font_path)
    
    def generate_graph(self, data):
        # 縦軸のデータを抽出
        percentages = data['パーセンテージ']
        # テキストデータを抽出
        events = data['イベント']

        # グラフのサイズを設定
        fig, ax = plt.subplots(figsize=(12, 8))  # グラフサイズを大きく設定

        # 各データポイントに対して、テキストを配置
        for percentage, event in zip(percentages, events):
            match = re.match(r"(\d+)-(\d+)", str(percentage))  # 範囲かどうかをチェック
            if match:
                start, end = map(int, match.groups())
                position = (1 - (start + end) / 200.0) * len(percentages)  # 範囲の中央位置
                wrapped_text = textwrap.fill(event, width=25)  # テキストを25文字で折り返し
                ax.text(0.65, position, wrapped_text, ha='left', va='center', fontsize=12, fontproperties=self.font_prop)  # 最右側に表示
            else:
                position = (1 - int(percentage) / 100.0) * len(percentages)  # 単一の数値の場合
                wrapped_text = textwrap.fill(event, width=25)  # テキストを25文字で折り返し
                ax.text(0.25, position, f'{percentage}%', ha='right', va='center', fontsize=12, fontproperties=self.font_prop)  # 数直線の左側にパーセンテージ表示
                ax.text(0.35, position, wrapped_text, ha='left', va='center', fontsize=12, fontproperties=self.font_prop)  # 数直線の右側にイベント表示

        # 縦軸に数直線を描画
        ax.axvline(x=0.3, color='black', linewidth=1)  # 数直線を描画

        # 縦軸の範囲を設定
        ax.set_ylim(0, len(percentages))  

        # 軸の表示を削除して、見た目をすっきりさせる
        ax.set_xticks([])
        ax.set_yticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        # マージンを調整して、左右が見切れないようにする
        plt.subplots_adjust(left=0.1, right=0.9, top=0.95, bottom=0.05)  # マージンを再調整

        return fig  # フィギュアオブジェクトを返す

    def save_graph(self, fig, output_path):
        # グラフを保存
        fig.savefig(output_path, bbox_inches='tight')
        plt.close(fig)
