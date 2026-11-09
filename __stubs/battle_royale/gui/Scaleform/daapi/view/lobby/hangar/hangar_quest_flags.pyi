# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/lobby/hangar/hangar_quest_flags.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from battle_royale.gui.Scaleform.daapi.view.lobby.hangar_constants import QuestFlagTypes as QuestFlagTypes
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.genConsts.HANGAR_HEADER_QUESTS import HANGAR_HEADER_QUESTS as HANGAR_HEADER_QUESTS
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags import BattleQuestsFlag as BattleQuestsFlag
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.flag_helpers import getActiveQuestLabel as getActiveQuestLabel
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.quest_flags_getters import BaseQuestFlagsGetter as BaseQuestFlagsGetter
from gui.server_events.events_constants import BATTLE_ROYALE_GROUPS_ID as BATTLE_ROYALE_GROUPS_ID
from gui.server_events.events_dispatcher import showMissionsCategories as showMissionsCategories
from gui.shared.formatters import icons as icons
from gui.shared.system_factory import registerQuestFlag as registerQuestFlag
from helpers import time_utils as time_utils, dependency as dependency
from helpers.time_utils import ONE_DAY as ONE_DAY
from skeletons.gui.game_control import IBattleRoyaleController as IBattleRoyaleController

class BattleRoyaleQuestFlagsGetter(BaseQuestFlagsGetter):
    _SUPPORTED_FLAGS: tuple

class _BattleRoyaleQuestsFlag(BattleQuestsFlag):
    __slots__: tuple
    _QUEST_TYPE = HANGAR_HEADER_QUESTS.QUEST_TYPE_BATTLE_ROYALE
    __battleRoyaleController: Any
    @classmethod
    def showQuestsInfo(cls, questType, _):
        ...
    @classmethod
    def _getLabelAndFlagType(cls, totalCount, completedQuests):
        ...

def registerQuestFlags():
    ...
