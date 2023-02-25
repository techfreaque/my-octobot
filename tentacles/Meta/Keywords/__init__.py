from octobot_tentacles_manager.api.inspector import check_tentacle_version
from octobot_commons.logging.logging_util import get_logger

if check_tentacle_version("2.0", "matrix_library", "matrix-strategy-maker"):
    try:
        from .matrix_library import *
    except Exception as e:
        get_logger("TentacleLoader").error(
            f"Error when loading matrix_library: "
            f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
            f"error persists, try reinstalling your tentacles via "
            f'"python start.py tentacles --install --all".'
        )
if check_tentacle_version("1.2.0", "scripting_library", "OctoBot-Private-Tentacles"):
    try:
        from .scripting_library import *
    except Exception as e:
        get_logger("TentacleLoader").error(
            f"Error when loading scripting_library: "
            f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
            f"error persists, try reinstalling your tentacles via "
            f'"python start.py tentacles --install --all".'
        )

if check_tentacle_version('1.2.0', 'scripting_library', 'OctoBot-Default-Tentacles'):
    try:
        from .scripting_library import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading scripting_library: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')

if check_tentacle_version('1.0', 'matrix_library', 'Matrix-Keywords-Bundle'):
    try:
        from .matrix_library import *
    except Exception as e:
        get_logger('TentacleLoader').error(f'Error when loading matrix_library: '
                                           f'{e.__class__.__name__}{f" ({e})" if f"{e}" else ""}. If this '
                                           f'error persists, try reinstalling your tentacles via '
                                           f'"python start.py tentacles --install --all".')
