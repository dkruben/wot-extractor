# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/battle_hud_block.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from visual_script import ASPECT as ASPECT
from visual_script.block import Meta as Meta, Block as Block
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import errorVScript as errorVScript
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
helpers: Any
dependency: Any
Math: Any

class BattleHUDMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    @property
    def _avatar(self):
        ...

class BattleHUDEventMeta(BattleHUDMeta):
    @classmethod
    def blockIcon(cls):
        ...

class OnShowMessage(BattleHUDEventMeta, Block):
    _active: Any
    _onVehicleMessage: Any
    _onVehicleError: Any
    _onPlayerMessage: Any
    _key: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def validate(self):
        ...
    @property
    def active(self):
        ...
    def __onShowVehicleErrorByKey(self, key, args=None, extra=None):
        ...
    def __onShowVehicleMessageByKey(self, key, args=None, extra=None):
        ...
    def __onShowPlayerMessageByKey(self, key, args=None, extra=None):
        ...
    def __onShowVehicleMessageByCode(self, code, postfix, entityID, extra, equipmentID, ignoreMessages):
        ...
    def __onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID, ignoreMessages):
        ...

class ShowVehicleErrorMessage(Block, BattleHUDEventMeta):
    _in: Any
    _keySlot: Any
    _paramsSlot: Any
    _out: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
