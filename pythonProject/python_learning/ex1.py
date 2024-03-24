name = 'aac'
stock_code = '003032'
stock_price = 19.99
stock_price_daily_growth_factor = 1.2
growth_days = 7
grown_price = stock_price * (stock_price_daily_growth_factor ** growth_days)
print(f"公司名称为{name},股票代码为{stock_code},当前股价为{stock_price}")
print("每日增长系数为%2.1f，经过%d天的增长后，股价达到了%4.2f"%(stock_price_daily_growth_factor,growth_days,grown_price))