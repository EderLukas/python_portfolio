import requests
from datetime import datetime, timedelta
from env import SE_API_KEY, NE_API_KEY, ACCOUNT_SID, AUTH_TOKEN, FROM_PHONE, TO_PHONE
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

date_yesterday = (datetime.now() - timedelta(1)).strftime("%Y-%m-%d")
date_before_yesterday = (datetime.now() - timedelta(2)).strftime("%Y-%m-%d")

# Get Stock data from API endpoint https://www.alphavantage.co/query
params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": SE_API_KEY,
}
stock_response = requests.get(STOCK_ENDPOINT, params)
stock_response.raise_for_status()

stocks_last_two_days = {}
for day, values in stock_response.json()["Time Series (Daily)"].items():
    if day == date_yesterday or day == date_before_yesterday:
        stocks_last_two_days[day] = values

# work out if the stocks value has risen or fallen 5%
stock_value_yesterday = float(stocks_last_two_days[date_yesterday]["4. close"])
stock_value_before_yesterday = float(stocks_last_two_days[date_before_yesterday]["4. close"])
difference = abs(stock_value_yesterday - stock_value_before_yesterday)

percentage = difference * 100 / stock_value_yesterday

if difference > 5:

    # Get the 3 first articles from news endpoint Use https://newsapi.org/docs/endpoints/everything
    params = {
        "q": COMPANY_NAME,
        "from": date_yesterday,
        "sortBy": "popularity",
        "apiKey": NE_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params)
    news_response.raise_for_status()

    three_latest_articles = [article for article in news_response.json()["articles"]][:3]

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
            body=f"Stock change ratio {difference}%\n\n"
                 f"Headline:\t{three_latest_articles[0]['title']}\n"
                 f"Brief:\t{three_latest_articles[0]['description']}\n\n"
                 f"Headline:\t{three_latest_articles[1]['title']}\n"
                 f"Brief:\t{three_latest_articles[1]['description']}\n\n"
                 f"Headline:\t{three_latest_articles[2]['title']}\n"
                 f"Brief:\t{three_latest_articles[2]['description']}",
            from_=FROM_PHONE,
            to=TO_PHONE
        )
