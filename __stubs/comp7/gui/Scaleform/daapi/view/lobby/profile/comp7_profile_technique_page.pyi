# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/Scaleform/daapi/view/lobby/profile/comp7_profile_technique_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from comp7.gui.Scaleform.daapi.view.lobby.profile.comp7_profile_helper import getBattleHandlers as getBattleHandlers
from comp7.gui.Scaleform.daapi.view.lobby.profile.profile_utils import COMP7_VEHICLE_STATISTICS_LAYOUT as COMP7_VEHICLE_STATISTICS_LAYOUT
from comp7.gui.Scaleform.daapi.view.lobby.profile.seasons_manager import getComp7SeasonManagers as getComp7SeasonManagers
from gui.Scaleform.daapi.view.lobby.profile.ProfileTechniquePage import ProfileTechniquePage as ProfileTechniquePage
from gui.Scaleform.genConsts.PROFILE_DROPDOWN_KEYS import PROFILE_DROPDOWN_KEYS as PROFILE_DROPDOWN_KEYS
from gui.Scaleform.locale.PROFILE import PROFILE as PROFILE
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from math_common import round_py2_style_int as round_py2_style_int

class Comp7ProfileTechniquePage(ProfileTechniquePage):
    def __init__(self, *args):
        ...
    @classmethod
    def _makeBattleTypesDropDown(cls, accountDossier, forVehiclesPage=False):
        ...
    def _getEmptyScreenLabel(self):
        ...
    def _getDefaultTableHeader(self, isFallout=False, showMarkOfMastery=False):
        ...
    def _unpackVehicleParams(self, vehParams):
        ...
    def _getLayout(self):
        ...
