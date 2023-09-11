from portfolio import portfolio

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

print(portfolio.calculate_portfolio_value(stocks, prices))
print(portfolio.calculate_portfolio_return(10000, 15000))
print(portfolio.get_most_profitable_stock(stocks, prices))
