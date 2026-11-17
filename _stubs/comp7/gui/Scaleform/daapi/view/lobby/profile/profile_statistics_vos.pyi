# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/profile_statistics_vos.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.Scaleform.daapi.view.lobby.profile.profile_utils import COMP7_STATISTICS_LAYOUT as COMP7_STATISTICS_LAYOUT
from gui.Scaleform.daapi.view.lobby.profile.ProfileUtils import ProfileUtils as PUtils
from gui.Scaleform.daapi.view.lobby.profile.profile_statistics_vos import ProfileDictStatisticsVO as ProfileDictStatisticsVO, packAvgDmgLditItemData as packAvgDmgLditItemData, getDetailedStatisticsData as getDetailedStatisticsData, formatChartsData as formatChartsData, getVehStatsByTypes as getVehStatsByTypes, getVehStatsByNation as getVehStatsByNation
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.impl import backport as backport
from gui.impl.gen import R as R

class ProfileComp7StatisticsVO(ProfileDictStatisticsVO):
    __headerKey: Any
    def __init__(self, targetData, accountDossier, isCurrentUser):
        ...
    def _getHeaderText(self, data):
        ...
    def _getHeaderData(self, data):
        ...
    def _getDetailedData(self, data):
        ...

def getComp7StatisticsVO(battlesType, targetData, accountDossier, isCurrentUser):
    ...
