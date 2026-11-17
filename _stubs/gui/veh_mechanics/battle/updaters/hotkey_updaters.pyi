# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/hotkey_updaters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import CommandMapping as CommandMapping
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater as ViewUpdater
HotKeyCommand: Any

class IHotKeysView(object):
    def setHotkeys(self, hotKeyCommands):
        ...

class HotKeysUpdater(ViewUpdater):
    def initialize(self):
        ...
    def finalize(self):
        ...
    def _onMappingChanged(self, *_):
        ...

class HotKeysViewUpdater(HotKeysUpdater):
    _DEFAULT_KEYS: tuple
    __commands: Any
    def __init__(self, commands, view):
        ...
    def _onMappingChanged(self, *_):
        ...
