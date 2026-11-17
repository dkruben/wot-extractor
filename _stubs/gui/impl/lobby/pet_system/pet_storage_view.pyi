# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/pet_system/pet_storage_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from itertools import chain as chain
from adisp import adisp_process as adisp_process
from frameworks.wulf import WindowFlags as WindowFlags
from frameworks.wulf.view.array import fillStringsArray as fillStringsArray
from gui.game_control.links import URLMacros as URLMacros
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.pet_system.pet_card_model import PetCardModel as PetCardModel
from gui.impl.gen.view_models.views.lobby.pet_system.pet_name_model import PetNameModel as PetNameModel
from gui.impl.gen.view_models.views.lobby.pet_system.pet_storage_view_model import PetStorageViewModel as PetStorageViewModel, SynergyStateEnum as SynergyStateEnum, VisibilityStateEnum as VisibilityStateEnum
from gui.impl.lobby.pet_system.tooltips.synergy_tooltip import SynergyTooltip as SynergyTooltip
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.pet_system.bonus_helper import BonusItem as BonusItem
from gui.pet_system.pet_item_helper import PetItem as PetItem, PromoPetItem as PromoPetItem
from gui.pet_system.pet_ui_settings import PetUISettings as PetUISettings
from gui.pet_system.processor import SelectActivePetProcessor as SelectActivePetProcessor, SelectPetActiveBonusProcessor as SelectPetActiveBonusProcessor, SelectPetNameProcessor as SelectPetNameProcessor, SelectPetStateProcessor as SelectPetStateProcessor
from gui.pet_system.synergy_helper import SynergyItem as SynergyItem
from gui.server_events.events_dispatcher import showMissions as showMissions
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared import events as events_constants
from gui.shared import g_eventBus as g_eventBus
from gui.shared.event_dispatcher import showPetInfoPage as showPetInfoPage, showShop as showShop, showHangar as showHangar
from helpers import dependency as dependency
from pet_system_common import pet_constants as pet_constants
from pet_system_common.PetPromoConfig import PromoSource as PromoSource
from pet_system_common.pet_constants import PetStateBehavior as PetStateBehavior
from shared_utils import first as first
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.pet_system import IPetSystemController as IPetSystemController
_logger: Any
STATE_MAPPING: dict
MODEL_STATE_MAPPING: dict

class PetStorageView(ViewComponent):
    LAYOUT_ID: Any
    __petController: Any
    lobbyContext: Any
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def closeWindow(self):
        ...
    def __onClose(self):
        ...
    def __update(self):
        ...
    def __setActivePet(self, petId=None):
        ...
    def __updatePetData(self, petId=None):
        ...
    def __getSynergyState(self, petID):
        ...
    def __markPromoAsSeen(self, petId, model):
        ...
    def __updateBonuses(self):
        ...
    def __updateBonusCount(self):
        ...
    def __updateCards(self):
        ...
    def __updateNameList(self):
        ...
    def __setNames(self, petNames, nameIDs, isNew=False):
        ...
    @staticmethod
    def __sortNames(nameIDs):
        ...
    # decorador original: @adisp_process
    def __onPetSelect(self, args):
        ...
    # decorador original: @adisp_process
    def __onBonusSelect(self, args):
        ...
    def __onCardSelect(self, args):
        ...
    # decorador original: @adisp_process
    def __updatePetName(self, args):
        ...
    def __updateSeenNames(self):
        ...
    # decorador original: @adisp_process
    def __updateStateBehavior(self, args):
        ...
    @staticmethod
    def __openInfoPage():
        ...
    def __tryToShowEvent(self):
        ...
    def __onUpdateUnlockedPetsIDs(self, *_):
        ...
    def __onUpdateSynergy(self, *_):
        ...
    def __onUpdateActivePet(self, petID):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    # decorador original: @adisp_process
    def __onToPurchase(self):
        ...
    def __onToGameView(self):
        ...

class PetStorageViewWindow(WindowImpl):
    def __init__(self, layer, **kwargs):
        ...
