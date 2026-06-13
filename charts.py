import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from networth_tracker import load_networth_history


# ---------------------------------------------------------
# helper: matplotlib figure → base64 string
# 用途：讓 image 可以直接 embed 在 HTML email
# ---------------------------------------------------------
def fig_to_base64(fig):
    """
    Convert matplotlib figure to base64 string
    so it can be embedded in HTML <img> tag.
    """
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)

    return base64.b64encode(buf.read()).decode("utf-8")


# ---------------------------------------------------------
# PIE CHART: portfolio allocation
# ---------------------------------------------------------
def build_pie_chart(allocation_percent):
    """
    Input:
        allocation_percent = {
            "Stocks": 40,
            "Crypto": 10,
            "Cash": 50
        }

    Output:
        base64 PNG image
    """

    fig, ax = plt.subplots()

    labels = list(allocation_percent.keys())
    sizes = list(allocation_percent.values())

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    ax.set_title("Portfolio Allocation")
    #Convert to PNG bytes because base64 didn't work
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    png_bytes = buf.read()
    plt.close(fig)   # ⭐ fix

    return png_bytes


# ---------------------------------------------------------
# LINE CHART: net worth history
# ---------------------------------------------------------
def build_networth_line_chart():
    """
    Reads CSV history and builds a net worth time series chart.
    """

    history = load_networth_history()

    # no data safety check
    if not history:
        return ""

    df = pd.DataFrame(history)

    # convert types
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["net_worth_nzd"] = df["net_worth_nzd"].astype(float)

    # sort to ensure correct line order
    df = df.sort_values("timestamp")

    fig, ax = plt.subplots()

    ax.plot(
        df["timestamp"],
        df["net_worth_nzd"],
        marker="o"
    )

    ax.set_title("Net Worth Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("NZD")

    # rotate x labels for readability
    plt.xticks(rotation=45)

    ax.grid(True, alpha=0.3)


    #Convert to PNG bytes because base64 didn't work
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    png_bytes = buf.read()
    plt.close(fig)   # ⭐ fix


    return png_bytes