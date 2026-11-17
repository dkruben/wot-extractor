# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/pet_system_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import skeletons.gui.pet_system
from pet_system_common.pet_constants import AnimationStateName as AnimationStateName, PetHangarObject as PetHangarObject, PetStateBehavior as PetStateBehavior, PetStaticTrigger as PetStaticTrigger, PetTrigger as PetTrigger, StorageStaticTrigger as StorageStaticTrigger
from visual_script.misc import EDITOR_TYPE as EDITOR_TYPE
from visual_script.type import VScriptEnum as VScriptEnum
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script import ASPECT as ASPECT
from visual_script.block import Block as Block, Meta as Meta
from visual_script.dependency import dependencyImporter as dependencyImporter
Event: Any
dependency: Any
game_control: Any
shared: Any
events: Any
event_dispatcher: Any
lobby_entry: Any
ps_states: Any
state_machine: Any
GenericComponents: Any
guiShared: Any

class PetSystemMeta(Meta):
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

class OnEventShow(Block, PetSystemMeta):
    __petController: Any
    _in: Any
    _fullscreenNeeded: Any
    _out: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class OnFirstClickSend(Block, PetSystemMeta):
    __petController: Any
    _in: Any
    _out: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class OnPetStorageOpen(Block, PetSystemMeta):
    __petController: Any
    _in: Any
    _out: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class IsInPetStorageView(Block, PetSystemMeta):
    __petController: Any
    _state: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class IsInPetFullscreenEventView(Block, PetSystemMeta):
    __petController: Any
    _state: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class PetTriggerEnum(VScriptEnum):
    @classmethod
    def vs_name(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def nameToIndex(cls, value):
        ...
    @classmethod
    def _vs_collectEnumEntries(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class StorageStaticTriggerEnum(VScriptEnum):
    @classmethod
    def vs_name(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class PetStaticTriggerEnum(VScriptEnum):
    @classmethod
    def vs_name(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class AnimationStateNameEnum(VScriptEnum):
    @classmethod
    def vs_name(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def nameToIndex(cls, value):
        ...
    @classmethod
    def _vs_collectEnumEntries(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class GetPetState(Block, PetSystemMeta):
    __petController: Any
    _state: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class OnStateChanged(Block, PetSystemMeta):
    __petController: Any
    _out: Any
    _state: Any
    def __init__(self, agent):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onUpdatePetState(self, state):
        ...

class OnPetAnimationTriggered(Block, PetSystemMeta):
    __petController: Any
    _out: Any
    _trigger: Any
    def __init__(self, agent):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onTrigger(self, trigger):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onPetSequence(self, event):
        ...

class GetStorageStaticTrigger(Block, PetSystemMeta):
    __petController: Any
    _staticTrigger: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class OnStorageStaticTriggerChanged(Block, PetSystemMeta):
    __petController: Any
    _out: Any
    _staticTrigger: Any
    def __init__(self, agent):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onUpdateStorageStaticTrigger(self, staticTrigger):
        ...

class GetPetStaticTrigger(Block, PetSystemMeta):
    __petController: Any
    _staticTrigger: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class OnPetStaticTriggerChanged(Block, PetSystemMeta):
    __petController: Any
    _out: Any
    _staticTrigger: Any
    def __init__(self, agent):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onUpdatePetStaticTrigger(self, staticTrigger):
        ...

class GetSynergy(Block, PetSystemMeta):
    __petController: Any
    _synergy: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class GetIsFirstClickAvailable(Block, PetSystemMeta):
    __petController: Any
    _isAvailable: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class OnSynergyChanged(Block, PetSystemMeta):
    __petController: Any
    _out: Any
    _synergy: Any
    def __init__(self, agent):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onUpdatePetSynergy(self, synergy):
        ...

class OnPetObjectHover(Block, PetSystemMeta):
    _in: Any
    _out: Any
    _isHoverIn: Any
    _objectName: Any
    def __init__(self, agent):
        ...
    def _execute(self):
        ...

class OnPetCanInteractInHangarStateChanged(Block, PetSystemMeta):
    __petController: Any
    _out: Any
    _canInteract: Any
    def __init__(self, agent):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _execute(self):
        ...
    def _onUpdateCanInteractInHangar(self, canInteract):
        ...
