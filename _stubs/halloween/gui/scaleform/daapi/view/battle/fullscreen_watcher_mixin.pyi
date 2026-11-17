# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/scaleform/daapi/view/battle/fullscreen_watcher_mixin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import WindowStatus as WindowStatus, WindowLayer as WindowLayer
from halloween.gui.impl.battle.help_view import HelpWindow as HelpWindow
from halloween.gui.scaleform.daapi.view.battle.anomalies_watcher_mixin import AnomaliesWatcherMixin as AnomaliesWatcherMixin
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class FullscreenWatcherMixin(AnomaliesWatcherMixin):
    guiLoader: Any
    __ACTIVE_WINDOW_STATUSES: tuple
    __RESTRICTED_LAYERS: tuple
    __isWindowOverlapped: Any
    def __init__(self, *args, **kwargs):
        ...
    def updateVisibility(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onViewStatusChanged(self, _, newStatus):
        ...
