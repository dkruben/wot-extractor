# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/pm4_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from account_helpers.settings_core.settings_constants import PersonalMission4 as PersonalMission4
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.personal_missions_30.personal_mission_constants import OperationIDs as OperationIDs
from gui.impl.lobby.personal_missions_30.views_helpers import isPM4BannerAnimationShown as isPM4BannerAnimationShown, isIntroShown as isIntroShown, markPM4BannerAnimationShown as markPM4BannerAnimationShown
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.tooltips.pm4_banner_tooltip import PM4BannerTooltipView as PM4BannerTooltipView
from gui.shared.event_dispatcher import showPersonalMissionMainWindow as showPersonalMissionMainWindow
from personal_missions import PM_BRANCH as PM_BRANCH

class PM4EventBunner(StandardEventBanner):
    NAME = 'PM4EntryPoint'
    @property
    def playAppearAnim(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def borderColor(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onAppearAnimationPlayed(self):
        ...
    def onClick(self):
        ...
