# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/marathon/marathon_constants.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/marathon/marathon_constants.py
from gui.impl.gen import R
from helpers.time_utils import ONE_DAY, ONE_HOUR
from shared_utils import CONST_CONTAINER
ZERO_TIME = 0.0
TIME_FORMAT_DAYS = 'days'
TIME_FORMAT_HOURS = 'hours'
TIME_FORMAT_TO_TIME_UNIT = {TIME_FORMAT_DAYS: ONE_DAY, 
   TIME_FORMAT_HOURS: ONE_HOUR}
R_BUYING_PANEL = R.strings.marathon.vehiclePreview.buyingPanel
R_TITLE_TOOLTIP = R.strings.marathon.vehiclePreview.title.tooltip
BUYING_BUTTON_ICON_ALIGN = 'right'
TOKEN_COUNT_INDEX = 1
MISSION_TAB_FORMAT = 'MISSIONS_TAB_{}'
AWARD_TOKENS_FORMAT = '{}{}'

class MarathonState(CONST_CONTAINER):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 3
    SUSPENDED = 4
    DISABLED = 5
    UNKNOWN = 6
    ENABLED_STATE = (NOT_STARTED, IN_PROGRESS, FINISHED)
    DISABLED_STATE = (SUSPENDED, DISABLED, UNKNOWN)


class MarathonWarning(CONST_CONTAINER):
    WRONG_VEH_TYPE = 'veh_type'
    WRONG_BATTLE_TYPE = 'battle_type'
    NONE = ''


class MarathonFlagTooltip(CONST_CONTAINER):
    from gui.marathon.marathon_header_tooltips import BaseTooltip, ProgressHeaderTooltip, CountdownHeaderTooltip, SimpleTextHeaderTooltip
    BASE = BaseTooltip
    COUNTDOWN = CountdownHeaderTooltip
    PROGRESS = ProgressHeaderTooltip
    TEXT = SimpleTextHeaderTooltip
