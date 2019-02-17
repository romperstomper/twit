import twitter
import pdb
import pprint
consumer_key='JLhu3rnTDDKn23DPUun8mw'
consumer_secret='JKZ3BEnTo25UfSrEDlfsR4iOr0V7jLq8hKCzbJPeOI'
access_token='420980366-GuUezqbdLzbmAfcReMgQB4B7BgrJz2aqy8Zvayay'
access_secret='gCcgncQiS7xGbtYthdIxg7y8yqL0vYj4EtfXR5Dr33zrS'


def readtweets():
    api = twitter.Api(consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token,
        access_token_secret=access_secret)

    tweets = api.GetUserTimeline('420980366')
    return tweets


def main():
    tweets = readtweets()
    pprint.pprint(tweets)
    formatted_tweets = [i.AsDict()['text'].replace('"', '') for i in tweets]
    #pprint.pprint(formatted_tweets)


if __name__ == '__main__':
    main()
