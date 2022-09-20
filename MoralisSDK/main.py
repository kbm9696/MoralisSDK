from chainlink import Chainlink


chain = Chainlink()
data = chain.active_feeds(limit=10)
print(data)