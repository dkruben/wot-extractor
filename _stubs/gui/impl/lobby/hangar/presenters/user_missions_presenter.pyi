# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/user_missions_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.hangar.user_missions_plugin_model import UserMissionsPluginModel as UserMissionsPluginModel
from gui.impl.gen.view_models.views.lobby.hangar.user_missions_slide_model import UserMissionsSlideModel as UserMissionsSlideModel
from gui.impl.gen.view_models.views.lobby.hangar.user_missions_widget_model import UserMissionsWidgetModel as UserMissionsWidgetModel
from gui.impl.lobby.user_missions.hangar_widget.plugins import IUserMissionPlugin as IUserMissionPlugin
from gui.impl.lobby.user_missions.hangar_widget.presenters.battle_pass_presenter import BattlePassPresenter as BattlePassPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.event_banners_presenter import EventBannersPresenter as EventBannersPresenter
from gui.impl.lobby.user_missions.hangar_widget.presenters.quests_presenter import QuestsPresenter as QuestsPresenter
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsContainerService as IMissionsContainerService, IUserMissionWidgetService as IUserMissionWidgetService
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from helpers import dependency as dependency
from typing import Optional as Optional
from frameworks.wulf import Array as Array
INVALID_GROUP_INDEX = -1

# base nao representavel no stub: ViewComponent[...]
class UserMissionsPresenter:
    _missionsContainerService: Any
    _widgetService: Any
    _WIDGET_ALIAS = R.aliases.user_missions.hangarWidget
    _CHILDREN: dict
    _WIDGET_SLIDER_ID = 'missionsSlider'
    _DEFAULT_SLIDE_ID = 'missions'
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def slides(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onGroupVisibilityChanged(self, groupName, isVisible):
        ...
    def _updateSlides(self, vm):
        ...
    def _updateSelectedSlide(self, vm):
        ...
    def _addChildren(self):
        ...
    def _updatePlugins(self):
        ...
    def _addPlugin(self, plugin):
        ...
    def _onShowPlugin(self, plugin):
        ...
    def _onHidePlugin(self, pluginAlias):
        ...
    def _onSlideChanged(self, selectedSlide):
        ...
    def _addChild(self, posId):
        ...
    def _removeChild(self, posId):
        ...
    def _getChildComponents(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def __removeGroup(self, groups, groupName):
        ...
