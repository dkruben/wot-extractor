# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/techtree/settings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple, defaultdict as defaultdict
from future.utils import viewitems as viewitems
import nations as nations
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui.Scaleform.genConsts.NODE_STATE_FLAGS import NODE_STATE_FLAGS as NODE_STATE_FLAGS
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES as GUI_ITEM_TYPE_NAMES
from items import getTypeInfoByName as getTypeInfoByName
from items.vehicles import VEHICLE_CLASS_TAGS as VEHICLE_CLASS_TAGS
__all__: tuple
TREE_SHARED_REL_FILE_PATH = 'gui/flash/techtree/tree-shared.xml'
NATION_TREE_REL_FILE_PATH = 'gui/flash/techtree/{}-tree.xml'
NATION_TREE_REL_PREMIUM_FILE_PATH = 'gui/flash/techtree/{}-premium.xml'
NODE_ORDER_PREFIX_COMMON = 0
NODE_ORDER_PREFIX_PREMIUM = 1
_VEHICLE_TYPE_NAME: Any
RESEARCH_ITEMS: tuple
MAX_PATH_LIMIT = 5
UNKNOWN_VEHICLE_LEVEL = -1
DEFAULT_UNLOCK_PROPS: Any
BpfProps: Any
_DEFAULT_BPF_PROPS: Any

class NODE_STATE(object):
    @classmethod
    def add(cls, state, flag):
        ...
    @classmethod
    def addIfNot(cls, state, flag):
        ...
    @classmethod
    def remove(cls, state, flag):
        ...
    @classmethod
    def removeIfHas(cls, state, flag):
        ...
    @classmethod
    def isNext2Unlock(cls, state):
        ...
    @classmethod
    def isAvailable2Unlock(cls, state):
        ...
    @classmethod
    def isUnlocked(cls, state):
        ...
    @classmethod
    def inInventory(cls, state):
        ...
    @classmethod
    def isVehicleCanBeChanged(cls, state):
        ...
    @classmethod
    def isInstalled(cls, state):
        ...
    @classmethod
    def isAvailable2Buy(cls, state):
        ...
    @classmethod
    def isAvailable2Sell(cls, state):
        ...
    @classmethod
    def isWasInBattle(cls, state):
        ...
    @classmethod
    def isPremium(cls, state):
        ...
    @classmethod
    def isCollectible(cls, state):
        ...
    @classmethod
    def isActionVehicle(cls, state):
        ...
    @classmethod
    def isCollectibleActionVehicle(cls, state):
        ...
    @classmethod
    def isBuyForCredits(cls, state):
        ...
    @classmethod
    def isBuyForGold(cls, state):
        ...
    @classmethod
    def setNext2Unlock(cls, state):
        ...
    @classmethod
    def change2Unlocked(cls, state):
        ...
    @classmethod
    def changeLast2Buy(cls, state, isLast2Buy):
        ...
    @classmethod
    def isRentalOver(cls, state):
        ...
    @classmethod
    def isRestoreAvailable(cls, state):
        ...
    @classmethod
    def isRentAvailable(cls, state):
        ...
    @classmethod
    def canTradeIn(cls, state):
        ...
    @classmethod
    def canTradeOff(cls, state):
        ...
    @classmethod
    def isAnnouncement(cls, state):
        ...
    @classmethod
    def hasBlueprints(cls, state):
        ...
    @classmethod
    def printStates(cls, state):
        ...

# base nao representavel no stub: namedtuple(...)
class UnlockStats:
    def isUnlocked(self, nodeCD):
        ...
    def isSeqUnlocked(self, seq):
        ...
    def getVehXP(self, nodeCD):
        ...
    def getVehTotalXP(self, nodeCD):
        ...

# base nao representavel no stub: namedtuple(...)
class UnlockProps:
    __slots__: tuple
    def makeTuple(self):
        ...

class SelectedNation(object):
    __slots__: tuple
    __index = None
    @classmethod
    def byDefault(cls):
        ...
    @classmethod
    def select(cls, index):
        ...
    @classmethod
    def getIndex(cls):
        ...
    @classmethod
    def getName(cls):
        ...
    @classmethod
    def clear(cls):
        ...

class RequestState(object):
    __slots__: tuple
    __states: Any
    @classmethod
    def sent(cls, name):
        ...
    @classmethod
    def received(cls, name):
        ...
    @classmethod
    def inProcess(cls, name):
        ...

class VehicleClassInfo(object):
    __slots__: tuple
    __info: Any
    def __init__(self):
        ...
    def getInfoByTags(self, tags):
        ...
    def clear(self):
        ...
