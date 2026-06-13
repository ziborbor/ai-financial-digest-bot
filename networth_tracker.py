import csv
from datetime import datetime
import pytz
import os

CSV_FILE = "networth_history.csv"


def log_networth(total_net_worth, market_condition):
    """
    Append today's net worth snapshot into CSV
    """

    tz = pytz.timezone("Pacific/Auckland")
    today = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.isfile(CSV_FILE)
    print("file_exists?")
    print(file_exists)
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        # write header if file is new
        if not file_exists:
            writer.writerow(["timestamp", "net_worth_nzd", "market_condition"])

        writer.writerow([today, total_net_worth, market_condition])


def load_networth_history():
    """
    Read full history for reporting / charts
    """
    if not os.path.exists(CSV_FILE):
        return []

    with open(CSV_FILE, "r") as f:
        return list(csv.DictReader(f))
    

#Today vs Yesterday
def get_latest_change():
    history = load_networth_history()
    if len(history) < 2:
        return None

    last = float(history[-1]["net_worth_nzd"])
    prev = float(history[-2]["net_worth_nzd"])

    diff = last - prev
    pct = (diff / prev) * 100 if prev != 0 else 0

    return diff, pct