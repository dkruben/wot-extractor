# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/carousel_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import WindowLayer as WindowLayer
from notification import NotificationMVC as NotificationMVC
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.app_loader import sf_lobby as sf_lobby
from gui.impl import backport as backport
from gui.impl.backport import createTooltipData as createTooltipData, BackportTooltipWindow as BackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared.event_dispatcher import showVehicleHubOverview as showVehicleHubOverview
from gui.shared.utils.functions import replaceHyphenToUnderscore as replaceHyphenToUnderscore
from halloween.gui.halloween_gui_constants import HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP as HALLOWEEN_CAROUSEL_VEHICLE_TOOLTIP
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_vehicle_view_model import CarouselTooltips as CarouselTooltips, HangarCarouselVehicleViewModel as HangarCarouselVehicleViewModel, VehicleTypes as VehicleTypes
from halloween.gui.impl.gen.view_models.views.lobby.widgets.hangar_carousel_view_model import HangarCarouselViewModel as HangarCarouselViewModel
from halloween.gui.impl.lobby.hw_helpers import isDailyKeyQuestCompleted as isDailyKeyQuestCompleted, getDailyKeyQuestDescription as getDailyKeyQuestDescription, getVehicleState as getVehicleState
from halloween.gui.impl.lobby.tooltips.simple_format_tooltip import SimpleFormatTooltipView as SimpleFormatTooltipView
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController as IHalloweenController
from halloween.uilogging.loggers import HWMetricsLogger as HWMetricsLogger
from halloween.uilogging.logging_constants import HWLogKeys as HWLogKeys
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace

# base nao representavel no stub: ViewComponent[...]
class CarouselView:
    _POP_UP_PADDING_X = 5
    _POP_UP_PADDING_Y = 13
    _carouselSize = 0
    _hangarSpace: Any
    _itemsCache: Any
    _halloweenCtrl: Any
    _halloweenArtefactsCtrl: Any
    __uiLogger: Any
    def __init__(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def __onLoadingMilestoneReached(self, milestoneName):
        ...
    def __updateNotificationsLayout(self):
        ...
    def _finalize(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @sf_lobby
    def __app(self):
        ...
    def _getVehicles(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _subscribe(self):
        ...
    def _unsubscribe(self):
        ...
    def __onVehicleLockUpdated(self, *args):
        ...
    def __onRentVehicleStatusUpdate(self):
        ...
    def __fillVehicles(self):
        ...
    def __onCurrentVehicleChanged(self):
        ...
    def __onTankChanged(self, args):
        ...
    def __onVehiclePreview(self, args):
        ...
    def __onResized(self, args):
        ...
