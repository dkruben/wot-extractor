# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/simple_dialog_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.resources import R as R
from gui.impl.gen.view_models.constants.dialog_presets import DialogPresets as DialogPresets
from gui.impl.gen.view_models.windows.simple_dialog_window_model import SimpleDialogWindowModel as SimpleDialogWindowModel
from gui.impl.pub.dialog_window import DialogContent as DialogContent, DialogFlags as DialogFlags
from gui.impl.pub.pure_dialog_window import PureDialogWindow as PureDialogWindow
from frameworks.wulf import ViewModel as ViewModel

class SimpleDialogWindow(PureDialogWindow):
    def __init__(self, bottomContent=None, parent=None, balanceContent=None, enableBlur=True, preset=..., flags=...):
        ...
    @property
    def contentViewModel(self):
        ...
    def setFormattedMessage(self, formattedMessage=''):
        ...
    def setMessage(self, message, args=None, fmtArgs=None, namedFmtArgs=True):
        ...
