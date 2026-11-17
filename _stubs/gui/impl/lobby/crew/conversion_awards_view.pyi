# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/conversion_awards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import SoundGroups as SoundGroups
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.common.awards_view_model import AwardsViewModel as AwardsViewModel
from gui.impl.lobby.crew.base_crew_view import BaseCrewSubView as BaseCrewSubView
from gui.impl.lobby.crew.tooltips.conversion_tooltip import ConversionTooltip as ConversionTooltip
from gui.impl.lobby.crew.utils import packCompensationData as packCompensationData
from gui.impl.pub import WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from .crew_sounds import SOUNDS as SOUNDS

class ConversionAwardsView(BaseCrewSubView):
    itemsCache: Any
    __slots__: tuple
    __conversionResult: Any
    __tooltipData: Any
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onClose(self, *_):
        ...
    def __onDisconnected(self):
        ...

class ConversionAwardsWindow(WindowImpl):
    def __init__(self, **kwargs):
        ...
