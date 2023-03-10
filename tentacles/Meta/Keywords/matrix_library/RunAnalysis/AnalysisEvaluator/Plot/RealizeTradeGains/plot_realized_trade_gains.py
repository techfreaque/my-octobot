#  Drakkar-Software OctoBot-Trading
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
from tentacles.Meta.Keywords.matrix_library.RunAnalysis.BaseDataProvider.default_base_data_provider import (
    base_data_provider,
)


async def plot_realized_trade_gains(
    run_data: base_data_provider.RunAnalysisBaseDataGenerator,
    plotted_element,
    x_as_trade_count: bool = True,
    own_yaxis: bool = False,
):
    await run_data.load_realized_pnl(x_as_trade_count)
    plotted_element.plot(
        kind="bar",
        x=run_data.realized_pnl_x_data,
        y=run_data.realized_pnl_trade_gains_data,
        x_type="tick0" if x_as_trade_count else "date",
        title="Realized gains per trade",
        own_yaxis=own_yaxis,
    )
