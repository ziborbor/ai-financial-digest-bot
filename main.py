import json
from news import fetch_news
from llm import summarize_news
from emailer import send_email


def build_email(news_items):
    """
    功能：把所有新聞組裝成 HTML email

    流程：
    1. 初始化 HTML header
    2. 每則新聞 → 丟給 AI
    3. 解析 AI JSON
    4. 組成 HTML block
    5. return 完整 email
    """

    html = "<h1>📊 Daily Financial Digest</h1>"

    for n in news_items:

        # 用 AI 分析單一新聞
        ai_output = summarize_news(n)

        # 嘗試把 AI output 轉成 JSON
        try:
            data = json.loads(ai_output)
        except:
            # 如果 AI 沒照規則輸出，就 fallback
            data = {
                "summary": ai_output,
                "market": "N/A",
                "category": "Other",
                "impact_score": 3
            }

        # 加入 HTML email
        html += f"""
        <hr>

        <h3>{n['title']}</h3>

        <p><b>Summary:</b> {data['summary']}</p>

        <p><b>Market Impact:</b> {data['market']}</p>

        <p><b>Category:</b> {data['category']}</p>

        <p><b>Impact Score:</b> {data['impact_score']}/5</p>

        <a href="{n['link']}">Read original</a>
        """

    return html


def main():
    """
    主流程（整個 bot 的 entry point）

    步驟：
    1. 抓新聞
    2. AI 分析
    3. 組 email
    4. 發送 email
    """
    print("NEWS FILE:")
    #print("DIR:", dir(news))
    RetrievedNews = fetch_news()              # step 1
    email_content = build_email(RetrievedNews) # step 2
    send_email(email_content)        # step 3

    print("✅ Daily Digest sent!")


if __name__ == "__main__":
    main()