from tentacles.Meta.Keywords import *


async def script(ctx: Context):
    activated_trade_analysis = True
    if activated_trade_analysis:
        await trade_analysis.plot_orders(ctx, None)
        await trade_analysis.plot_current_position(ctx, None)
        await trade_analysis.plot_average_entry(ctx, None)
        await trade_analysis.plot_balances(ctx, None)
