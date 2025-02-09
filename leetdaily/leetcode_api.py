import requests

LEETCODE_GRAPHQL_URL = "https://leetcode.com/graphql"

def get_daily_problem():
    """Fetch the daily LeetCode problem."""
    query = """
    query questionOfToday {
        activeDailyCodingChallengeQuestion {
            date
            link
            question {
                title
                difficulty
                content  # Problem description in HTML format
            }
        }
    }
    """
    response = requests.post(LEETCODE_GRAPHQL_URL, json={"query": query})
    if response.status_code == 200:
        data = response.json()
        return data['data']['activeDailyCodingChallengeQuestion']
    else:
        raise Exception(f"Failed to fetch daily problem: {response.status_code}")