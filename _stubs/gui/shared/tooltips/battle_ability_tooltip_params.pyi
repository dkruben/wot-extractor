# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/battle_ability_tooltip_params.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from functools import partial as partial
from past.utils import old_div as old_div
import ResMgr as ResMgr
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import _getFormattedNum as _getFormattedNum, _cutDigits as _cutDigits
from gui.Scaleform.locale.COMMON import COMMON as COMMON
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.tooltips import formatters as formatters
from gui.shared.formatters import text_styles as text_styles
from helpers import i18n as i18n
from items import vehicles as vehicles
from soft_exception import SoftException as SoftException
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from items import _xml as _xml
COLOR_SCHEME: tuple
NEUTRAL_STYLE: Any
TOOLTIPS_PATH = 'gui/ability_tooltips.xml'
_logger: Any
g_battleAbilityParamsRenderers: dict
ConsumableTooltipEntry: Any
g_battleAbilityTooltipMgr: Any

class DisplayValuesMixin(object):
    @classmethod
    def _getDisplayParams(cls, curEq, eqsRange, param):
        ...

class DirectValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getDisplayParams(cls, curEq, eqsRange, param):
        ...

class ReciprocalValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getDisplayParams(cls, curEq, eqsRange, param):
        ...

class ShellStunValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getDisplayParams(cls, curEq, eqsRange, param):
        ...

class MultiValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getDisplayParams(cls, curEq, eqsRange, param):
        ...

class NestedValuesMixin(DisplayValuesMixin):
    @classmethod
    def _getDisplayParams(cls, curEq, eqsRange, param):
        ...
    @classmethod
    def _getEqParam(cls, eq, params):
        ...

class NestedTupleFirstValuesMixin(NestedValuesMixin):
    @classmethod
    def _getEqParam(cls, eq, params):
        ...

class NestedShellStunValuesMixin(NestedValuesMixin):
    @classmethod
    def _getDisplayParams(cls, curEq, eqsRange, param):
        ...

class DisplayLabelMixin(object):
    @classmethod
    def _formatParamStringInternal(cls, values, unitLocalization=None, returnArray=False):
        ...
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class NumericLabelMixin(DisplayLabelMixin):
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class SecondsLabelMixin(DisplayLabelMixin):
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class AdditionalSecondsLabelMixin(DisplayLabelMixin):
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class MeterLabelMixin(DisplayLabelMixin):
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class PercentageLabelMixin(DisplayLabelMixin):
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class PerksControllerModPercentageMixin(DisplayLabelMixin):
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class MultiMeterLabelMixin(DisplayLabelMixin):
    @classmethod
    def _formatParamString(cls, values, isMultiplier=True, returnArray=False):
        ...

class AbilityParam(object):
    @classmethod
    def extendBlocks(cls, staticBlock, dynamicBlock, curEq, eqsRange, param, title, isMultiplier=True):
        ...

class FixedTextParam(AbilityParam):
    @classmethod
    def extendBlocks(cls, staticBlock, dynamicBlock, curEq, eqsRange, param, title, isMultiplier=True):
        ...

class TextParam(AbilityParam, DisplayValuesMixin, DisplayLabelMixin):
    @classmethod
    def extendBlocks(cls, staticBlock, dynamicBlock, curEq, eqsRange, param, title, isMultiplier=True):
        ...

class MultiTextParam(AbilityParam, DisplayValuesMixin, DisplayLabelMixin):
    @classmethod
    def extendBlocks(cls, staticBlock, dynamicBlock, curEq, eqsRange, param, title, isMultiplier=True):
        ...

class NestedTextParam(AbilityParam, DisplayValuesMixin, DisplayLabelMixin):
    @classmethod
    def extendBlocks(cls, staticBlock, dynamicBlock, curEq, eqsRange, param, title, isMultiplier=True):
        ...

class DirectNumericTextParam(TextParam, DirectValuesMixin, NumericLabelMixin):
    ...

class DirectSecondsTextParam(TextParam, DirectValuesMixin, SecondsLabelMixin):
    ...

class DirectMetersTextParam(TextParam, DirectValuesMixin, MeterLabelMixin):
    ...

class DirectPercentageTextParam(TextParam, DirectValuesMixin, PercentageLabelMixin):
    ...

class ReciprocalPercentageTextParam(TextParam, ReciprocalValuesMixin, PercentageLabelMixin):
    ...

class ShellStunSecondsTextParam(TextParam, ShellStunValuesMixin, SecondsLabelMixin):
    ...

class MultipleMetersTextParam(MultiTextParam, MultiValuesMixin, MultiMeterLabelMixin):
    ...

class NestedMetersTextParam(NestedTextParam, NestedValuesMixin, MeterLabelMixin):
    ...

class NestedSecondsTextParam(NestedTextParam, NestedValuesMixin, SecondsLabelMixin):
    ...

class NestedPercentageTextParam(NestedTextParam, NestedValuesMixin, PercentageLabelMixin):
    ...

class NestedPercentageTextTupleValueParam(NestedTextParam, NestedTupleFirstValuesMixin, PerksControllerModPercentageMixin):
    ...

class NestedShellStunSecondsTextParam(TextParam, NestedShellStunValuesMixin, SecondsLabelMixin):
    ...

class BattleAbilityTooltipManager(object):
    __tooltipsSettings: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    def _validateTooltipsData(self, tooltipsSettings):
        ...
    def init(self, xmlPath):
        ...
    def createBattleAbilityTooltipRenderers(self, skillInfo, staticBlock, dynamicBlock, level=1):
        ...
    def getTooltipInfo(self, tooltipIdentifier):
        ...

def _getTextStyle(idx):
    ...
def _getAttrName(param):
    ...
def _allElementsEq(values):
    ...
def makeRenderer(func, isMultiplier=True):
    ...
