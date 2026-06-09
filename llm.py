import os
from openai import OpenAI
from dotenv import load_dotenv
print("🔥 LLM.PY IS LOADED")

load_dotenv()  # 載入 .env 裡的 API key

# 初始化 OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_news(article, user_profile):
    """
    把新聞變成「對你個人有意義的金融分析」
    """

    prompt = f"""
You are a PERSONAL FINANCIAL AI ADVISOR.

Your job:
- Analyze news impact on the user
- Focus ONLY on relevance to user's portfolio and situation
- Be conservative (no hype)

USER PROFILE:
{user_profile}

NEWS:
Title: {article['title']}
Content: {article['summary']}

Return STRICT JSON:

{{
  "relevance_score": 1-5,
  "category": "AI / Macro / Stocks / Crypto / Property / Other",
  "summary": "short summary",
  "portfolio_impact": "how it affects user's holdings or net worth",
  "action": "Buy / Sell / Hold / Monitor / Ignore",
  "action_reason": "why this action",
  "risk_level": "low / medium / high"
}}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text
