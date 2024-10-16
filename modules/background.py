# タスクの背景モジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # 上位ディレクトリをPythonモジュールのパスに追加

def gen_background(client, messages):
    messages = [
        {"role": "system", "content": "ユーザーが与えたタスクを分析し、タスクの背景情報を生成する必要があります。背景情報は箇条書き形式で出力してください。例えば、ユーザーがLLMを使って『誰がスパイか』ゲームを遊びたい場合、背景情報は次のようになります：\n- あなたは『誰がスパイか』ゲームに参加しています\n- あなたの役割は“黄桃”です。"},
    ] + messages
    response = client.generate_response(messages)
    return response
