import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


def send_email(content):
    """
    功能：把 HTML 內容寄到指定 email

    步驟：
    1. 建立 email message
    2. 設定 subject / from / to
    3. 連接 Gmail SMTP server
    4. 登入
    5. 發送
    6. 關閉連線
    """

    # 建立 HTML email
    msg = MIMEText(content, "html")
    msg["Subject"] = "📊 Daily Financial Digest"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = os.getenv("TO_EMAIL")

    # 連接 Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # 啟用 TLS 加密

    # 登入 Gmail（用 app password）
    server.login(
        os.getenv("EMAIL_USER"),
        os.getenv("EMAIL_PASS")
    )

    # 發送 email
    server.send_message(msg)

    # 關閉連線
    server.quit()