# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/missions_token_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.view.meta.MissionsTokenPopoverMeta import MissionsTokenPopoverMeta as MissionsTokenPopoverMeta
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.impl import backport as backport
from gui.server_events.events_dispatcher import showMissionDetails as showMissionDetails
from gui.server_events.events_helpers import missionsSortFunc as missionsSortFunc
from gui.server_events.formatters import TOKEN_SIZES as TOKEN_SIZES
from gui.shared import events as events
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from helpers.i18n import makeString as ms
from skeletons.gui.server_events import IEventsCache as IEventsCache

class MissionsTokenPopover(MissionsTokenPopoverMeta):
    eventsCache: Any
    _tokenId: Any
    _questId: Any
    _token: Any
    def __init__(self, ctx=None):
        ...
    def onBuyBtnClick(self):
        ...
    def onQuestClick(self, idx):
        ...
    def _populate(self):
        ...
