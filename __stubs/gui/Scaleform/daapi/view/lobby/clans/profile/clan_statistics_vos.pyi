# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/clans/profile/clan_statistics_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.lobby.clans.profile import getI18ArenaById as getI18ArenaById
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import DetailedStatisticsUtils as SUtils
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import ProfileUtils as PUtils
from gui.Scaleform.daapi.view.lobby.profile.profile_statistics_vos import BaseDictStatisticsVO as BaseDictStatisticsVO
from gui.Scaleform.locale.CLANS import CLANS as CL
from gui.clans.data_wrapper.utils import formatField as formatField
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers.i18n import makeString as _ms

class FortGlobalMapStatistics(BaseDictStatisticsVO):
    def _getHeaderData(self, data):
        ...
    def _getDetailedData(self, data):
        ...

def _resourceParam(value):
    ...
def _getTooltip(headerKey, bodyKey, ratingOutdated=False):
    ...
def _getDataObject(key, i18nFunc, value, ratingOutdated=False, tooltipData=None):
    ...
def _getDataObjectTruncatedValue(key, i18nFunc, value):
    ...
def _getLevelParams(i18nFunc, battlesCountGetter, winsEfficiencyGetter, eloRatingGetter, placeGetter, favArenaNameGetter, ratingOutdated):
    ...
