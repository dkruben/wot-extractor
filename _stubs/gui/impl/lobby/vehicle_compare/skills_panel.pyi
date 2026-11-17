# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/vehicle_compare/skills_panel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel as SkillSimpleModel
from gui.impl.gen.view_models.views.lobby.crew.common.tooltip_constants import TooltipConstants as TooltipConstants
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_skills_panel_view_model import CompareSkillsPanelViewModel as CompareSkillsPanelViewModel
from gui.impl.lobby.crew.crew_helpers.skill_helpers import getRoleBySkillName as getRoleBySkillName
from gui.impl.lobby.crew.crew_helpers.skill_model_setup import skillSimpleModelSetup as skillSimpleModelSetup, ModelProps as ModelProps
from gui.impl.lobby.crew.tooltips.veh_cmp_skills_tooltip import VehCmpSkillsTooltip as VehCmpSkillsTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showSkillSelectWindow as showSkillSelectWindow
from gui.shared.gui_items.Tankman import crewMemberRealSkillLevel as crewMemberRealSkillLevel
from helpers import dependency as dependency
from items.components.skills_constants import SKILL_INDICES_ORDERED as SKILL_INDICES_ORDERED
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_view import CrewSkillsManager as CrewSkillsManager, VehicleCompareConfiguratorMain as VehicleCompareConfiguratorMain
propsGetters: dict

class CompareSkillsPanelView(ViewImpl):
    __slots__: tuple
    __appLoader: Any
    __guiLoader: Any
    __toolTipMgr: Any
    __cmpConf: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def onCrewSkillUpdated(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillViewModel(self):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    @staticmethod
    def __onClick():
        ...
    def __onReset(self):
        ...

def compareIconGetter(skillName, **__):
    ...
def compareLevelGetter(vehicle, skillName, **__):
    ...
