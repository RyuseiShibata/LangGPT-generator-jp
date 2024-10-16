# Minstrel
Minstrelは、LangGPTフォーマットに基づいた構造化されたプロンプトを生成するためのマルチエージェントシステムです。このプロジェクトは、複数のインテリジェントエージェントが協力して高品質なLangGPTプロンプトを生成し、生成されるテキストの正確性と多様性を向上させることを目的としています。

# 機能
複数エージェントが協力してLangGPTプロンプトを生成
効率的なプロンプト生成アルゴリズム
拡張とカスタマイズが容易

# インストール
以下の手順に従って、このプロジェクトをインストールして実行してください。

1. プロジェクトリポジトリをクローン：
```bash
git clone https://github.com/RyuseiShibata/LangGPT-generator-jp.git
cd LangGPT-generator-jp
```

2. 仮想環境を作成して有効化（任意ですが推奨）：
```bash
conda create -n langgpt python=3.10 -y
conda activate langgpt
```

3. 依存関係をインストール：
```bash
pip install openai==1.37.1
pip install streamlit==1.37.0
```

4. 使用方法
```bash
python -m streamlit run app.py
```

