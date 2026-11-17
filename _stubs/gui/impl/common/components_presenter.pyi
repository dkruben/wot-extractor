# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/common/components_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl.common.base_sub_model_view import BaseSubModelView as BaseSubModelView
from gui.impl.pub import ViewImpl as ViewImpl
from frameworks.wulf import View as View, ViewEvent as ViewEvent, Window as Window

class ComponentsPresenterView(ViewImpl):
    __componentPresenters: Any
    def __init__(self, settings):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def createPopOverContent(self, event):
        ...
    def _registerSubModels(self):
        ...

class BaseSubModelViewWithToolTips(BaseSubModelView):
    def createToolTipContent(self, event, contentID):
        ...
    def createPopOverContent(self, event):
        ...
    def createToolTip(self, event):
        ...
