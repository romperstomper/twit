import twitter
consumer_key='JLhu3rnTDDKn23DPUun8mw'
consumer_secret='JKZ3BEnTo25UfSrEDlfsR4iOr0V7jLq8hKCzbJPeOI'

access_token='420980366-GuUezqbdLzbmAfcReMgQB4B7BgrJz2aqy8Zvayay'
access_secret='gCcgncQiS7xGbtYthdIxg7y8yqL0vYj4EtfXR5Dr33zrS'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_secret)


print(api.VerifyCredentials())