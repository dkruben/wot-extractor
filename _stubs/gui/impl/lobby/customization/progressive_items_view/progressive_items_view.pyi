# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/customization/progressive_items_view/progressive_items_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from gui.game_control.links import URLMacros as URLMacros
from gui.server_events.events_dispatcher import showProgressiveItemsBrowserView as showProgressiveItemsBrowserView
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_view.item_model import ItemModel as ItemModel
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_view.item_level_info_model import ItemLevelInfoModel as ItemLevelInfoModel
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_view.progressive_items_view_model import ProgressiveItemsViewModel as ProgressiveItemsViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.Scaleform.daapi.view.lobby.customization.shared import getProgressionItemStatusText as getProgressionItemStatusText
from gui.shared.gui_items.customization import CustomizationTooltipContext as CustomizationTooltipContext
from helpers import dependency as dependency, int2roman as int2roman
from helpers.i18n import makeString as _ms
from items import vehicles as vehicles
from items.components.c11n_constants import ProjectionDecalFormTags as ProjectionDecalFormTags
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from web.web_client_api import webApiCollection as webApiCollection, ui as ui_web_api, sound as sound_web_api
from gui.shared.utils.graphics import isRendererPipelineDeferred as isRendererPipelineDeferred
from items.components.c11n_constants import CustomizationType as CustomizationType
_logger: Any
_PREVIEW_ICON_SIZE: tuple
_PREVIEW_ICON_INNER_SIZE_DEFAULT: tuple
_PREVIEW_ICON_INNER_SIZE: dict

class ProgressiveItemsView(ViewImpl):
    __slots__: tuple
    __lobbyContext: Any
    __itemsCache: Any
    __customizationService: Any
    __appLoader: Any
    __settingsCore: Any
    __guiLoader: Any
    _itemsProgressData: Any
    _possibleItems: Any
    _vehicle: Any
    __blur: Any
    __layoutID: Any
    __c11nView: Any
    __urlMacros: Any
    __guiSettings: Any
    def __init__(self, layoutID, c11nView=None, *args, **kwargs):
        ...
    def createToolTip(self, event):
        ...
    def update(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _onSelectItem(self, args=None):
        ...
    def _showVideoPage(self, args=None):
        ...
    # decorador original: @adisp_process
    def __showVideo(self):
        ...
    def _getPossibleItemsForVehicle(self):
        ...
    def __setItems(self, model):
        ...
    def __setEachLevelInfo(self, model, item):
        ...
    @staticmethod
    def __getTooltipData(intCD, tooltip, level):
        ...
