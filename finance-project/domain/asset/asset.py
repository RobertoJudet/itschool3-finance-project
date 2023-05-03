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
        # print(self.__yfin.fast_info)

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
    def closed_price(self) -> float:
        return self.__info["previousClose"]

    @property
    def fifty_day_price(self) -> float:
        return self.__info["fiftyDayAverage"]

    @property
    def today_low_price(self) -> float:
        return self.__info["dayLow"]

    @property
    def today_high_price(self) -> float:
        return self.__info["dayHigh"]

    @property
    def open_price(self) -> float:
        return self.__info["open"]

    @property
    def up_or_down_percentage(self) -> float:
        x = self.__info["open"]
        y = self.__info["previousClose"]
        if x > y:
            return -x / y
        else:
            return x / y
