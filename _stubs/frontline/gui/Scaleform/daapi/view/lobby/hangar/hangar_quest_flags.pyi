# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/hangar/hangar_quest_flags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frontline.gui.gui_constants import QuestFlagTypes as QuestFlagTypes
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS as HANGAR_HEADER_QUESTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.flag_helpers import getActiveQuestLabel as getActiveQuestLabel, headerQuestFormatterVo as headerQuestFormatterVo, wrapQuestGroup as wrapQuestGroup
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags_getters import BaseQuestFlagsGetter as BaseQuestFlagsGetter
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags import BattleQuestsFlag as BattleQuestsFlag
from gui.shared.formatters import icons as icons
from gui.shared.system_factory import registerQuestFlag as registerQuestFlag
from helpers import time_utils as time_utils, dependency as dependency
from helpers.time_utils import ONE_DAY as ONE_DAY
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController

class EpicQuestFlagsGetter(BaseQuestFlagsGetter):
    _SUPPORTED_FLAGS: tuple

class _EpicQuestsFlag(BattleQuestsFlag):
    __slots__: tuple
    __epicController: Any
    @classmethod
    def formatQuests(cls, vehicle, params):
        ...

def registerQuestFlags():
    ...
