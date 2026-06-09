import os
from openai import OpenAI
from dotenv import load_dotenv
print("🔥 LLM.PY IS LOADED")

load_dotenv()  # 載入 .env 裡的 API key

# 初始化 OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_news(article):
    """
    功能：用 AI 讀一則新聞，輸出結構化分析

    input:
        article = {
            title,
            summary,
            link
        }

    AI 做的事：
    1. 總結新聞
    2. 判斷市場影響
    3. 分類（AI / Macro / Stocks / Crypto）
    4. 給 impact score (1-5)

    return:
        string (JSON format)
    """

    prompt = f"""
You are a financial analyst.

Return STRICT JSON ONLY:

{{
  "summary": "...",
  "market": "...",
  "category": "AI | Macro | Stocks | Crypto | Other",
  "impact_score": 1-5
}}

News:
Title: {article['title']}
Content: {article['summary']}
"""

    # 呼叫 GPT 做分析
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text