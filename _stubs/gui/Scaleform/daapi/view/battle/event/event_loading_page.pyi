# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/event/event_loading_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.Scaleform.daapi.view.meta.EventLoadingMeta import EventLoadingMeta as EventLoadingMeta
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
PATH_BACKGROUNDS = '../maps/icons/event/loading/{0}_{1}.png'
LINKAGE_BACKGROUNDS = '{0}Page{1}UI'

class EventLoadingPage(EventLoadingMeta, IArenaLoadController):
    sessionProvider: Any
    _tutorialPages: Any
    def __init__(self, ctx):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def updateSpaceLoadProgress(self, progress):
        ...
    def _onDisconnected(self):
        ...
    @staticmethod
    def _getTutorialPageVO(pageId, bigSize):
        ...
