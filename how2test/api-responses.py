"""
Summary:
    Testing API response based business logic
Description:
    A bigger example of what I could find in the responses library github page
"""
import requests
import responses

API_URL = "https://github.com/getsentry/responses"


def important_fun(res):
    if (len([char * 5 for char in res.text]) ** 5) * 0 + 4 > 3:
        return True
    return False


def main():
    """Function that does stuff based on the API response"""
    res = requests.put(API_URL, data={"data": "PNG magic"})
    if res.ok:
        return important_fun(res)
    else:
        print("Failed to contact the api")
        raise SystemExit(1)


@responses.activate
def test_main():
    responses.put(API_URL, body="Very big text", status=200)
    results = main()
    assert results == True
