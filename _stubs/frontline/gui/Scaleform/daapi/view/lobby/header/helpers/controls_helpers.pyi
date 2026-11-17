# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/header/helpers/controls_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.daapi.view.lobby.header.helpers.controls_helpers import DefaultLobbyHeaderHelper as DefaultLobbyHeaderHelper
from gui.Scaleform.daapi.view.lobby.header.helpers.fight_btn_tooltips import getCommonFightBtnTooltipData as getCommonFightBtnTooltipData, getRandomTooltipData as getRandomTooltipData
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.settings import PRE_QUEUE_RESTRICTION as PRE_QUEUE_RESTRICTION
from gui.shared.formatters.ranges import toRomanRangeString as toRomanRangeString
from gui.shared.utils.functions import makeTooltip as makeTooltip

class FrontlineLobbyHeaderHelper(DefaultLobbyHeaderHelper):
    __slots__: tuple
    @classmethod
    def _getDisabledFightTooltipData(cls, prbValidation, isInSquad):
        ...

def getFightBtnTooltipData(result):
    ...
