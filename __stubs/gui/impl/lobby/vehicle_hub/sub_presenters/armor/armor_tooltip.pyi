# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/armor_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from builtins import round as round
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_layer_model import ArmorLayerModel as ArmorLayerModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_tooltip_model import ArmorTooltipModel as ArmorTooltipModel
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.penetration_utils import calculatePenetrationInfo as calculatePenetrationInfo
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.utils import getMaterialsAtCursor as getMaterialsAtCursor, stackMaterials as stackMaterials
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.window_impl import WindowImpl as WindowImpl
from items.components.component_constants import MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS as MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.penetration_utils import ShellParams as ShellParams
_DEFAULT_REDUCTION_FACTOR = 1

class ArmorTooltipView(ViewImpl):
    __slots__: tuple
    _vehicleEntity: Any
    def __init__(self, vehicleEntity):
        ...
    def update(self, currentMode, shellParams, collisions):
        ...

class ArmorTooltipWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, vehicleEntity, parent=None):
        ...
    def update(self, currentMode, shellParams, collisions):
        ...
