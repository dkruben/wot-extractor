# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/seasons_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_helper import getDropdownKeyBySeason as getDropdownKeyBySeason, getSeasonName as getSeasonName, COMP7_ARCHIVE_NAMES as COMP7_ARCHIVE_NAMES, COMP7_SEASON_NUMBERS as COMP7_SEASON_NUMBERS, getDropdownKeyByArchiveName as getDropdownKeyByArchiveName, isComp7Archive as isComp7Archive, getArchiveName as getArchiveName
from comp7.gui.shared.gui_items.dossier.stats import getComp7DossierStats as getComp7DossierStats
from gui.Scaleform.daapi.view.lobby.profile.ProfileSection import BattleTypesDropDownItems as BattleTypesDropDownItems
from gui.Scaleform.daapi.view.lobby.profile.seasons_manager import BaseSeasonManager as BaseSeasonManager
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7SeasonsManager(BaseSeasonManager):
    __comp7Controller: Any
    _seasonKey: Any
    def __init__(self):
        ...
    def getStats(self, dossierStats):
        ...
    def addSeasonsDropdown(self, targetVO):
        ...
    def _makeSeasonsDropDown(self):
        ...
    def _showSeasonsDropDown(self):
        ...
    def _getSeasonsProvider(self):
        ...
    @staticmethod
    def _addSeasonToDropDown(itemsList, seasonID, season):
        ...

def getComp7SeasonManagers():
    ...
