# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/service_record/service_record_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.impl import backport as backport
from gui.impl.backport.backport_tooltip import createBackportTooltipContent as createBackportTooltipContent
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.crew.personal_case.achievement_model import AchievementModel as AchievementModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.service_record_view_model import ServiceRecordViewModel as ServiceRecordViewModel
from gui.impl.lobby.container_views.base.components import ContainerBase as ContainerBase
from gui.impl.lobby.crew.container_vews.common.tankman_info_component import TankmanInfoComponent as TankmanInfoComponent
from gui.impl.lobby.crew.container_vews.service_record.context import ServiceRecordViewContext as ServiceRecordViewContext
from gui.impl.lobby.crew.container_vews.service_record.controller import ServiceRecordInteractionController as ServiceRecordInteractionController
from gui.impl.lobby.crew.personal_case import IPersonalTab as IPersonalTab
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items.dossier import dumpDossier as dumpDossier
from gui.shared.gui_items.dossier.achievements.abstract import isRareAchievement as isRareAchievement
from typing import List as List, Type as Type
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase

class ServiceRecordView(ContainerBase, IPersonalTab, ViewImpl):
    TITLE: Any
    def __init__(self, layoutID=..., **kwargs):
        ...
    def _getComponents(self):
        ...
    def _getContext(self, *args, **kwargs):
        ...
    def _getInteractionControllerCls(self):
        ...
    @property
    def viewModel(self):
        ...
    def onChangeTankman(self, tankmanID):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def onStopAnimations(self):
        ...
    def _fillViewModel(self, vm):
        ...
