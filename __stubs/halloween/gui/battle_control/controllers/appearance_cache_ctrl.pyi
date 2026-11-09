# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/gui/battle_control/controllers/appearance_cache_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
from gui.battle_control.controllers.appearance_cache_ctrls.default_appearance_cache_ctrl import DefaultAppearanceCacheController as DefaultAppearanceCacheController
from helpers import uniprof as uniprof
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from vehicle_outfit.outfit import Outfit as Outfit
from vehicle_systems.camouflages import getOutfitComponent as getOutfitComponent
from vehicle_systems.tankStructure import ModelStates as ModelStates
from vehicle_systems.vehicle_damage_state import VehicleDamageState as VehicleDamageState
from vehicle_systems import model_assembler as model_assembler
from vehicle_systems import camouflages as camouflages
from vehicle_systems.tankStructure import ModelsSetParams as ModelsSetParams
_logger: Any

class HalloweenAppearanceCacheController(DefaultAppearanceCacheController):
    _spawnList: Any
    def __init__(self, setup):
        ...
    def startControl(self, battleCtx, arenaVisitor):
        ...
    def stopControl(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def updateSpawnList(self, spawnListData):
        ...
    @staticmethod
    def collectPrerequisitesForEventBattle(typeDescriptor, outfit, spaceID, isTurretDetached, damageState):
        ...
