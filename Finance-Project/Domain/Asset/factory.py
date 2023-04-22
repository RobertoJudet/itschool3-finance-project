import yahooquery
from Domain.Asset.asset import Asset


class AssetFactory:
    def make_new(self, ticker: str) -> Asset:
        t = yahooquery.Ticker(ticker)
        profile = t.summary_profile[ticker]
        name = profile["longBusimessSumary"].split(" ")[0:2]
        country = profile["country"]
        sector = profile["sector"]
        return Asset(
            ticker=ticker,
            nr=0,
            name=name,
            country=country,
            sector=sector,
        )
