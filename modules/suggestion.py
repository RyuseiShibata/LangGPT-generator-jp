# タスクの提案モジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path)  # Pythonモジュールパスに上位ディレクトリを追加

def gen_suggestion(client, messages):
    messages = [
        {"role": "system", "content": "ユーザーが提供するタスクを分析し、タスクの提案情報を無序リスト形式で生成してください。どのような対話情報も出力しないでください。例えば、ユーザーがLLMに「誰がスパイか」ゲームをプレイさせたい場合、提案情報は次のようになります：\n- 自分の陣営が明確でないときは、説明をできるだけ曖昧にする"},
    ] + messages
    response = client.generate_response(messages)
    return response
