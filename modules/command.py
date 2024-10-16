# タスクのコマンドモジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # 上位ディレクトリをPythonモジュールのパスに追加

def gen_command(client, messages):
    messages = [
        {"role": "system", "content": "ユーザーが与えたタスクを分析し、そのタスクに必要なアクションに基づいてLLM用のコマンドプロンプトを生成してください。コマンドは箇条書き形式で出力し、各コマンドは「/」で始まり、その後にコマンド記号とコマンドの説明が続きます。例えば、ユーザーがLLMで『誰がスパイか』ゲームを遊びたい場合、コマンド情報は次のようになります：\n- /describe あなたの役割を説明してください\n- /vote 敵対陣営だと思うプレイヤーに投票してください"},
    ] + messages
    response = client.generate_response(messages)
    return response
