# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/crew_post_progression_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.crew_post_progression_view_model import CrewPostProgressionViewModel as CrewPostProgressionViewModel, PauseReasonType as PauseReasonType
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils import decorators as decorators
from gui.shared.gui_items.processors.common import ClaimRewardForPostProgression as ClaimRewardForPostProgression
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.impl.auxiliary.crew_books_helper import crewBooksViewedCache as crewBooksViewedCache
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from .crew_sounds import CREW_SOUND_OVERLAY_SPACE as CREW_SOUND_OVERLAY_SPACE
from PlayerEvents import g_playerEvents as g_playerEvents

class CrewPostProgressionView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    gui: Any
    _COMMON_SOUND_SPACE = CREW_SOUND_OVERLAY_SPACE
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __amountXpForBook(self):
        ...
    def __setPause(self, vm):
        ...
    def __onUpdateXpp(self, *args):
        ...
    def __updateCountAndProgression(self, vm):
        ...
    # decorador original: @decorators.adisp_process(...)
    def __onClaim(self):
        ...
    def __onDisconnected(self):
        ...

class CrewPostProgressionWindow(WindowImpl):
    def __init__(self, parent=None):
        ...
