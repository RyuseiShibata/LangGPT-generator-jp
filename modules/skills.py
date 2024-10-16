# タスクに必要なスキルモジュールを生成

import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path)  # Pythonモジュールパスに上位ディレクトリを追加

def gen_skills(generator, messages):
    messages = [
        {"role": "system", "content": "ユーザーが提供するタスクを分析し、タスクに必要なスキルを確認して、無序リスト形式で出力してください。スキルの説明はできるだけ簡潔にし、詳細を含めないでください。例えば、ユーザーがLLMに時事ホットトピックを評価してほしい場合、必要なスキルは次のようになります：\n- 様々な社会的ホットトピックに精通し、事件の背景や経緯を迅速に把握できる\n- 多角的に事件を分析し、独特で鋭い見解を提供できる"},
    ] + messages
    response = generator.generate_response(messages)
    return response
