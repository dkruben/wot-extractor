# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/header/helpers/fight_btn_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.mapbox.mapbox_helpers import getMapboxBattlesStatus as getMapboxBattlesStatus
from gui.prb_control.formatters.tooltips import getAbsenceCrewList as getAbsenceCrewList
from gui.prb_control.settings import UNIT_RESTRICTION as UNIT_RESTRICTION
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION, PREBATTLE_RESTRICTION as PREBATTLE_RESTRICTION
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString
from gui.shared.gui_items.Vehicle import getTypeUserName as getTypeUserName
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n
from gui.prb_control.items import ValidationResult as ValidationResult
_STR_PATH = R.strings.menu.headerButtons.fightBtn.tooltip
_TOOLTIP_PATH = R.strings.tooltips
getRoyaleFightBtnTooltipData = getCommonFightBtnTooltipData

def getSquadFightBtnTooltipData(result):
    ...
def getRankedFightBtnTooltipData(result):
    ...
def getCommonFightBtnTooltipData(result):
    ...
def getMapsTrainingTooltipData():
    ...
def getEpicBattlesOnlyVehicleTooltipData(result):
    ...
def getEventTooltipData():
    ...
def getPreviewTooltipData():
    ...
def getRandomTooltipData(result, isInSquad):
    ...
def getMapboxFightBtnTooltipData(result, isInSquad):
    ...
