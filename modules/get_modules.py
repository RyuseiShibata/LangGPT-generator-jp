# 説明: タスクに必要なモジュールを取得
import sys
import os
abs_path = os.getcwd()
sys.path.append(abs_path) # 上位ディレクトリをPythonモジュールのパスに追加
import json

def get_modules(generator, messages):
    '''
    タスクに必要なモジュールを取得
    :param client: OpenAIクライアント
    :param text: タスクの説明
    :return: タスクに必要なモジュール
    モジュールの正しい形式は以下の通りです:
    {
        background: bool,
        command: bool,
        suggesstion: bool,
        goal: bool,
        examples: bool,
        constraints: bool,
        workflow: bool,
        output_format: bool,
        skills: bool,
        style: bool,
        initialization: bool
    }
    '''
    default_modules = {
        "background": True,
        "command": False,
        "suggesstion": False,
        "goal": True,
        "examples": False,
        "constraints": True,
        "workflow": True,
        "output_format": True,
        "skills": False,
        "style": False,
        "initialization": True
    }
    ## タスクに必要なモジュールを生成
    messages = [
        {"role": "system", "content": "あなたはユーザーが与えたタスクの種類を分析し、そのタスクを完全に記述するために必要なモジュール（例: 背景、目標、制約、コマンド、提案、タスクのサンプル、ワークフロー、出力フォーマット、スキル、スタイル、初期設定など）を提示する必要があります。json形式で出力し、各モジュールが必要かどうかをTrueまたはFalseで表してください。例えば、背景、スキル、ワークフロー、出力フォーマット、初期設定が必要な場合、フォーマットは次のようになります：{\"background\": True, \"command\": False, \"suggesstion\": False, \"goal\": False, \"examples\": False, \"constraints\": False, \"workflow\": True, \"output_format\": True, \"skills\": True, \"style\": False, \"initialization\": True}"},
    ] + messages
    response = generator.generate_response(messages).replace("```", "").replace("\n", "").replace("json", "").replace(" ", "").replace("True", "true").replace("False", "false")

    for i in range(5):
        ## モジュールのフォーマットが正しいかどうかを確認
        try:
            ## モジュールを読み込む
            print(response)
            modules = json.loads(response)
            ## モジュールに欠けている部分や余計な部分がないか確認
            for key in ["background", "command", "suggesstion", "goal", "examples", "constraints", "workflow", "output_format", "skills", "style", "initialization"]:
                if key not in modules:
                    modules[key] = False
                pass
            extra_keys = []
            for key in modules.keys():
                if key not in ["background", "command", "suggesstion", "goal", "examples", "constraints", "workflow", "output_format", "skills", "style", "initialization"]:
                    extra_keys.append(key)
                pass
            for key in extra_keys:
                del modules[key]
            return modules
        except Exception as e:
            print(e)
            continue
    ## フォーマットが正しくない場合、デフォルトのモジュールを返す
    return default_modules
