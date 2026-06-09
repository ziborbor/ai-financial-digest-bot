import json
from news import fetch_news
from llm import analyze_news
from emailer import send_email
from user_profile import USER_PROFILE


def build_email(news_items):
    html = "<h1>📊 Personal Financial Digest</h1>"

    for n in news_items:

        ai_output = analyze_news(n, USER_PROFILE)

        try:
            data = json.loads(ai_output)
        except:
            continue

        # filter：只顯示對你重要的
        if data.get("relevance_score", 0) < 3:
            continue

        html += f"""
        <hr>

        <h3>{n['title']}</h3>

        <p>📌 Summary: {data['summary']}</p>

        <p><b>Portfolio Impact:</b> {data['portfolio_impact']}</p>

        <p><b>Action:</b> {data['action']}</p>

        <p><b>Reason:</b> {data['action_reason']}</p>

        <p><b>Risk:</b> {data['risk_level']}</p>

        <p><b>Relevance:</b> {data['relevance_score']}/5</p>

        <a href="{n['link']}">Read original</a>
        """

    return html


def main():
    RetrievedNews = fetch_news()

    email_content = build_email(RetrievedNews)

    send_email(email_content)

    print("✅ Personal AI Digest sent!")


if __name__ == "__main__":
    main()