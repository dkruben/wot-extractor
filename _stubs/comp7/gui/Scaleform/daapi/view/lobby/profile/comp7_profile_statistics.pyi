# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/comp7_profile_statistics.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_helper import getBattleHandlers as getBattleHandlers
from comp7.gui.Scaleform.daapi.view.lobby.profile.profile_statistics_vos import getComp7StatisticsVO as getComp7StatisticsVO
from comp7.gui.Scaleform.daapi.view.lobby.profile.seasons_manager import getComp7SeasonManagers as getComp7SeasonManagers
from gui.Scaleform.daapi.view.lobby.profile.ProfileStatistics import ProfileStatistics as ProfileStatistics
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS

class Comp7ProfileStatistics(ProfileStatistics):
    def __init__(self, *args):
        ...
    @classmethod
    def _makeBattleTypesDropDown(cls, accountDossier, forVehiclesPage=False):
        ...
    def _setStatisticsVO(self, targetData, accountDossier):
        ...
