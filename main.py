stocks = { "AAPL" : 169.69, "GME" : 19.29, "GOOGL" : 107.34, "AMZN" : 105.45, "TSLA" : 164.31 , \
"MSFT" : 307.26, "NVDA" : 277.49, "META" : 240.32, "AMD" : 89.37 , "NFLX" : 329.93}

ticker = input('Enter a ticker symbol (e.g. GME). Type QUIT to stop: ')
while not ticker == "QUIT":
  if ticker in stocks:
    print('{} : {}'.format(ticker, stocks[ticker]))
  else:
    print('{} not found'.format(ticker))

  ticker = input('Enter a ticker symbol (e.g. GME). Type QUIT to stop: ')