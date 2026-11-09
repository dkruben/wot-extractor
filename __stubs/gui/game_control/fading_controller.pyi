# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/fading_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from gui.impl.common.fade_manager import FadeManager as FadeManager, DefaultFadingCover as DefaultFadingCover
from wg_async import wg_await as wg_await, wg_async as wg_async
from skeletons.gui.game_control import IFadingController as IFadingController

class FadingController(IFadingController):
    _managerByLayer: Any
    def __init__(self):
        ...
    # decorador original: @wg_async
    def show(self, layerID):
        ...
    # decorador original: @wg_async
    def hide(self, layerID):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def _hideImmediately(self):
        ...
    def _getFadeManager(self, layerID):
        ...
