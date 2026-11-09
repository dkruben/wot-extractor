# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/views/info_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from constants import PLAYER_RANK as PLAYER_RANK
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from frontline.gui.frontline_skill_packer import packBaseSkills as packBaseSkills
from frontline.gui.impl.gen.view_models.views.lobby.views.skill_category_base_model import SkillCategoryBaseModel as SkillCategoryBaseModel, SkillCategoryType as SkillCategoryType
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.gen import R as R
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from frontline.gui.impl.gen.view_models.views.lobby.views.info_view_model import InfoViewModel as InfoViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.rank_item_model import RankItemModel as RankItemModel

class InfoView(ViewImpl):
    __epicController: Any
    _autoscrollSection: Any
    def __init__(self, layoutID=..., showFullScreen=False, autoscrollSection='', **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self, _=None):
        ...
    def __onViewClose(self):
        ...

class InfoViewWindow(WindowImpl):
    def __init__(self, parent=None, autoscrollSection=''):
        ...
