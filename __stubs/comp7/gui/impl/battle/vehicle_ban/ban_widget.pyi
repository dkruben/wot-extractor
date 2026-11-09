# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from PlayerEvents import g_playerEvents as g_playerEvents
from ReplayEvents import g_replayEvents as g_replayEvents
from comp7.gui.impl.battle.vehicle_ban.ban_helpers import fillComp7VehicleModel as fillComp7VehicleModel, getOwnDatabaseID as getOwnDatabaseID
from comp7.gui.impl.gen.view_models.views.battle.ban_widget_model import BanWidgetModel as BanWidgetModel
from comp7.gui.impl.gen.view_models.views.battle.banned_vehicle_model import BannedVehicleModel as BannedVehicleModel
from comp7.gui.impl.gen.view_models.views.battle.enums import BanState as BanState, CandidateState as CandidateState
from comp7.gui.shared.event_dispatcher import showComp7VehicleBanWindow as showComp7VehicleBanWindow
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from comp7_core_constants import ArenaPrebattlePhase as ArenaPrebattlePhase
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from skeletons.gui.shared import IItemsCache as IItemsCache
BAN_STATES_MAPPING: dict

class BanWidgetView(ViewImpl):
    __slots__: tuple
    __comp7Controller: Any
    __itemsCache: Any
    __sessionProvider: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *_, **__):
        ...
    def _finalize(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateData(self, model=None):
        ...
    def __setDefaultData(self, model):
        ...
    def __setCandidates(self, model):
        ...
    def __setResults(self, model):
        ...
    def __onOpen(self):
        ...
    def __onBanPhaseUpdated(self):
        ...
    def __onAvatarObserverVehicleChanged(self, *_):
        ...
    def __onConfigChanged(self):
        ...
    def __getVehicleBanCtrl(self):
        ...
    def __isVehicleBanEnabled(self):
        ...
    def __onReplayTimeWarpFinish(self):
        ...
