# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/complex_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui import makeHtmlString as makeHtmlString
from gui.shared.utils.functions import stripColorTagDescrTags as stripColorTagDescrTags
from helpers import i18n as i18n
_TEXT_FORMAT = "{0[0]}{1}{0[1]}\n<font size='1' > </font>\n"
_TOOLTIP_KIND: tuple
_BLOCK_TAGS_MAP: dict

def _getTags(blockType, formatType):
    ...
def _getFormattedText(text, blockType, formatType):
    ...
def _doFormatToolTipFromKey(tooltipID, formatType):
    ...
def _doFormatToolTipFromText(tooltipID, formatType):
    ...
def doFormatData(data, formatType):
    ...
def doFormatToolTip(tooltipID, formatType):
    ...
