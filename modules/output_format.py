# タスクに必要な出力フォーマットモジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path)  # Pythonモジュールパスに上位ディレクトリを追加

def gen_output_format(generator, messages):
    messages = [
        {"role": "system", "content": "ユーザーが提供したタスクを分析し、タスクの出力フォーマットを決定してください。どのような対話情報も出力しないでください。出力フォーマットはできるだけシンプルにし、JSONやXMLなどの標準フォーマットを優先的に検討してください。もし標準フォーマットがこのタスクに適さない場合、1文で簡潔にフォーマットを説明してください。詳細は含めないでください。例えば、ユーザーがLLMに方程式の解を求める場合、出力フォーマットの情報は次のようになります：\n- 出力は1つの数字であり、方程式の解を表します。"},
    ] + messages
    response = generator.generate_response(messages)
    return response
