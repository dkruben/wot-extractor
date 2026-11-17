# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/hw_helpers/bestiary_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from halloween.gui.halloween_account_settings import setSettings as setSettings, AccountSettingsKeys as AccountSettingsKeys, getSettings as getSettings
from halloween.gui.hw_vehicle_role_helper import getVehicleRole as getVehicleRole
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController as IHalloweenArtefactsController
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
from halloween_common.configs.halloween_bestiary import EnemyModel as EnemyModel
from typing import Optional as Optional
from vehicle_outfit.outfit import Outfit as Outfit

def getEnemyRole(enemyType):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getOutfit(styleID, vehIntCD, c11nService=None, itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getUnlockMissionIdx(enemy, hwArtefactsCtrl=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isEnemyUnlocked(enemy, hwArtefactsCtrl=None):
    ...
def getLastSelectedEnemy():
    ...
def setLastSelectedEnemy(enemyIntCD):
    ...
def getEnemiesSeenList():
    ...
def markEnemyAsSeen(enemyIntCD):
    ...
