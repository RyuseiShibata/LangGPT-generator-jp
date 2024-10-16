# タスクに必要な初期化モジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path)  # Pythonモジュールパスに上位ディレクトリを追加

def gen_initialization(generator, messages):
    messages = [
        {"role": "system", "content": "あなたはユーザーが提供するタスクを分析し、タスクの初期化部分を確認してください。これは、タスク開始前のユーザーとの簡単な挨拶のやり取りになります。例えば、ユーザーがLLMに栄養プランを提供してほしい場合、初期化情報は以下のようになります：\n栄養プランナーとして、あなたの状況に基づいて栄養アドバイスを提供します。"},
    ] + messages
    response = generator.generate_response(messages)
    return response
