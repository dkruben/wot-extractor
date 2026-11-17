# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/marathon/marathon_header_tooltips.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import time as time
import typing as typing
from gui.Scaleform import MENU as MENU
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.marathon.marathon_constants import MarathonState as MarathonState
from gui.shared.formatters import text_styles as text_styles
from helpers import i18n as i18n
from helpers.time_utils import ONE_DAY as ONE_DAY, getTimeStructInLocal as getTimeStructInLocal, ONE_HOUR as ONE_HOUR

class BaseTooltip(object):
    _data: Any
    def __init__(self, dataContainer):
        ...
    def create(self):
        ...

class SimpleTextHeaderTooltip(BaseTooltip):
    def create(self):
        ...

class ProgressHeaderTooltip(BaseTooltip):
    def create(self):
        ...
    def __getProgressInDays(self, timeValue):
        ...

class CountdownHeaderTooltip(BaseTooltip):
    def create(self):
        ...
    def __getFormattedTillTimeString(self, timeValue, keyNamespace, extraFmt=False):
        ...
    def __getTillTimeStart(self, value):
        ...
    def __getTillTimeEnd(self, value):
        ...
