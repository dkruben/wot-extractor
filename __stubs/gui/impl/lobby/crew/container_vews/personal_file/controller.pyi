# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
from gui.impl.dialogs.dialogs import showPerksDropDialog as showPerksDropDialog
from gui.impl.gen import R as R
from gui.impl.lobby.crew.container_vews.common.base_personal_case_controller import BasePersonalCaseController as BasePersonalCaseController
from gui.impl.lobby.crew.container_vews.personal_file.events import PersonalFileComponentViewEvents as PersonalFileComponentViewEvents
from gui.shared.event_dispatcher import showQuickTraining as showQuickTraining, showSkillsTraining as showSkillsTraining, showCrewPostProgressionView as showCrewPostProgressionView
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from wg_async import wg_async as wg_async, wg_await as wg_await
from typing import Callable as Callable, List as List, Tuple as Tuple
from gui.impl.lobby.container_views.base.events import ComponentEventsBase as ComponentEventsBase

class PersonalFileInteractionController(BasePersonalCaseController):
    __guiLoader: Any
    __isPerksResetDialogLoading = False
    __crewAssistSortSelection: Any
    def __init__(self, view=None):
        ...
    def setCrewAssistSortSelection(self, value):
        ...
    def getCrewAssistSortSelection(self):
        ...
    def _getEventsProvider(self):
        ...
    def _getEvents(self):
        ...
    def _onSkillClick(self, tankmanInvID, role):
        ...
    def _onSkillsTrained(self, tankmanID):
        ...
    def _onSetAnimationInProgress(self, isEnabled):
        ...
    def _onIncreaseClick(self):
        ...
    # decorador original: @wg_async
    def _onResetClick(self, tankmanID):
        ...
    def _onWidgetClick(self):
        ...
    def _onCacheResync(self, reason, _):
        ...
    def onChangeTankman(self, tankmanID):
        ...
    def onStopAnimations(self):
        ...
