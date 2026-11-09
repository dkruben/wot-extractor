# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/free_sheet_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import operator as operator
from gui.Scaleform.daapi.view.meta.FreeSheetPopoverMeta import FreeSheetPopoverMeta as FreeSheetPopoverMeta
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.server_events import events_dispatcher as events_dispatcher
from gui.server_events.events_helpers import AwardSheetPresenter as AwardSheetPresenter
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from personal_missions import PM_BRANCH as PM_BRANCH
from skeletons.gui.server_events import IEventsCache as IEventsCache

class FreeSheetPopover(FreeSheetPopoverMeta):
    __eventsCache: Any
    __ANIMATION_DELAY = 200
    __playAnimation: Any
    __branch: Any
    def __init__(self, ctx=None):
        ...
    def onTaskClick(self, idx):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __update(self, *_):
        ...
