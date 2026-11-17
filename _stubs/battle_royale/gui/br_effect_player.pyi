# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/br_effect_player.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
import GenericComponents as GenericComponents
from helpers import dependency as dependency
from battle_royale.gui.battle_control.controllers.progression_ctrl import IProgressionListener as IProgressionListener
from gui.battle_control.view_components import IViewComponentsCtrlListener as IViewComponentsCtrlListener
from helpers import time_utils as time_utils
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
_logger: Any

class BRUpgradeEffectPlayer(IProgressionListener, IViewComponentsCtrlListener):
    __dynObjectsCache: Any
    __sessionProvider: Any
    __UPGRADE_INVALIDATION_TIME = 3
    __effectConfig: Any
    __upgradeStarted: Any
    def __init__(self):
        ...
    def detachedFromCtrl(self, ctrlID):
        ...
    def setVehicleVisualChangingStarted(self, vehicleID):
        ...
    def setVehicleVisualChangingFinished(self, vehicleID):
        ...
    def __playEffect(self, vehicleID):
        ...
