# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/pub/pop_over_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from frameworks.wulf import WindowFlags as WindowFlags, ViewFlags as ViewFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.windows.pop_over_window_model import PopOverWindowModel as PopOverWindowModel
from gui.impl.pub.window_impl import WindowImpl as WindowImpl
from gui.impl.pub.window_view import WindowView as WindowView

class PopOverWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, event, content, parent, layer=..., direction=None):
        ...
    @property
    def popOverModel(self):
        ...
