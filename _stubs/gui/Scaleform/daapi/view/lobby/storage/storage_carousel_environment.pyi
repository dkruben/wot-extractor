# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/storage_carousel_environment.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import ICarouselEnvironment as ICarouselEnvironment
from gui.Scaleform.daapi.view.common.vehicle_carousel.carousel_environment import formatCountString as formatCountString
from gui.Scaleform.daapi.view.meta.StorageCarouselEnvironmentMeta import StorageCarouselEnvironmentMeta as StorageCarouselEnvironmentMeta
from gui.Scaleform.locale.TANK_CAROUSEL_FILTER import TANK_CAROUSEL_FILTER as TANK_CAROUSEL_FILTER
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from gui.shared import event_dispatcher as shared_events
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers.i18n import makeString as _ms
from gui.shared.formatters import text_styles as text_styles
_SEARCH_INPUT_MAX_CHARS = 50

class StorageCarouselEnvironment(ICarouselEnvironment, IGlobalListener, StorageCarouselEnvironmentMeta):
    _dataProvider: Any
    __currentFilteredVehicles: Any
    __isFilterCounterShown: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def setDataProvider(self, dp):
        ...
    @property
    def filter(self):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def resetFilter(self):
        ...
    def blinkCounter(self):
        ...
    def formatCountVehicles(self):
        ...
    def changeSearchNameVehicle(self, inputText):
        ...
    def showItemInfo(self, itemId):
        ...
    def updateCounter(self):
        ...
    def updateSearchInput(self, text=''):
        ...
