import requests
from datetime import date,timedelta
frome twilio.rest import client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILIO_SID= "your sid"
TWILIO_AUTH_TOKEN= "your auth token"
NEWS_API_KEY="your api key"
MY_NUMBER="your number"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_endpoint="https://www.alphavantage.co/query?"
NEWS_ENDPOINT="https://newsapi.org/v2/top-headlines/sources?"
TWILIO_ENDPOINT="https://api.twilio.com/2010-04-01/Accounts?"
parameter={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API,
}
response=requests.get(stock_endpoint,params=parameter)
response_stock=response.json()
yesterday=date.today()-timedelta(days=1)
dyesterday=date.today()-timedelte(days=2)
yesterday_str=str(yesterday)
yes_close=response_stock["Time Series (Daily)"][yesterday_str]["4. close"]
dyes_close=response_stock["Time Series (Daily)"][dyesterday_str]["4. close"]
difference=abs(float(yes_close)-float(dyes_close))
diff_percent=(difference/float(yesterday_closing_price)*100)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if diff_percent>5:
    news_params={
        "apikey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
    }
news_response=request.get(NEWS_ENDPOINT,params=news_params)
articles=news_response.json()["articles"]
three_articles=articles[:3]
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
formatted_articles=[f"Headline:{article['title']}.\nBrief:{article['description']}"for article in three_article]
client=client(TWILIO_SID,TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message =client.messages.create(
        body=article,
        from="334535"
        to="MY_NUMBER"
    )
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

