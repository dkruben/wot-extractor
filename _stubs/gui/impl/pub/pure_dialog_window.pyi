# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/pure_dialog_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets as DialogPresets
from gui.impl.pub.dialog_window import DialogWindow as DialogWindow, DialogFlags as DialogFlags
from frameworks.wulf import ViewModel as ViewModel, Array as Array

class PureDialogWindow(DialogWindow):
    def __init__(self, content=None, bottomContent=None, parent=None, balanceContent=None, enableBlur=True, preset=..., flags=...):
        ...
    def setTitle(self, title=..., args=None, fmtArgs=None, namedFmtArgs=True):
        ...
    def setFormattedTitle(self, formattedTitle=''):
        ...
    def setIcon(self, icon):
        ...
    def addButton(self, name, label, isFocused=False, invalidateAll=False, soundDown=None, rawLabel=''):
        ...
    def setBackground(self, backImg):
        ...
    def _getResultData(self):
        ...
    @staticmethod
    def _addArgsOfModel(arrModel, args):
        ...
    @staticmethod
    def _addArgsOfString(arrModel, args):
        ...
