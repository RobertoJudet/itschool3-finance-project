import yfinance


class Asset:
    def __init__(self, ticker: str, nr: float, name: str, country: str, sector: str):
        self.__ticker = ticker
        self.__nr = nr
        self.__name = name
        self.__country = country
        self.__sector = sector
        self.__yfin = yfinance.Ticker(ticker)

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
        price = self.fast_info()["lastPrice"]
        return round(price, 2)

    def fast_info(self):
        return self.__yfin.fast_info

    @property
    def currency(self) -> str:
        return self.fast_info()["currency"]

    @property
    def close_price(self) -> float:
        return self.__yfin.fast_info["previousClose"]

    @property
    def fifty_day_price(self) -> float:
        return self.__yfin.fast_info["fiftyDayAverage"]

    @property
    def today_low_price(self) -> float:
        return self.__yfin.fast_info["dayLow"]

    @property
    def today_high_price(self) -> float:
        return self.__yfin.fast_info["dayHigh"]

    @property
    def open_price(self) -> float:
        return self.__yfin.fast_info["open"]

    @property
    def evolution(self):
        evolution = (
            self.__yfin.fast_info["lastPrice"] - self.__yfin.fast_info["previousClose"]
        ) / self.__yfin.fast_info["previousClose"]
        return evolution

    # TODO extract the call self.__yfin.fast_info to not have duplicate code

    # TODO a property, in percentage how much it went up or down
    # current_price & closed_price

