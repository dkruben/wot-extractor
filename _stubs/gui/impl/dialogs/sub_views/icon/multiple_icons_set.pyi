# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/dialogs/sub_views/icon/multiple_icons_set.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from gui.impl.gen import R as R
from gui.impl.dialogs.sub_views.common import IconSetData as IconSetData
from gui.impl.gen.view_models.views.dialogs.sub_views.multiple_icons_set_view_model import MultipleIconsSetViewModel as MultipleIconsSetViewModel, IconPositionLogicEnum as IconPositionLogicEnum
from gui.impl.gen.view_models.views.dialogs.sub_views.icon_view_model import IconViewModel as IconViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.image_substitution_view_model import ImageSubstitutionViewModel as ImageSubstitutionViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from frameworks.wulf import ViewSettings as ViewSettings
from typing import List as List, Optional as Optional, Any as Any
from frameworks.wulf import Array as Array
TYPE_ICONS: _Any
TYPE_RESOURCES: _Any

class MultipleIconsSet(ViewImpl):
    __slots__: tuple
    def __init__(self, iconResIDList=None, backgroundResIDList=None, overlayResIDList=None, layoutID=None, iconPositionLogic=...):
        ...
    def _onLoading(self, iconResIDList, backgroundResIDList, overlayResIDList, iconPositionLogic, *args, **kwargs):
        ...

def _populateImageSubstitutionModel(substitution):
    ...
def _addIconResIdsToViewModelArray(source, target):
    ...
def _addLayersResIdsToViewModelArray(source, target):
    ...
