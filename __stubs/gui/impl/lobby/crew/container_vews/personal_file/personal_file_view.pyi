# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/personal_file_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_file_view_model import PersonalFileViewModel as PersonalFileViewModel
from gui.impl.lobby.container_views.base.components import ContainerBase as ContainerBase
from gui.impl.lobby.crew.container_vews.common.tankman_info_component import TankmanInfoComponent as TankmanInfoComponent
from gui.impl.lobby.crew.container_vews.personal_file.components.post_progression_widget_component import PostProgressionWidgetComponent as PostProgressionWidgetComponent
from gui.impl.lobby.crew.container_vews.personal_file.components.skill_matrix_component import SkillMatrixComponent as SkillMatrixComponent
from gui.impl.lobby.crew.container_vews.personal_file.context import PersonalFileViewContext as PersonalFileViewContext
from gui.impl.lobby.crew.container_vews.personal_file.controller import PersonalFileInteractionController as PersonalFileInteractionController
from gui.impl.lobby.crew.personal_case import IPersonalTab as IPersonalTab
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from PlayerEvents import g_playerEvents as g_playerEvents
from typing import List as List, Type as Type
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase

class PersonalFileView(ContainerBase, IPersonalTab, ViewImpl):
    __slots__: tuple
    TITLE: Any
    itemsCache: Any
    __appLoader: Any
    __isAnimationShowing: Any
    __hasPendingRefresh: Any
    def __init__(self, layoutID=..., **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def onChangeTankman(self, tankmanID):
        ...
    def _getEvents(self):
        ...
    def onStopAnimations(self):
        ...
    def setAnimationInProgress(self, isEnabled):
        ...
    def hideContent(self):
        ...
    def showContent(self):
        ...
    def refresh(self):
        ...
    def _getComponents(self):
        ...
    def _getContext(self, *args, **kwargs):
        ...
    def _getInteractionControllerCls(self):
        ...
    def _fillViewModel(self, vm):
        ...
    def _finalize(self):
        ...
    def __clearAnimationData(self, skipped=False):
        ...
    def __onDisconnected(self):
        ...
