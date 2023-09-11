
_initial_portfolio_value = 10000


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _initial_portfolio_value
    total_value = 0
    for stock_symbol, quantity in stocks.items():
        if stock_symbol in prices:
            total_value += quantity * prices[stock_symbol]

    if _initial_portfolio_value is None:
        _initial_portfolio_value = total_value

    return total_value


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return ((current_value - initial_value) / initial_value) * 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    most_profitable_stock = None
    max_profit_percentage = float('-inf')

    for stock_symbol, quantity in stocks.items():
        if stock_symbol in prices:
            initial_value = calculate_portfolio_value(
                {stock_symbol: quantity}, prices)
            current_value = quantity * prices[stock_symbol]
            profit_percentage = calculate_portfolio_return(
                initial_value, current_value)

            if profit_percentage > max_profit_percentage:
                max_profit_percentage = profit_percentage
                most_profitable_stock = stock_symbol

    return most_profitable_stock


__all__ = ['calculate_portfolio_return',
           'calculate_portfolio_return', 'get_most_profitable_stock']
