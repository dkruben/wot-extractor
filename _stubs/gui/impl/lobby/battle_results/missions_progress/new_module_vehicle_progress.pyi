# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_results/missions_progress/new_module_vehicle_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.daapi.view.lobby.techtree.data import ResearchItemsData as ResearchItemsData
from gui.battle_results.pbs_helpers.common import getBattleResults as getBattleResults
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.battle_results.missions_progress.progression_presenter_interface import IProgressionCategoryPresenter as IProgressionCategoryPresenter
from gui.impl.lobby.vehicle_hub.sub_presenters.modules_sub_presenter import ModulesTreeViewDumper as ModulesTreeViewDumper
from gui.impl.lobby.hangar.presenters.utils import GUINode as GUINode
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.gen.view_models.views.lobby.battle_results.progression.module_vehicle_progress_model import ModuleVehicleProgressModel as ModuleVehicleProgressModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.unlock_module_progress_model import UnlockModuleProgressModel as UnlockModuleProgressModel
from gui.impl.gen.view_models.views.lobby.battle_results.progression.unlock_vehicle_progress_model import UnlockVehicleProgressModel as UnlockVehicleProgressModel
from gui.shared import event_dispatcher as event_dispatcher, events as events
from gui.Scaleform.genConsts.CURRENCIES_CONSTANTS import CURRENCIES_CONSTANTS as CURRENCIES_CONSTANTS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.backport import createTooltipData as createTooltipData
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator

# base nao representavel no stub: ViewComponent[...]
class NewModuleVehicleProgressPresenter(IProgressionCategoryPresenter):
    __categoryProgressFilter: Any
    __arenaUniqueID: Any
    __vehicleIntCD: Any
    __progress: Any
    _data: Any
    def __init__(self, categoryProgressFilter, arenaUniqueID, *args, **kwargs):
        ...
    @classmethod
    def getPathToResource(cls):
        ...
    @classmethod
    def getViewAlias(cls):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def prepare(self):
        ...
    def finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _updateModel(self):
        ...
    def _updateProgress(self):
        ...
    def __onPremiumXpBonusChanged(self, event):
        ...
    # decorador original: @args2params(...)
    def __onNavigate(self, vehicleCD):
        ...
    def __createUnlockModule(self, item, unlockProps):
        ...
    def __createUnlockVehicle(self, item, unlockProps, avgBattlesTillUnlock):
        ...
