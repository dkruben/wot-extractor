# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/platoon/platoon_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from UnitBase import BitfieldHelper as BitfieldHelper
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as _CAPS
from constants import MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.Scaleform.locale.PLATOON import PLATOON as PLATOON
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl
from helpers import dependency as dependency
from helpers import i18n as i18n
from items import vehicles as vehicles
from shared_utils import BitmaskHelper as BitmaskHelper
from skeletons.gui.game_control import IPlatoonController as IPlatoonController, IHangarGuiController as IHangarGuiController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any
Position: Any

class PreloadableWindow(WindowImpl):
    __preload: Any
    def __init__(self, wndFlags=..., content=None, decorator=None, layer=..., areaID=...):
        ...
    def preload(self):
        ...
    def _isPreloading(self):
        ...
    def _onContentReady(self):
        ...

class BonusState(BitmaskHelper):
    NO_BONUS = 0
    XP_BONUS = 1
    SQUAD_CREDITS_BONUS = 2
    PREM_CREDITS_BONUS = 4

def removeNationFromTechName(string):
    ...
def getNationFromTechName(string):
    ...
def convertTierFilterToList(tierFilter):
    ...
def isExpandedTierFilter(unitFilter, tierFilterList):
    ...
def getVehicleDescriptorByIntCD(vehicleIntCD):
    ...
def getQueueInfoByQueueType(queueInfo, queueType):
    ...
def formatSearchEstimatedTime(seconds):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPlatoonBonusState(isPlatoonCreated, lobbyCtx=None, hangarGuiCtrl=None, platoonCtrl=None):
    ...
