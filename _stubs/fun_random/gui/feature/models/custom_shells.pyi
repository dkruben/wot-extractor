# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/models/custom_shells.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from items import vehicles as vehicles
from gui.shared.gui_items.vehicle_modules import Shell as Shell
from fun_random.gui.feature.configs.sub_modes.custom_shells import FunSubModeCustomShellConfigModel as FunSubModeCustomShellConfigModel, FunSubModeCustomShellSlotConfigModel as FunSubModeCustomShellSlotConfigModel, FunSubModeCustomShellLayoutConfigModel as FunSubModeCustomShellLayoutConfigModel, FunSubModeCustomShellsConfigModel as FunSubModeCustomShellsConfigModel

class FunCustomShell(object):
    intCD: Any
    count: Any
    imageName: Any
    def __init__(self, intCD, count, imageName):
        ...
    @classmethod
    def fromShellItem(cls, shell):
        ...
    @classmethod
    def fromCustomShellConfig(cls, shellConfig, count):
        ...

class FunCustomShellSlot(object):
    __slotConfig: Any
    __customShell: Any
    __originalIndex: Any
    def __init__(self, slotConfig, customShell, originalIndex):
        ...
    @classmethod
    def fromShellItem(cls, customShellsConfig, layoutConfig, shell):
        ...
    @classmethod
    def fromCustomLayoutConfig(cls, customShellsConfig, layoutConfig):
        ...
    @property
    def originalIndex(self):
        ...
    @property
    def command(self):
        ...
    @property
    def shell(self):
        ...
    @property
    def imageNameOverride(self):
        ...
    @property
    def tooltipOverride(self):
        ...
