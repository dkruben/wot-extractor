# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import typing as typing
import SoundGroups as SoundGroups
from goodies import goodie_constants as goodie_constants
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.gen.view_models.views.lobby.crew.help_navigate_from import HelpNavigateFrom as HelpNavigateFrom
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.crew.container_vews.quick_training.events import QuickTrainingViewEvents as QuickTrainingViewEvents
from gui.impl.lobby.crew.crew_sounds import SOUNDS as SOUNDS
from gui.shared import event_dispatcher as event_dispatcher
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Tankman import NO_SLOT as NO_SLOT, NO_TANKMAN as NO_TANKMAN
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID as NO_VEHICLE_ID
from gui.shared.gui_items.items_actions import factory as factory
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from typing import List as List, Tuple as Tuple, Callable as Callable
from Event import Event as Event
from gui.impl.lobby.container_views.base.events import ComponentEventsBase as ComponentEventsBase
_ACTION_KEY = 'action'
_ACTION_TYPE_KEY = 'actionType'
_ADD_KEY = 'add'
_PERCENT_KEY = 'percent'
CREW_BOOKS_PURCHASE_ENABLED = 'isCrewBooksPurchaseEnabled'
IS_MENTORING_LICENSE_ENABLED = 'isMentoringLicenseEnabled'
FREE_XP_STEPPER_ACTION: dict

class QuickTrainingInteractionController(InteractionController):
    lobbyContext: Any
    def _getEventsProvider(self):
        ...
    def _getEvents(self):
        ...
    def onInventoryUpdate(self, invDiff):
        ...
    def onGoodiesUpdate(self, diff):
        ...
    def onGlobalFreeXpChange(self):
        ...
    def onChangeTankman(self, tankmanID=..., slotIdx=...):
        ...
    def onEmptyWidgetSlotClick(self, _, slotIdx):
        ...
    @staticmethod
    def onAbout():
        ...
    def onCardMouseLeave(self):
        ...
    def _onServerSettingsChange(self, diff):
        ...
    def _onFreeXpMouseEnter(self):
        ...
    def _onFreeXpSelected(self, isSelected):
        ...
    def _onFreeXpStepperUpdate(self, data):
        ...
    def _onFreeXpManualInput(self, value):
        ...
    def _onBookSelected(self, bookId, count):
        ...
    def _onBookMouseEnter(self, bookId):
        ...
    @staticmethod
    def _onBuyBook(bookId):
        ...
    def _onLearn(self):
        ...
    def _onCancel(self):
        ...
    def _onMentoringClick(self):
        ...
    @staticmethod
    def _onPostProgression():
        ...
    def __clearAllSelection(self):
        ...
    def __updatePossibleCrewXp(self):
        ...
    def __refreshStepperWithAcquiringXp(self):
        ...
