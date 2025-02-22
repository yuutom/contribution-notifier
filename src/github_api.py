import requests

GITHUB_API_URL = "https://api.github.com/graphql"


def get_today_contributions(username, token, date):
    query = """
    {
      user(login: "%s") {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                date
                contributionCount
              }
            }
          }
        }
      }
    }
    """ % username

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(GITHUB_API_URL, json={"query": query}, headers=headers)
    data = response.json()

    if "errors" in data:
        raise Exception(f"GitHub API Error: {data['errors']}")

    contributions = sum(
        day["contributionCount"]
        for week in data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
        for day in week["contributionDays"]
        if day["date"] == date
    )

    return contributions
