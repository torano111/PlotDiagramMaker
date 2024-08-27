# graph_generator.py
# グラフ生成のロジックを扱うファイル

import matplotlib.pyplot as plt

class GraphGenerator:
    def generate_graph(self, data, output_path):
        # 縦軸のデータを抽出
        percentages = data['パーセンテージ']
        # テキストデータを抽出
        events = data['イベント']

        # グラフのサイズを設定
        plt.figure(figsize=(5, len(percentages) * 0.5))

        # 各データポイントに対して、テキストを配置
        for i, (percentage, event) in enumerate(zip(percentages, events)):
            plt.text(0.5, i, event, ha='left', va='center', fontsize=12)

        # 縦軸にパーセンテージを設定
        plt.yticks(range(len(percentages)), percentages)

        # 軸の表示を削除して、見た目をすっきりさせる
        plt.xticks([])
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.gca().spines['left'].set_visible(False)
        plt.gca().spines['bottom'].set_visible(False)

        # グラフを保存
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()
