# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/cybersport.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.daapi.view.lobby.rally import vo_converters as vo_converters
from gui.Scaleform.daapi.view.lobby.rally.action_button_state_vo import ActionButtonStateVO as ActionButtonStateVO
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.shared.tooltips import ToolTipBaseData as ToolTipBaseData, TOOLTIP_TYPE as TOOLTIP_TYPE
from helpers import dependency as dependency
from helpers import i18n as i18n
from skeletons.gui.shared import IItemsCache as IItemsCache

class CybersportToolTipData(ToolTipBaseData):
    itemsCache: Any
    def __init__(self, context):
        ...

class CybersportSelectedVehicleToolTipData(CybersportToolTipData):
    def getDisplayableData(self, intCD):
        ...

class CybersportSlotToolTipData(CybersportToolTipData):
    def getDisplayableData(self, index, unitMgrID=None):
        ...

class CybersportSlotSelectedToolTipData(CybersportToolTipData):
    def getDisplayableData(self, index, unitMgrID=None):
        ...

class SquadSlotSelectedToolTipData(CybersportToolTipData):
    def getDisplayableData(self, index, unitMgrID=None):
        ...

class CybersportUnitToolTipData(CybersportToolTipData):
    def getDisplayableData(self, data=None):
        ...

class CybersportUnitLevelToolTipData(CybersportToolTipData):
    def getDisplayableData(self, level):
        ...
