# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/notification/actions_handlers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from comp7.gui.prb_control.entities import comp7_prb_helpers as comp7_prb_helpers
from comp7.gui.shared.event_dispatcher import showComp7BanWindow as showComp7BanWindow
from comp7.gui.shared.event_dispatcher import showComp7MetaRootTab as showComp7MetaRootTab, showComp7AllRewardsSelectionWindow as showComp7AllRewardsSelectionWindow
from constants import PENALTY_TYPES as PENALTY_TYPES, FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA as FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA, ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from gui.shared import event_dispatcher as shared_events
from helpers import dependency as dependency
from notification.actions_handlers import NavigationDisabledActionHandler as NavigationDisabledActionHandler, _OpenPunishmentWindowHandler as _OpenPunishmentWindowHandler
from notification.settings import NOTIFICATION_TYPE as NOTIFICATION_TYPE
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IComp7Controller as IComp7Controller, IHangarSpaceSwitchController as IHangarSpaceSwitchController

class OpenComp7ShopHandler(NavigationDisabledActionHandler):
    __comp7Controller: Any
    __spaceSwitchController: Any
    __customizationService: Any
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...
    def __onC11nVisibilityChanged(self, isC11nVisible):
        ...
    def __onSpaceUpdated(self):
        ...
    def __goToShop(self):
        ...

class OpenBondEquipmentSelection(NavigationDisabledActionHandler):
    @classmethod
    def getNotType(cls):
        ...
    @classmethod
    def getActions(cls):
        ...
    def doAction(self, model, entityID, action):
        ...

class Comp7OpenPunishmentWindowHandler(_OpenPunishmentWindowHandler):
    def handleAction(self, model, entityID, action):
        ...
