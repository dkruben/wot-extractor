# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/frameworks/wulf/view/submodel_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
import typing as typing
from helpers.events_handler import EventsHandler as EventsHandler
from typing import Optional as Optional
from frameworks.wulf import View as View, ViewEvent as ViewEvent, Window as Window
_logger: Any

class SubModelPresenter(EventsHandler):
    __slots__: tuple
    __parentView: Any
    __viewModel: Any
    __isLoaded: Any
    def __init__(self, viewModel, parentView):
        ...
    @property
    def isLoaded(self):
        ...
    @property
    def parentView(self):
        ...
    def getParentWindow(self):
        ...
    def getViewModel(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def clear(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createPopOverContent(self, event):
        ...
    def createContextMenuContent(self, event):
        ...
    def createToolTip(self, event):
        ...
    def createPopOver(self, event):
        ...
    def createContextMenu(self, event):
        ...
