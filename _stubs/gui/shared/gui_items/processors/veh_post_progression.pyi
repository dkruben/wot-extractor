# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/veh_post_progression.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showResearchConfirmDialog as showResearchConfirmDialog
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.processors import Processor as Processor, plugins as plugins, makeSuccess as makeSuccess
from gui.SystemMessages import pushMessage as pushMessage, SM_TYPE as SM_TYPE
from gui.veh_post_progression.messages import makeModificationErrorMsg as makeModificationErrorMsg, makeDiscardPairsMsg as makeDiscardPairsMsg, makeBuyPairMsg as makeBuyPairMsg, makePurchaseStepsMsg as makePurchaseStepsMsg, makeChangeSlotCategoryMsg as makeChangeSlotCategoryMsg, makeSetSlotCategoryMsg as makeSetSlotCategoryMsg, makePurchasePerksMsg as makePurchasePerksMsg
from gui.veh_post_progression.models.ext_money import EXT_MONEY_ZERO as EXT_MONEY_ZERO, getFullXPFromXPPrice as getFullXPFromXPPrice
from gui.veh_post_progression.sounds import playSound as playSound
from gui.veh_post_progression.sounds import Sounds as Sounds
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from post_progression_common import ACTION_TYPES as ACTION_TYPES, FEATURE_BY_GROUP_ID as FEATURE_BY_GROUP_ID
from gui.shared.gui_items import Vehicle as Vehicle

class PostProgressionProcessor(Processor):
    __slots__: tuple
    IS_GAMEFACE_SUPPORTED = True
    _vehicleCD: Any
    def __init__(self, vehicle):
        ...
    def _getVehicle(self):
        ...
    def _skipRentalIsOver(self):
        ...
    def __setupPlugins(self):
        ...

class ChangeVehicleSetupEquipments(PostProgressionProcessor):
    __slots__: tuple
    __groupID: Any
    __layoutIdx: Any
    def __init__(self, vehicle, groupID, layoutIdx):
        ...
    def _request(self, callback):
        ...
    def _skipRentalIsOver(self):
        ...

class SwitchPrebattleAmmoPanelAvailability(PostProgressionProcessor):
    __slots__: tuple
    __groupID: Any
    __enabled: Any
    __vehName: Any
    def __init__(self, vehicle, groupID, enabled):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class DiscardPairsProcessor(PostProgressionProcessor):
    __slots__: tuple
    __stepIDs: Any
    __modIDs: Any
    def __init__(self, vehicle, stepIDs, modIDs):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class PurchasePairProcessor(PostProgressionProcessor):
    __slots__: tuple
    __stepID: Any
    __modID: Any
    __discardMod: Any
    def __init__(self, vehicle, stepID, modificationID):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class PurchaseStepsProcessor(PostProgressionProcessor):
    __slots__: tuple
    __price: Any
    __stepIDs: Any
    def __init__(self, vehicle, stepIDs):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def __getPrice(self, vehicle):
        ...

class SetEquipmentSlotTypeProcessor(PostProgressionProcessor):
    __slots__: tuple
    __slotID: Any
    __isChange: Any
    def __init__(self, vehicle, slotID):
        ...
    def _request(self, callback):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class PurchaseVehSkillTreeStepsProcessor(PostProgressionProcessor):
    __stepIDs: Any
    __price: Any
    __responseDelayedCallback: Any
    __delay: Any
    __cbDelayer: Any
    def __init__(self, vehicle, stepIDs, responseDelayedCallback, delay):
        ...
    def _request(self, callback):
        ...
    def _response(self, code, callback, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def __getPrice(self, vehicle):
        ...
    def __getResearchedPerksText(self):
        ...
