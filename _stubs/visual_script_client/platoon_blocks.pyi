# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/platoon_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from visual_script.block import Meta as Meta, Block as Block
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
dependency: Any
shared: Any
events: Any

class PlatoonMeta(Meta):
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

class OnPlatoonStateChanged(Block, PlatoonMeta):
    _PLAYER_INDEX = -1
    _platoonController: Any
    _subscribe: Any
    _unsubscribe: Any
    _subscribeOut: Any
    _unsubscribeOut: Any
    _onPlatoonEnter: Any
    _onPlatoonExit: Any
    _onPlayerEnter: Any
    _onPlayerExit: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onPlatoonTankEnter(self, event):
        ...
    def __onPlatoonTankLeave(self, event):
        ...
    def __enablePlatoonLighting(self, isEnabled):
        ...
