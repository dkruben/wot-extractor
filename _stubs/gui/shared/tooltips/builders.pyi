# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/tooltips/builders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import importlib as importlib
import logging as logging
from typing import Any as Any
from gui.Scaleform.daapi.settings.config import ADVANCED_COMPLEX_TOOLTIPS as ADVANCED_COMPLEX_TOOLTIPS
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.shared.gui_items.artefacts import OptionalDevice as OptionalDevice
from gui.shared.tooltips import complex_formatters as complex_formatters
from gui.shared.tooltips import contexts as contexts, advanced as advanced
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from soft_exception import SoftException as SoftException
_logger: _Any
DISABLED_ITEMS_ID = 12793

class TooltipBuilder(object):
    __slots__: tuple
    _tooltipType: _Any
    _linkage: _Any
    _provider: _Any
    def __init__(self, tooltipType, linkage):
        ...
    @property
    def tooltipType(self):
        ...
    @property
    def linkage(self):
        ...
    @property
    def provider(self):
        ...
    def build(self, stateType, advanced_, *args, **kwargs):
        ...
    def supportAdvanced(self, tooltipType, *args):
        ...

class SimpleBuilder(TooltipBuilder):
    __slots__: tuple
    def build(self, stateType, advanced_, *args, **kwargs):
        ...

class AdvancedBuilder(TooltipBuilder):
    __settingsCore: _Any
    def _getDisableAnimFlag(self):
        ...
    def _setDisableAnimFlag(self):
        ...

class DataBuilder(SimpleBuilder):
    __slots__: tuple
    _provider: _Any
    def __init__(self, tooltipType, linkage, provider):
        ...
    def build(self, formatType, advanced_, *args, **kwargs):
        ...
    def _buildData(self, advanced_, *args, **kwargs):
        ...

class TooltipWindowBuilder(DataBuilder):
    def build(self, formatType, advanced_, *args, **kwargs):
        ...

class AdvancedTooltipWindowBuilder(AdvancedBuilder):
    __slots__: tuple
    _adProvider: _Any
    _condition: _Any
    _provider: _Any
    def __init__(self, tooltipType, linkage, provider, adProvider, condition=None):
        ...
    def build(self, formatType, advanced_, *args, **kwargs):
        ...
    def supportAdvanced(self, tooltipType, *args):
        ...

class AdvancedDataBuilder(AdvancedBuilder):
    __slots__: tuple
    _provider: _Any
    _adProvider: _Any
    _condition: _Any
    def __init__(self, tooltipType, linkage, provider, adProvider, condition=None):
        ...
    def build(self, formatType, advanced_, *args, **kwargs):
        ...
    def supportAdvanced(self, tooltipType, *args):
        ...
    def _buildData(self, advanced_, *args, **kwargs):
        ...

class ConditionBuilder(DataBuilder):
    __slots__: tuple
    _defaultLinkage: _Any
    def __init__(self, tooltipType, linkage, defaultLinkage, provider):
        ...
    def build(self, formatType, advanced_, *args, **kwargs):
        ...
    def _format(self, data, formatType):
        ...
    def _check(self, data):
        ...

class DefaultFormatBuilder(ConditionBuilder):
    __slots__: tuple
    def __init__(self, tooltipType, defaultLinkage, provider):
        ...
    def _check(self, data):
        ...

class ComplexBuilder(AdvancedBuilder):
    __slots__: tuple
    advancedComplexTooltips: _Any
    def __init__(self, tooltipType, linkage, advancedComplexTooltips):
        ...
    def supportAdvanced(self, tooltipType, *args):
        ...
    def build(self, formatType, advanced_, *args, **kwargs):
        ...

class AdvancedComplexBuilder(AdvancedBuilder):
    _provider: _Any
    def __init__(self, tooltipType, linkage, provider):
        ...
    def supportAdvanced(self, _, *args):
        ...
    def build(self, formatType, advanced_, *args, **kwargs):
        ...

class BuildersCollection(object):
    __slots__: tuple
    _builders: _Any
    def __init__(self, *builders):
        ...
    def clear(self):
        ...
    @property
    def linkages(self):
        ...
    @property
    def total(self):
        ...
    def addBuilder(self, builder):
        ...
    def getBuilder(self, tooltipType):
        ...

class LazyBuildersCollection(BuildersCollection):
    _settings: _Any
    def __init__(self, settings, *builders):
        ...
    def clear(self):
        ...
    def getBuilder(self, tooltipType):
        ...
    def _load(self, tooltipType):
        ...
