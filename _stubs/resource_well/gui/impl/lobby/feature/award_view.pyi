# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/award_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl import backport as backport
from gui.impl.auxiliary.vehicle_helper import fillVehicleInfo as fillVehicleInfo
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.shared.event_dispatcher import selectVehicleInHangar as selectVehicleInHangar, showHangar as showHangar
from helpers import dependency as dependency
from resource_well.gui.impl.gen.view_models.views.lobby.award_view_model import AwardViewModel as AwardViewModel
from resource_well.gui.impl.lobby.feature.sounds import RESOURCE_WELL_SOUND_SPACE as RESOURCE_WELL_SOUND_SPACE
from resource_well.gui.impl.lobby.feature.tooltips.serial_number_tooltip import SerialNumberTooltip as SerialNumberTooltip
from resource_well.gui.shared.event_dispatcher import showMainWindow as showMainWindow
from skeletons.gui.resource_well import IResourceWellController as IResourceWellController

class AwardView(ViewImpl):
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell: Any
    __vehicle: Any
    __rewardConfig: Any
    def __init__(self, rewardID, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, serialNumber, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __close(self):
        ...
    def __showVehicle(self):
        ...

class AwardWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, rewardID, serialNumber):
        ...
