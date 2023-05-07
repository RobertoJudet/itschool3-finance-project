import yfinance
class Asset:
    def __init__(self, ticker: str, nr: float, name: str, country: str, sector: str):
        self.__ticker = ticker
        self.__nr = nr
        self.__name = name
        self.__country = country
        self.__sector = sector
        yfin = yfinance.Ticker(ticker)
        self.__info = yfin.fast_info

    @property
    def ticker(self) -> str:
        return self.__ticker

    @property
    def units(self) -> float:
        return self.__nr

    @property
    def name(self) -> str:
        return self.__name

    @property
    def country(self) -> str:
        return self.__country

    @property
    def current_price(self) -> float:
        price = self.__info["lastPrice"]
        return round(price, 2)

    @property
    def currency(self) -> str:
        return self.__info["currency"]

    @property
    def today_low_price(self) -> float:
        price = self.__info["dayLow"]
        return round(price, 2)

    @property
    def today_high_price(self) -> float:
        price = self.__info["dayHigh"]
        return round(price, 2)

    @property
    def open_price(self) -> float:
        price = self.__info["open"]
        return round(price, 2)

    @property
    def closed_price(self) -> float:
        price = self.__info["previousClose"]
        return round(price, 2)

    @property
    def fifty_day_price(self) -> float:
        price = self.__info["fiftyDayAverage"]
        return round(price, 2)

    @property
    def price_change_percent(self):
        price = ((self.__info["lastPrice"] - self.__info["previousClose"]) / self.__info[
            'previousClose']) * 100
        return f"{round(price, 2)}%"
