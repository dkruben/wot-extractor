# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/personal/tank_girls_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.server_events.events_dispatcher import showTankwomanAward as showTankwomanAward
from gui.shared.formatters import text_styles as text_styles
from gui.Scaleform.daapi.view.meta.TankgirlsPopoverMeta import TankgirlsPopoverMeta as TankgirlsPopoverMeta
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS as PERSONAL_MISSIONS
from gui.server_events import events_helpers as events_helpers
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache

class TankgirlsPopover(TankgirlsPopoverMeta):
    __eventsCache: Any
    def onRecruitClick(self, idx):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __update(self):
        ...
    def __getMissionAward(self, eventID):
        ...
    def __onQuestsUpdated(self, *args):
        ...
