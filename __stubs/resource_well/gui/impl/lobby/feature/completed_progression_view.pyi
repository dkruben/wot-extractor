# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/completed_progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from typing import Optional as Optional, Tuple as Tuple
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewImpl as ViewImpl
from gui.shared import g_eventBus as g_eventBus, events as events
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar
from helpers import dependency as dependency
from resource_well.gui.feature.resource_well_helpers import getSerialNumber as getSerialNumber, hasRequiredStyle as hasRequiredStyle
from resource_well.gui.impl.gen.view_models.views.lobby.completed_progression_view_model import CompletedProgressionViewModel as CompletedProgressionViewModel
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE as RESOURCE_WELL_SOUND_SPACE
from resource_well.gui.impl.lobby.feature.tooltips.serial_number_tooltip import SerialNumberTooltip as SerialNumberTooltip
from shared_utils import first as first
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class CompletedProgressionView(ViewImpl):
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell: Any
    __rewardID: Any
    __vehicle: Any
    def __init__(self, layoutID=...):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onShown(self):
        ...
    def __fillModel(self):
        ...
    def __showVehicle(self):
        ...
    def __onEventStateUpdated(self):
        ...
    def __goBack(self):
        ...
    def __searchRewardIDAndVehicle(self):
        ...

class CompletedProgressionWindow(WindowImpl):
    def __init__(self, layer, *args, **kwargs):
        ...
