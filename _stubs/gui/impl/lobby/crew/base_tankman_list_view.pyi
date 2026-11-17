# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/base_tankman_list_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from .base_crew_view import BaseCrewSoundView as BaseCrewSoundView
from gui.game_control import restore_contoller as restore_contoller
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.crew.tooltips.dismissed_toggle_tooltip import DismissedToggleTooltip as DismissedToggleTooltip
from gui.impl.lobby.crew.utils import playRecruitVoiceover as playRecruitVoiceover
from gui.server_events import recruit_helper as recruit_helper
from gui.shared.gui_items.Tankman import NO_SLOT as NO_SLOT
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
_START_CARDS_LIMIT = 50

class BaseTankmanListView(BaseCrewSoundView):
    appLoader: Any
    _itemsLimit: Any
    _itemsOffset: Any
    __sound: Any
    def __init__(self, settings):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    @property
    def _tankmenProvider(self):
        ...
    @property
    def _recruitsProvider(self):
        ...
    @property
    def _filterState(self):
        ...
    def _onTankmenBufferUpdated(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    # decorador original: @args2params(...)
    def _onTankmanRestore(self, tankmanID):
        ...
    # decorador original: @args2params(...)
    def _onLoadCards(self, limit, offset):
        ...
    def _fillVisibleCards(self, cardsList):
        ...
    def _fillTankmen(self, cardsList, limit, offset):
        ...
    def _fillRecruits(self, cardsList, limit, offset):
        ...
    def _fillTankmanCard(self, cardsList, tankman):
        ...
    def _fillRecruitCard(self, cardsList, recruitInfo):
        ...
    def _onPlayVoiceover(self, recruitID):
        ...
