# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/manual/manual_main_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers import AccountSettings as AccountSettings
from gui.Scaleform.daapi.view.meta.ManualMainViewMeta import ManualMainViewMeta as ManualMainViewMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, event_dispatcher as shared_events
from gui.Scaleform.daapi.view.lobby.manual.manual_view_base import ManualViewBase as ManualViewBase
_logger: Any

class ManualMainView(ManualViewBase, ManualMainViewMeta):
    @staticmethod
    def addCounter(param):
        ...
    def closeView(self):
        ...
    def onChapterOpenedS(self, chapterIndex):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onChapterClosed(self, _):
        ...
