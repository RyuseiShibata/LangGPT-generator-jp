# タスクに必要なワークフローモジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path)  # Pythonモジュールパスに上位ディレクトリを追加

def gen_workflow(generator, messages):
    messages = [
        {"role": "system", "content": "ユーザーが提供するタスクを分析し、このタスクを実行するために必要なワークフローを分解し、順序付きリスト形式で出力してください。番号は手順の順序を表します。どのような対話情報も出力しないでください。分岐が必要なワークフローでは、'1.1'や'1.2'のようにサブフローで示してください。繰り返しが必要な場合には、「ステップ2に戻る」や「前のステップを繰り返す」といった表現を使用してください。例えば、ユーザーがLLMに一元二次方程式を解かせる場合、ワークフロー情報は次のようになります：\n1. 方程式を標準形に変形し、方程式の係数a、b、cを確認する。\n2. 方程式の判別式を計算し、解の状況を分析する。\n2.1 判別式＞0の場合、実数解が2つある。\n2.2 判別式=0の場合、実数解が1つある。\n2.3 判別式<0の場合、実数解がない。\n3. 解の状況に応じて解の形式を決定する。\n4. 方程式の解を求める。\n5. 解が正しいかどうか検証する。"},
    ] + messages
    response = generator.generate_response(messages)
    return response
