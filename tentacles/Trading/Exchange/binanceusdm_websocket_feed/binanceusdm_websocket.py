#  Drakkar-Software OctoBot-Tentacles
#  Copyright (c) Drakkar-Software, All rights reserved.
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  This library is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public
#  License along with this library.
import octobot_trading.exchanges as exchanges
from octobot_trading.enums import WebsocketFeeds as Feeds
import tentacles.Trading.Exchange.binanceusdm.binanceusdm_exchange as binanceusdm_exchange


class BinanceUsdMCCXTWebsocketConnector(exchanges.CCXTWebsocketConnector):
    EXCHANGE_FEEDS = {
        Feeds.TRADES: False,
        Feeds.KLINE: False,
        # needs to fetch funding rate as well to get funding and mark price
        Feeds.TICKER: False, 
        Feeds.CANDLE: False,
    }

    @classmethod
    def get_name(cls):
        return binanceusdm_exchange.BinanceUsdM.get_name()

    def get_adapter_class(self, adapter_class):
        return binanceusdm_exchange.BinanceUsdMAdapter
