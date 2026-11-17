# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/processors/tankman.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
from gui import SystemMessages as SystemMessages, makeHtmlString as makeHtmlString
from gui.SystemMessages import CURRENCY_TO_SM_TYPE as CURRENCY_TO_SM_TYPE, SM_TYPE as SM_TYPE
from gui.game_control.restore_contoller import getTankmenRestoreInfo as getTankmenRestoreInfo
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import formatPrice as formatPrice, formatPriceValue as formatPriceValue
from gui.shared.gui_items import Tankman as Tankman
from gui.shared.gui_items.Tankman import BaseBookConvertingFormatter as BaseBookConvertingFormatter, NO_SLOT as NO_SLOT, getTankmanSkill as getTankmanSkill
from gui.shared.gui_items.processors import GroupedRequestProcessor as GroupedRequestProcessor, ItemProcessor as ItemProcessor, Processor as Processor, makeError as makeError, makeI18nError as makeI18nError, makeI18nSuccess as makeI18nSuccess, makeSuccess as makeSuccess, plugins as plugins
from gui.shared.gui_items.processors.plugins import AutoReturnValidator as AutoReturnValidator
from gui.shared.money import Currency as Currency, Money as Money
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils.role_presenter_helper import getRoleUserName as getRoleUserName
from helpers import dependency as dependency
from items import makeIntCompactDescrByID as makeIntCompactDescrByID, tankmen as tankmen
from items.tankmen import SKILL_INDICES as SKILL_INDICES
from skeletons.gui.game_control import IRestoreController as IRestoreController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class TankmanDismiss(ItemProcessor):
    restore: Any
    def __init__(self, tankman):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class TankmanRecruit(Processor):
    vehicle: Any
    nationID: Any
    vehTypeID: Any
    role: Any
    tmanCostTypeIdx: Any
    def __init__(self, nationID, vehTypeID, role, tmanCostTypeIdx):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class TankmanTokenRecruit(Processor):
    nationID: Any
    vehTypeID: Any
    role: Any
    tokenName: Any
    recruitInfo: Any
    vehicleName: Any
    def __init__(self, nationID, vehTypeID, role, tokenName, tokenData):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class TankmanEquip(GroupedRequestProcessor):
    __tankmanInvID: Any
    _vehicleInvID: Any
    __vehicleSlotIdx: Any
    _sysMsgPrefix: Any
    def __init__(self, tankmanInvID, vehicleInvID, vehicleSlotIdx, groupID=0, groupSize=1):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class QuickServiceTankmanEquip(TankmanEquip):
    def _successHandler(self, code, ctx=None):
        ...

class TankmanRecruitAndEquip(Processor):
    vehicle: Any
    slot: Any
    tmanCostTypeIdx: Any
    isReplace: Any
    def __init__(self, vehicle, slot, tmanCostTypeIdx):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def __getSysMsgPrefix(self):
        ...

class CrewSkinsProcessorBase(Processor):
    _tmanInvID: Any
    def __init__(self, tmanInvID):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class CrewSkinUnequip(CrewSkinsProcessorBase):
    def _request(self, callback):
        ...

class CrewSkinEquip(CrewSkinsProcessorBase):
    __skinID: Any
    def __init__(self, tmanInvID, skinID):
        ...
    def _request(self, callback):
        ...

class TankmanUnload(GroupedRequestProcessor):
    __vehicleInvID: Any
    __vehicleSlotIdx: Any
    def __init__(self, vehicleInvID, vehicleSlotIdx=..., groupID=0, groupSize=1):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    @staticmethod
    def __sysMsgPrefix(ctx):
        ...
    @staticmethod
    def __tmanQuantity(ctx):
        ...

class TankmanReturn(Processor):
    __vehicle: Any
    def __init__(self, vehicle, validators=None):
        ...
    @property
    def vehicle(self):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None, **kwargs):
        ...
    def _request(self, callback):
        ...

class TankmanAutoReturn(TankmanReturn):
    validator: Any
    def __init__(self, vehicle, validators=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class ResetAllTankmenSkills(Processor):
    __PREFIX = 'reset_all_tankmen_skills'
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...

class TankmanRetraining(GroupedRequestProcessor):
    __tankmanInvID: Any
    __vehicleIntCD: Any
    __tmanCostTypeIdx: Any
    __tmanCost: Any
    __isRoleChange: Any
    def __init__(self, tankmanInvID, vehicleIntCD, tmanCostTypeIdx, isRoleChange, groupID=0, groupSize=1):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def __sysMessagePrefix(self, ctx):
        ...

class TankmanFreeToOwnXpConvertor(GroupedRequestProcessor):
    __tankmanInvID: Any
    __selectedXpForConvert: Any
    def __init__(self, tankmanInvID, selectedXpForConvert, groupID=0, groupSize=1):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class TankmanAddSkills(ItemProcessor):
    skillNames: Any
    skillsRole: Any
    utilizationType: Any
    def __init__(self, tmanInvID, utilizationType, skillsRole, skillNames):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def __getSysMsgKey(self):
        ...

class TankmanAddSkill(ItemProcessor):
    utilizationType: Any
    skillName: Any
    def __init__(self, tmanInvID, skillName, utilizationType):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class TankmanChangeRole(GroupedRequestProcessor):
    __roleIdx: Any
    __vehTypeCompDescr: Any
    __changeRoleCost: Any
    __vehSlotIdx: Any
    __vehicle: Any
    __retrainVehicle: Any
    def __init__(self, tankmanInvID, role, vehTypeCompDescr, vehSlotIdx=-1, groupID=0, groupSize=1):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...

class TankmanDropSkills(ItemProcessor):
    dropSkillCostIdx: Any
    def __init__(self, tankman, dropSkillCostIdx):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...
    def __getTankmanSysMsgType(self, dropSkillCostIdx):
        ...

class TankmanChangePassport(ItemProcessor):
    firstNameID: Any
    firstNameGroup: Any
    lastNameID: Any
    lastNameGroup: Any
    iconID: Any
    iconGroup: Any
    isFemale: Any
    isPremium: Any
    def __init__(self, tankmanInvID, firstNameID, firstNameGroup, lastNameID, lastNameGroup, iconID, iconGroup):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _request(self, callback):
        ...
    @classmethod
    def __hasUniqueData(cls, tankman, firstNameID, lastNameID, iconID):
        ...

class TankmanRestore(GroupedRequestProcessor):
    __tankmanInvID: Any
    __restorePrice: Any
    def __init__(self, tankman, groupID=0, groupSize=1):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

class TankmenJunkConverter(Processor):
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...
    def _request(self, callback):
        ...

class TransferTankmanXP(Processor, BaseBookConvertingFormatter):
    sourceID: Any
    targetID: Any
    def __init__(self, sourceID, targetID):
        ...
    def _request(self, callback):
        ...
    def _errorHandler(self, code, errStr='', ctx=None):
        ...
    def _successHandler(self, code, ctx=None):
        ...

def _getSysMsgType(price):
    ...
def _getFinancialTransactionSysMsgType(price):
    ...
def _getRecruitPrice(tmanCostTypeIdx):
    ...
