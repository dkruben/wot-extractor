# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/progression_styles/stage_switcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.Scaleform.daapi.view.meta.StageSwitcherMeta import StageSwitcherMeta as StageSwitcherMeta
from gui.customization.constants import CustomizationModes as CustomizationModes
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.customization.progression_styles.stage_switcher_model import StageSwitcherModel as StageSwitcherModel, SwitcherType as SwitcherType
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class StageSwitcher(StageSwitcherMeta):
    __view: Any
    def _makeInjectView(self):
        ...

class StageSwitcherView(ViewImpl):
    __customizationService: Any
    __itemsCache: Any
    __ctx: Any
    def __init__(self, flags=...):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onItemsRemoved(self, *_, **__):
        ...
    def __onItemInstalled(self, item, *_):
        ...
    def __onChangesCanceled(self):
        ...
    def __updateModel(self):
        ...
    def __onChange(self, *args):
        ...
    def __onModeChanged(self, modeId, _):
        ...
