# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/DebugMonitorView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import xrange as xrange
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.DebugView import DebugView as DebugView
from gui.DebugView import DebugViewItem as DebugViewItem

class DebugMonitorView(DebugView):
    __contentInfo: Any
    __newContentInfo: Any
    def __init__(self, textureName='', parentGUI=None):
        ...
    def destroy(self):
        ...
    def setContent(self, content):
        ...
    def __setItem(self, nameStr, valueStr, dividerStr, item=None):
        ...
    def __updateContentInfoItem(self, keyname, value):
        ...
    def __commitContentInfo(self):
        ...
    def __roolbackContentInfo(self):
        ...
    def __buildContentItemsBy(self, content, baseIndent=0, baseKeyname=''):
        ...
    def __updateViewByContentItems(self, contentItems):
        ...
