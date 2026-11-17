# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/ClanProfileTableStatisticsView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from adisp import adisp_process as adisp_process
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.daapi.view.lobby.clans.profile import getI18ArenaById as getI18ArenaById
from gui.Scaleform.daapi.view.meta.ClanProfileTableStatisticsViewMeta import ClanProfileTableStatisticsViewMeta as ClanProfileTableStatisticsViewMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES as CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS as CLANS
from gui.clans import formatters as formatters
from gui.clans.data_wrapper.utils import formatField as formatField, isValueAvailable as isValueAvailable
from gui.impl import backport as backport
from gui.shared.formatters import icons as icons, text_styles as text_styles
from gui.shared.utils import sortByFields as sortByFields
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from helpers import int2roman as int2roman
from helpers import time_utils as time_utils
from helpers.i18n import makeString as _ms
from skeletons.gui.web import IWebController as IWebController

class _SORT_IDS(object):
    FRONT = 'front'
    PROVINCE = 'province'
    MAP = 'map'
    PRIMETIME = 'primeTime'
    DAYS = 'days'
    INCOME = 'income'

class ClanProfileTableStatisticsView(ClanProfileTableStatisticsViewMeta):
    clanCtrl: Any
    __provincesDP: Any
    def __init__(self):
        ...
    # decorador original: @adisp_process
    def setProxy(self, proxy, clanDossier):
        ...
    def _dispose(self):
        ...
    def _prepareHeaders(self, showTreasury, enabled):
        ...

class _ClanProfileProvinceDataProvider(SortableDAAPIDataProvider):
    _list: Any
    __mapping: Any
    __selectedID: Any
    __showTreasuryData: Any
    __dataList: Any
    __commonRevenue: Any
    __sortMapping: Any
    def __init__(self, showTreasuryData):
        ...
    def getCommonRevenue(self):
        ...
    @property
    def collection(self):
        ...
    @property
    def sortedCollection(self):
        ...
    def emptyItem(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def getSelectedIdx(self):
        ...
    def setSelectedID(self, clanID):
        ...
    def getVO(self, index):
        ...
    def buildList(self, provinces):
        ...
    def rebuildList(self, cache):
        ...
    def refreshItem(self, cache, clanDBID):
        ...
    def pyGetSelectedIdx(self):
        ...
    def pySortOn(self, fields, order):
        ...
    def _makeVO(self, province):
        ...
    def __sortingMethod(self, item, field):
        ...
    def __getFront(self, province):
        ...
    def __getProvinceName(self, province):
        ...
    def __getMap(self, province):
        ...
    def __getPrimeTime(self, province):
        ...
    def __getDays(self, province):
        ...
    def __getIncome(self, province):
        ...
    def __isRobbed(self, province):
        ...

def _packColumn(columndID, label, buttonWidth, tooltip, enabled, icon='', sortOrder=-1, showSeparator=True, textAlign='left'):
    ...
