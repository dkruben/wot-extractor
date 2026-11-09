# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/configs/sub_modes/custom_shells.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from dict2model import fields as fields, models as models, schemas as schemas
from fun_random.gui.feature.fun_constants import FunCustomShellsSource as FunCustomShellsSource
funSubModeCustomShellSchema: Any
funSubModeCustomShellSlotSchema: Any
funSubModeCustomShellLayoutSchema: Any
funSubModeCustomShellsSchema: Any

class FunSubModeCustomShellConfigModel(models.Model):
    __slots__: tuple
    intCD: Any
    def __init__(self, intCD):
        ...

class FunSubModeCustomShellSlotConfigModel(models.Model):
    __slots__: tuple
    command: Any
    imageOverride: Any
    tooltipOverride: Any
    def __init__(self, command, imageOverride, tooltipOverride):
        ...

class FunSubModeCustomShellLayoutConfigModel(models.Model):
    __slots__: tuple
    shellSource: Any
    shellIndex: Any
    shellCount: Any
    slotIndex: Any
    def __init__(self, shellSource, shellIndex, shellCount, slotIndex):
        ...

class FunSubModeCustomShellsConfigModel(models.Model):
    __slots__: tuple
    shells: Any
    slots: Any
    layouts: Any
    def __init__(self, shells=None, slots=None, layouts=None):
        ...
    @property
    def exists(self):
        ...
