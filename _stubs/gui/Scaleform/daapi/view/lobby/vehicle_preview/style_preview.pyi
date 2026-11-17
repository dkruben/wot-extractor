# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/style_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.LobbySelectableView import LobbySelectableView as LobbySelectableView
from gui.Scaleform.daapi.view.lobby.vehicle_preview.preview_selectable_logic import PreviewSelectableLogic as PreviewSelectableLogic
from gui.Scaleform.daapi.view.lobby.vehicle_preview.sound_constants import STYLE_PREVIEW_SOUND_SPACE as STYLE_PREVIEW_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.VehicleBasePreviewMeta import VehicleBasePreviewMeta as VehicleBasePreviewMeta
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents as CameraRelatedEvents
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, event_dispatcher as event_dispatcher, events as events, g_eventBus as g_eventBus
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.customization.c11n_items import getGroupFullNameResourceID as getGroupFullNameResourceID
from helpers import dependency as dependency
from skeletons.gui.game_control import IHeroTankController as IHeroTankController
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from uilogging.shop.loggers import ShopVehicleStylePreviewMetricsLogger as ShopVehicleStylePreviewMetricsLogger, ShopVehicleStylePreviewFlowLogger as ShopVehicleStylePreviewFlowLogger
_logger: Any

class VehicleStylePreview(LobbySelectableView, VehicleBasePreviewMeta):
    __background_alpha__ = 0.0
    __hangarSpace: Any
    __heroTanksControl: Any
    _COMMON_SOUND_SPACE = STYLE_PREVIEW_SOUND_SPACE
    __ctx: Any
    _style: Any
    __backPreviewAlias: Any
    __outfit: Any
    __vehicleCD: Any
    __styleDescr: Any
    __topPanelData: Any
    __selectedVehicleEntityId: Any
    __uiMetricsLogger: Any
    __uiFlowLogger: Any
    def __init__(self, ctx=None):
        ...
    def closeView(self):
        ...
    def onBackClick(self):
        ...
    def setTopPanel(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _createSelectableLogic(self):
        ...
    def _getAdditionalInfoVO(self):
        ...
    def __onVehicleLoading(self, ctxEvent):
        ...
    def __onHangarCreateOrRefresh(self):
        ...
    def __handleWindowClose(self, event=None):
        ...
