import os
import json
import datetime
from github_api import get_today_contributions
from notifier import send_message

# 環境変数から設定を取得
USERNAME = os.getenv("GITHUB_USERNAME", "yuutom")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
CHANNEL_ACCESS_TOKEN = os.getenv("CHANNEL_ACCESS_TOKEN")
USER_ID = os.getenv("USER_ID")


def lambda_handler(event, context):
    today = datetime.date.today().isoformat()
    contributions = get_today_contributions(USERNAME, GITHUB_TOKEN, today)
    print(contributions)

    # if contributions == 0:
    message = "no contribution today！"
    send_message(CHANNEL_ACCESS_TOKEN, USER_ID, message)

    return {
        "statusCode": 200,
        "body": json.dumps({"date": today, "contributions": contributions})
    }
