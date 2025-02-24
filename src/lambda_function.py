import os
import json
import datetime
from github_api import get_today_contributions
from notifier import send_notification

# 環境変数から設定を取得
USERNAME = os.getenv("GITHUB_USERNAME", "yuutom")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
LINE_NOTIFY_TOKEN = os.getenv("LINE_NOTIFY_TOKEN")


def lambda_handler(event, context):
    today = datetime.date.today().isoformat()
    contributions = get_today_contributions(USERNAME, GITHUB_TOKEN, today)

    if contributions == 0:
        message = "今日のGitHub Contributionがまだありません！"
        send_notification(LINE_NOTIFY_TOKEN, message)

    return {
        "statusCode": 200,
        "body": json.dumps({"date": today, "contributions": contributions})
    }
