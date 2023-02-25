from octobot_tentacles_manager.api.inspector import check_tentacle_version
from octobot_commons.logging.logging_util import get_logger

if check_tentacle_version('1', 'trade_analysis', 'matrix-strategy-maker'):
    try:
        from .trade_analysis import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading trade_analysis: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')
