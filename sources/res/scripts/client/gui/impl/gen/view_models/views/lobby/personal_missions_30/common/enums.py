# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/common/enums.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/common/enums.py
from enum import Enum

class MissionCategory(Enum):
    ASSAULT = 'assault'
    SNIPER = 'sniper'
    SUPPORT = 'support'


class OperationState(Enum):
    COMPLETED_WITH_HONORS = 'completedWithHonors'
    COMPLETED = 'completed'
    ACTIVE = 'active'
    AVAILABLE = 'available'
    UNAVAILABLE = 'unavailable'
    LOCKED = 'locked'


class ParamTooltipType(Enum):
    PROGRESSION = 'progression'
    PM3_POINTS = 'pm3_points'
    CUSTOM_SIMPLE = 'custom_simple'
