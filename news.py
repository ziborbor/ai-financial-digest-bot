import feedparser
print("🔥 NEWS.PY IS LOADED")

# 定義要抓的 RSS 來源
# 這裡選了美股 + 財經新聞網站
RSS_FEEDS = [
    "https://feeds.finance.yahoo.com/rss/2.0/headline?s=^GSPC&region=US&lang=en-US",
    "https://www.cnbc.com/id/100003114/device/rss/rss.html",
]


def fetch_news(limit=5):
    """
    功能：從多個 RSS feed 抓最新新聞

    步驟：
    1. 逐個 RSS feed 讀取
    2. 解析 feed entries
    3. 取前 N 條新聞
    4. 統一格式輸出（title / summary / link）

    return:
        list[dict]
    """
    articles = []

    for url in RSS_FEEDS:
        feed = feedparser.parse(url)  # 把 RSS XML 解析成 Python object

        for entry in feed.entries[:limit]:
            articles.append({
                "title": entry.title,               # 標題
                "summary": entry.get("summary", ""),# 摘要（有些RSS可能沒有）
                "link": entry.link                 # 原文連結
            })

    return articles