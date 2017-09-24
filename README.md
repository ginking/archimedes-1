THIS WILL NEED TO BE EQUITY MANAGED, OTHERWISE SELL/BUY WILL GENERATE REDUCED/LOSS DRIVEN RETURNS AS IT'S BUILT TO SHORT THEN BUY AND SELL EOD WHICH IS NOT PEAK PERFORMANCE. 

THIS FOR US WAS PROOF OF CONCEPT EDITS/ENHANCEMENTS (FOREX SIDE REMOVED) AND WAS MANAGED BY A PROFESSIONAL TRADER PULLING THE FUNDS OR CLOSING OUT AT LOSS/GAIN THROUGHOUT EXPERIMENTATION PROCESS. 

PLEASE UNDERSTAND BY UTILISING THIS IN LIVE INVACIO, WILLIAM J D WEST OR OTHER DEVELOPERS MENTIONED THROUGHOUT THE LICENSE ARE NOT RESPONSIBLE FOR ANY LOSSES OBTAINED.

USE AT YOUR OWN RISK, PREFERABLY HAVE A ENGINEER GO THROUGH, EXPLAINING EACH ELEMENT AND ENHANCING TO YOUR OWN USES, PLEASE THEN ONLY UTILISE IF YOU ARE A ACCREDITED INVESTOR OR TRADER.

Archimedes 1 is a bot based sentient based trader, heavily influenced on forked existing bots, with a few enhancements here or there, this was completed to understand how the bots worked to roll the forward in our own manner to our own complete ai based trading system (Archimedes 2:0)

This bot watches [followed accounts] tweets and waits for them to mention any publicly traded companies. When they do, sentiment analysis is used determine whether the opinions are positive or negative toward those companies. The bot then automatically executes trades on the relevant stocks according to the expected market reaction. 

The code is written in Python and is meant to run on a Google Compute Engine instance. It uses the Twitter Streaming APIs (however new version) to get notified whenever tweets within remit are of interest. The entity detection and sentiment analysis is done using Google's Cloud Natural Language API and the Wikidata Query Service provides the company data. The TradeKing (ALLY) API does the stock trading (changed to ALLY).

The main module defines a callback where incoming tweets are handled and starts streaming user's feed:

def twitter_callback(tweet):
    companies = analysis.find_companies(tweet)
    if companies:
        trading.make_trades(companies)
        twitter.tweet(companies, tweet)

if __name__ == "__main__":
    twitter.start_streaming(twitter_callback)
The core algorithms are implemented in the analysis and trading modules. The former finds mentions of companies in the text of the tweet, figures out what their ticker symbol is, and assigns a sentiment score to them. The latter chooses a trading strategy, which is either buy now and sell at close or sell short now and buy to cover at close. The twitter module deals with streaming and tweeting out the summary.

Follow these steps to run the code yourself:

1. Create VM instance

Check out the quickstart to create a Cloud Platform project and a Linux VM instance with Compute Engine, then SSH into it for the steps below. The predefined machine type g1-small (1 vCPU, 1.7 GB memory) seems to work well.

2. Set up auth

The authentication keys for the different APIs are read from shell environment variables. Each service has different steps to obtain them.

Twitter

Log in to your Twitter account and create a new application. Under the Keys and Access Tokens tab for your app you'll find the Consumer Key and Consumer Secret. Export both to environment variables:

export TWITTER_CONSUMER_KEY="<YOUR_CONSUMER_KEY>"
export TWITTER_CONSUMER_SECRET="<YOUR_CONSUMER_SECRET>"
If you want the tweets to come from the same account that owns the application, simply use the Access Token and Access Token Secret on the same page. If you want to tweet from a different account, follow the steps to obtain an access token. Then export both to environment variables:

export TWITTER_ACCESS_TOKEN="<YOUR_ACCESS_TOKEN>"
export TWITTER_ACCESS_TOKEN_SECRET="<YOUR_ACCESS_TOKEN_SECRET>"
Google

Follow the Google Application Default Credentials instructions to create, download, and export a service account key.

export GOOGLE_APPLICATION_CREDENTIALS="/path/to/credentials-file.json"
You also need to enable the Cloud Natural Language API for your Google Cloud Platform project.

TradeKing (ALLY)

Log in to your TradeKing (ALLY account and create a new application. Behind the Details button for your application you'll find the Consumer Key, Consumer Secret, OAuth (Access) Token, and Oauth (Access) Token Secret. Export them all to environment variables:

export TRADEKING_CONSUMER_KEY="<YOUR_CONSUMER_KEY>"
export TRADEKING_CONSUMER_SECRET="<YOUR_CONSUMER_SECRET>"
export TRADEKING_ACCESS_TOKEN="<YOUR_ACCESS_TOKEN>"
export TRADEKING_ACCESS_TOKEN_SECRET="<YOUR_ACCESS_TOKEN_SECRET>"
Also export your TradeKing (ALLY) account number, which you'll find under My Accounts:

export TRADEKING_ACCOUNT_NUMBER="<YOUR_ACCOUNT_NUMBER>"
3. Install dependencies

There are a few library dependencies, which you can install using pip:

$ pip install -r requirements.txt
4. Run the tests

Verify that everything is working as intended by running the tests with pytest using this command:

$ export USE_REAL_MONEY=NO && pytest *.py --verbose
5. Run the benchmark

The benchmark report shows how the current implementation of the analysis and trading algorithms would have performed against historical data. You can run it again to benchmark any changes you may have made:

$ ./benchmark.py > benchmark.md
6. Start the bot

Enable real orders that use your money:

$ export USE_REAL_MONEY=YES
Have the code start running in the background with this command:

$ nohup ./main.py &

License


Archimedes (edits under Invacio) Max Braun Frame under Max Braun, licence under Apache V2 License.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


