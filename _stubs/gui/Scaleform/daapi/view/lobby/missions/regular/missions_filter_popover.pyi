# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/missions_filter_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings, MISSIONS_PAGE as MISSIONS_PAGE
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import HIDE_DONE as HIDE_DONE, HIDE_UNAVAILABLE as HIDE_UNAVAILABLE
from gui.Scaleform.daapi.view.meta.MissionsFilterPopoverViewMeta import MissionsFilterPopoverViewMeta as MissionsFilterPopoverViewMeta
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import MissionsEvent as MissionsEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers.i18n import makeString as _ms

class MissionsFilterPopoverView(MissionsFilterPopoverViewMeta):
    __filterData: Any
    def __init__(self, ctx=None):
        ...
    def changeFilter(self, hideUnavailable, hideDone):
        ...
    def setDefaultFilter(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getInitialVO(self):
        ...
