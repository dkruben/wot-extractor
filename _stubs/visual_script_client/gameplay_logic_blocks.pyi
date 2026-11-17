# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/gameplay_logic_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from inspect import getmembers as getmembers
from skeletons.gameplay import GameplayStateID as GameplayStateID, IGameplayLogic as IGameplayLogic
from visual_script import ASPECT as ASPECT
from visual_script.block import Meta as Meta, Block as Block, InitParam as InitParam
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.type import VScriptEnum as VScriptEnum
shared: Any
events: Any
dependency: Any
state_machine: Any
_logger: Any

class GameplayLogicMeta(Meta):
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

class GameplayStateIDEnum(VScriptEnum):
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
    def indexToName(cls, value):
        ...
    @classmethod
    def _vs_collectEnumEntries(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class GSMState(Block, GameplayLogicMeta, state_machine.BaseStateObserver):
    __gameplayLogic: Any
    _isStateActive: Any
    _onEnterState: Any
    _onExitState: Any
    _stateName: Any
    _state: Any
    def __init__(self, *args, **kwargs):
        ...
    def captionText(self):
        ...
    @classmethod
    def initParams(cls):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...

class OnPrebattleHighlights(Block, GameplayLogicMeta):
    _subscribe: Any
    _unsubscribe: Any
    _onStart: Any
    _onEnded: Any
    def __init__(self, *args, **kwargs):
        ...
    def onFinishScript(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onAnimationStarted(self, _):
        ...
    def __onAnimationEnded(self, _):
        ...
