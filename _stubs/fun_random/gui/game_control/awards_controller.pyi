# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/game_control/awards_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from fun_random.gui.feature.util.fun_mixins import FunProgressionWatcher as FunProgressionWatcher
from fun_random.gui.fun_gui_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from fun_random.gui.impl.lobby.common.lootboxes import FEP_CATEGORY as FEP_CATEGORY, FunRandomLootBoxTypes as FunRandomLootBoxTypes
from fun_random.gui.shared.event_dispatcher import showFunRandomLootBoxAwardWindow as showFunRandomLootBoxAwardWindow
from gui.game_control.AwardController import ServiceChannelHandler as ServiceChannelHandler
from gui.server_events.bonuses import getMergedCompensatedBonuses as getMergedCompensatedBonuses
from helpers import dependency as dependency
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages

class FunProgressionQuestsHandler(ServiceChannelHandler, FunProgressionWatcher):
    __systemMessages: Any
    _CLIENT_MSG_TYPE = SCH_CLIENT_MSG_TYPE.FUN_RANDOM_PROGRESSION
    def __init__(self, awardCtrl):
        ...
    def _showAward(self, ctx):
        ...
    def _needToShowAward(self, ctx):
        ...

class FunRandomLootBoxAutoOpenHandler(ServiceChannelHandler, FunProgressionWatcher):
    __systemMessages: Any
    __lootBoxData: Any
    def __init__(self, awardCtrl):
        ...
    def fini(self):
        ...
    def _showAward(self, ctx):
        ...
    def __showAward(self):
        ...
    def __onItemCacheSyncCompleted(self, *_):
        ...

def _getMessage(ctx):
    ...
