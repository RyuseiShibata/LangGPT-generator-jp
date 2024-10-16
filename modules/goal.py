# タスクに必要な目標モジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path)  # Pythonモジュールパスに上位ディレクトリを追加

def gen_goal(generator, messages):
    messages = [
        {"role": "system", "content": "あなたはユーザーが提供するタスクを分析し、タスクの目標を確認して、無序リストの形式で出力してください。どのような対話情報も出力しないでください。目標はできるだけ簡潔にし、タスクに明確に複数の行動が必要な場合を除き、通常は1つ、一般的には2つを超えないようにしてください。例えば、ユーザーがLLMに方程式の解を計算させたい場合、目標情報は以下のようになります：\n- 正しい方程式の解を計算する"},
    ] + messages
    response = generator.generate_response(messages)
    return response
