# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/offer_gift_vehicle_preview.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from constants import RentType as RentType
from gui.Scaleform.daapi.view.lobby.vehicle_preview.items_kit_helper import getDataOneVehicle as getDataOneVehicle, addBuiltInEquipment as addBuiltInEquipment
from gui.Scaleform.daapi.view.lobby.vehicle_preview.vehicle_preview import VehiclePreview as VehiclePreview
from gui.Scaleform.framework.entities import BaseDAAPIComponent as BaseDAAPIComponent
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.impl.lobby.offers.offer_gift_dialog import RENT_VALUE_DESCR_BY_TYPE as RENT_VALUE_DESCR_BY_TYPE
from gui.shared import event_dispatcher as event_dispatcher, formatters as formatters
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from web.web_client_api.common import ItemPackEntry as ItemPackEntry, ItemPackType as ItemPackType, ItemPackTypeGroup as ItemPackTypeGroup
from gui.impl import backport as backport
from gui.impl.gen import R as R
_logger: Any

class OfferGiftVehiclePreview(VehiclePreview):
    __offersProvider: Any
    __lobbyContext: Any
    _offer: Any
    _gift: Any
    _vehicle: Any
    _customCallbacks: Any
    _confirmCallback: Any
    __itemsPack: Any
    def __init__(self, ctx):
        ...
    def setBottomPanel(self):
        ...
    def _generateItemsPack(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _getPreviewDescription(self):
        ...
    def _getButtonLabel(self):
        ...
    def _getBuyingPanelData(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onInventoryChanged(self, *_):
        ...
    def __onServerSettingsChange(self, *args, **kwargs):
        ...
    def __onOffersUpdated(self):
        ...
    @classmethod
    def __getCrewItemPackEntry(cls, item):
        ...
