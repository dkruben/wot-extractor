# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/header_helpers/quest_flags_getters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.flag_constants import QuestFlagTypes as QuestFlagTypes
from gui.shared.system_factory import collectQuestFlags as collectQuestFlags
from shared_utils import findFirst as findFirst
from gui.Scaleform.daapi.view.lobby.hangar.header_helpers.base_flags import IQuestsFlag as IQuestsFlag
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle

class IQuestFlagsGetter(object):
    @classmethod
    def getVO(cls, vehicle, params=None):
        ...
    @classmethod
    def showQuestsInfo(cls, questType, questID):
        ...

class BaseQuestFlagsGetter(IQuestFlagsGetter):
    _SUPPORTED_FLAGS: tuple
    _ALL_QUEST_FLAGS = None
    @classmethod
    def getVO(cls, vehicle, params=None):
        ...
    @classmethod
    def showQuestsInfo(cls, questType, questID):
        ...
    @classmethod
    def _isQuestFlagsVisible(cls):
        ...
    @classmethod
    def __getAllQuestFlags(cls):
        ...

class DefaultQuestFlagsGetter(BaseQuestFlagsGetter):
    _SUPPORTED_FLAGS: tuple

class RankedQuestFlagsGetter(BaseQuestFlagsGetter):
    _SUPPORTED_FLAGS: tuple

class MapboxQuestFlagsGetter(BaseQuestFlagsGetter):
    _SUPPORTED_FLAGS: tuple
