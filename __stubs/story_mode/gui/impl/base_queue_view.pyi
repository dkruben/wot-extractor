# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/base_queue_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from helpers import dependency as dependency
from gui.impl.pub import ViewImpl as ViewImpl
from shared_utils import safeCancelCallback as safeCancelCallback
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController

class BaseWaitQueueView(ViewImpl):
    __slots__: tuple
    storyModeCtrl: Any
    _timerCallback: Any
    def __init__(self, *args, **kwargs):
        ...
    def startWaitQueue(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onArenaCreated(self):
        ...
    def _stopTimer(self):
        ...
    def _onWaitQueueTimeout(self):
        ...
