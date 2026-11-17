# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/efficiency.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.locale.BATTLE_RESULTS import BATTLE_RESULTS as BATTLE_RESULTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.tooltips import formatters as formatters
from helpers.i18n import makeString as ms
from gui.shared.formatters import text_styles as text_styles

class HeaderItemPacker(object):
    __headerTitle: Any
    __icon: Any
    def __init__(self, headerTitle, icon):
        ...
    def pack(self, data):
        ...

class TermsItemPacker(HeaderItemPacker):
    _termsAlias: Any
    def __init__(self, headerTitle, icon, termsAlias):
        ...
    def pack(self, data):
        ...
    def _packTerms(self, data):
        ...

class KillItemPacker(TermsItemPacker):
    def __init__(self):
        ...
    def pack(self, data):
        ...
    def _packTerms(self, data):
        ...

class DetectionItemPacker(TermsItemPacker):
    def __init__(self):
        ...

class LinerItemPacker(TermsItemPacker):
    def pack(self, data):
        ...

class DamageItemPacker(LinerItemPacker):
    def __init__(self):
        ...

class ArmorItemPacker(LinerItemPacker):
    def __init__(self):
        ...

class StunItemPacker(LinerItemPacker):
    def __init__(self):
        ...

class AssistItemPacker(LinerItemPacker):
    def __init__(self):
        ...

class CaptureItemPacker(LinerItemPacker):
    def __init__(self):
        ...

class DefenceItemPacker(LinerItemPacker):
    def __init__(self):
        ...

class CritsItemPacker(TermsItemPacker):
    def __init__(self):
        ...
    def pack(self, data):
        ...
    def __addResultBlock(self, items, title, text):
        ...

def makeHtmlText(pattern, text):
    ...
