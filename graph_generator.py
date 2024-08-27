# graph_generator.py
# グラフ生成のロジックを扱うファイル

import matplotlib.pyplot as plt
from matplotlib import font_manager
import textwrap

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
        fig, ax = plt.subplots(figsize=(7, len(percentages) * 0.5))  # グラフ幅を広げる

        # 各データポイントに対して、テキストを配置
        for i, (percentage, event) in enumerate(zip(percentages, events)):
            wrapped_text = textwrap.fill(event, width=30)  # テキストを30文字で折り返し
            ax.text(0.5, i, wrapped_text, ha='left', va='center', fontsize=12, fontproperties=self.font_prop)

        # 縦軸にパーセンテージを設定
        ax.set_yticks(range(len(percentages)))
        ax.set_yticklabels(percentages, fontproperties=self.font_prop)

        # 軸の表示を削除して、見た目をすっきりさせる
        ax.set_xticks([])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)

        # マージンを調整して左右が見切れないようにする
        plt.subplots_adjust(left=0.3, right=0.85)  # 右側のマージンを調整

        return fig  # フィギュアオブジェクトを返す

    def save_graph(self, fig, output_path):
        # グラフを保存
        fig.savefig(output_path, bbox_inches='tight')
        plt.close(fig)
