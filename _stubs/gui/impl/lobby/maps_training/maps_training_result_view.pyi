# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/maps_training_result_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import ArenaType as ArenaType
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_result_model import DoneValueEnum as DoneValueEnum, MapsTrainingResultModel as MapsTrainingResultModel
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared.event_dispatcher import showMapsTrainingPage as showMapsTrainingPage
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from skeletons.gui.battle_results import IBattleResultsService as IBattleResultsService
from skeletons.gui.game_control import IMapsTrainingController as IMapsTrainingController
from PlayerEvents import g_playerEvents as g_playerEvents
from maps_training_common.maps_training_constants import SCENARIO_INDEXES as SCENARIO_INDEXES
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_SECONDS_IN_MINUTE = 60

class MapsTrainingResultView(ViewImpl):
    __slots__: tuple
    battleResults: Any
    mapsTrainingController: Any
    hangarSpace: Any
    __arenaUniqueID: Any
    __isFromNotifications: Any
    __tooltipData: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __handleBattleResultsPosted(self, reusableInfo, _, __):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onClose(self):
        ...
    def __onDisconnected(self):
        ...
    def __onHangarSpaceCreated(self):
        ...
    def __setHangarReady(self):
        ...
    def __showMapsTrainingPage(self):
        ...
    def __setBattleResults(self):
        ...
    def __addRewards(self, model, vo):
        ...
    @staticmethod
    def __getDoneValue(vo):
        ...
    @staticmethod
    def __getDuration(vo):
        ...

class MapsTrainingResultWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
