# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/fullscreen_event_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.fullscreen_event_view_model import FullscreenEventViewModel as FullscreenEventViewModel
from gui.impl.lobby.pet_system.event_view import PetEvent as PetEvent
from gui.impl.pub import WindowImpl as WindowImpl
from frameworks.wulf import WindowFlags as WindowFlags

class FullscreenEventView(PetEvent):
    LAYOUT_ID: Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    def _updateData(self):
        ...
    def _getEvents(self):
        ...

class FullscreenEventViewWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
