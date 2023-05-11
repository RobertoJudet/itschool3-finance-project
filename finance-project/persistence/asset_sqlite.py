import sqlite3
import logging

from domain.asset.asset import Asset
from domain.asset.persistence_interface import AssetPersistenceInterface
from domain.user.user import User


class DuplicateAsset(Exception):
    pass


class AssetPersistenceSqlite(AssetPersistenceInterface):
    def add_to_user(self, user: User, asset: Asset):
        table = f"{user.id}-assets".replace("-", "_")
        with sqlite3.connect(f"main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    f"INSERT INTO '{table}' (ticker, name, country, units)"
                    f"VALUES ('{asset.ticker}', '{asset.name}', "
                    f"'{asset.country}', {asset.units})"
                )
                logging.info(
                    f"Successfully added asset {asset.ticker} to user {user.username}"
                )
            except sqlite3.IntegrityError as e:
                if "UNIQUE constraint failed" in str(e):
                    logging.warning(f"Asset <{asset.ticker}> already in database!")
                    raise DuplicateAsset(
                        f"Asset <{asset.ticker}> already in database! "
                    )
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    cursor.execute(
                        f"CREATE TABLE '{table}'"
                        f" (ticker TEXT PRIMARY KEY,"
                        f" name TEXT,"
                        f" country TEXT,"
                        f" units REAL)"
                    )
                    cursor.execute(
                        f"INSERT INTO '{table}' (ticker, name, country, units)"
                        f"VALUES ('{asset.ticker}', '{asset.name}', "
                        f"'{asset.country}', {asset.units})"
                    )
                conn.commit()

    def get_for_user(self, user: User) -> list[Asset]:
        table = f"{user.id}-assets".replace("-", "_")
        with sqlite3.connect(f"main_users.db") as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(f"SELECT * FROM '{table}'")
            except sqlite3.OperationalError as e:
                if "no such table" in str(e):
                    return []
                else:
                    raise e
            assets_info = cursor.fetchall()
        assets = [
            Asset(ticker=x[0], nr=x[3], name=x[1], country=x[2], sector="sec")
            for x in assets_info
        ]
        return assets