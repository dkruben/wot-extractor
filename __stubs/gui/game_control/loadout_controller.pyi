# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/loadout_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event, EventManager as EventManager
from skeletons.gui.game_control import ILoadoutController as ILoadoutController
from wg_async import wg_async as wg_async, await_callback as await_callback

class LoadoutController(ILoadoutController):
    __eManager: Any
    onSlotSelected: Any
    onInteractorUpdated: Any
    onUpdateFromItem: Any
    onResetItem: Any
    onSpecializationSelect: Any
    __interactor: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    @property
    def interactor(self):
        ...
    def clearInteractor(self):
        ...
    def setInteractor(self, interactor):
        ...

# decorador original: @wg_async
def updateInteractor(interactor, confirmed, rollback):
    ...
