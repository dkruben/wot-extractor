# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/training_room_external_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers import isDemonstrator as isDemonstrator, isDemonstratorExpert as isDemonstratorExpert
from comp7.gui.prb_control.entities.limits import Comp7TrainingLimits as Comp7TrainingLimits
from comp7.gui.prb_control.entities.pre_queue.vehicles_watcher import Comp7VehiclesWatcher as Comp7VehiclesWatcher
from constants import PREBATTLE_ERRORS as PREBATTLE_ERRORS, PREBATTLE_STATE as PREBATTLE_STATE
from gui.Scaleform.genConsts.BATTLE_TYPES import BATTLE_TYPES as BATTLE_TYPES
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES as PREBATTLE_ALIASES
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from gui.prb_control import prb_getters as prb_getters
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.training_room_external_handlers import TrainingRoomBaseHandler as TrainingRoomBaseHandler
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache

class Comp7TrainingRoomHandler(TrainingRoomBaseHandler):
    _GUI_TYPE_NAME = 'comp7'
    def getArenaFilter(self):
        ...
    def getArenaData(self):
        ...
    def getAdditionalInfo(self):
        ...
    def getIcon(self):
        ...
    def getMaxPlayersInTeam(self):
        ...
    def getObserverValidator(self):
        ...
    def playerReadyHandler(self, result):
        ...
    def getPrebattleLimits(self):
        ...
    def getPrebattlePropertyChecker(self):
        ...
    def getVehicleWatcherType(self):
        ...
    def getClientMessageData(self, errorType=None):
        ...
    def isEnabledForGuiTypeName(self, guiTypeName=None):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def _canBeComp7Observer(itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _getComp7MaxPlayersInTeam(comp7Controller=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def _isComp7ArenaFilter(arena, settings, comp7Controller=None):
    ...
def _shouldComp7PlayerStateBeValidated(propertyName):
    ...
