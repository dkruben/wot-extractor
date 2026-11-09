# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/fortifications.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.utils import old_div as old_div
from gui.Scaleform.daapi.view.lobby.rally import vo_converters as vo_converters
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.FORTIFICATIONS import FORTIFICATIONS as FORTIFICATIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.shared.tooltips import TOOLTIP_TYPE as TOOLTIP_TYPE
from gui.shared.tooltips.common import ToolTipBaseData as ToolTipBaseData
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui import makeHtmlString as makeHtmlString
__buildsDirectionMap: dict
_MAX_VEHICLES_COUNT = 23

class ToolTipRefSysDirects(ToolTipBaseData):
    def __init__(self, context):
        ...
    @staticmethod
    def __getTitle(index):
        ...
    @staticmethod
    def __getPointReward(index):
        ...
    def buildMapPoints(self, size, teamBasePositions, playerTeam, isCurrentBattle):
        ...
    def getDisplayableData(self, *args, **kwargs):
        ...

class FortToolTipData(ToolTipBaseData):
    itemsCache: Any
    def __init__(self, context):
        ...

class FortificationsSlotToolTipData(FortToolTipData):
    itemsCache: Any
    def getDisplayableData(self, index, unitMgrID=None):
        ...

def getBuildsDirection(direction):
    ...
