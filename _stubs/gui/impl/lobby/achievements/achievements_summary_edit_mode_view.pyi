# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/achievements_summary_edit_mode_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from adisp import adisp_process as adisp_process
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.game_control.wot_plus.service_record_customization.service_record_customization import ServiceRecordProcessor as ServiceRecordProcessor, CdnResourcesCacheManager as CdnResourcesCacheManager
from gui.impl.dialogs.dialogs import showServiceRecordCustomizationConfirmDialog as showServiceRecordCustomizationConfirmDialog
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements_main_view_model import AchievementsViews as AchievementsViews
from gui.impl.lobby.achievements.achievements_main_view import AchievementsViewCtx as AchievementsViewCtx, BaseAchievementView as BaseAchievementView
from gui.impl.lobby.achievements.summary.summary_view import SummaryView as SummaryView
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.summary_view_model import SummaryViewModel as SummaryViewModel

class SummaryEditModeView(SummaryView):
    def initialize(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _onSetIsInCustomizationMode(self, _):
        ...
    def __onCustomizationConfirmed(self, ctx):
        ...
    def __onCustomizationDiscard(self, _):
        ...
    def __onSetBackgroundDraft(self, ctx):
        ...
    def __setInitialData(self):
        ...
    def __onSetRibbonDraft(self, ctx):
        ...
    def __setRibbonDraftById(self, id_):
        ...
    def __setBackgroundDraftById(self, id_):
        ...

class _AchievemetSummaryEditModeView(BaseAchievementView):
    __slots__: tuple
    __wotPlusCtrl: Any
    __summaryViewPresenter: Any
    def __init__(self, userID, *args, **kwargs):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    @property
    def currentPresenter(self):
        ...
    # decorador original: @wg_async
    def _onClose(self):
        ...
    def __onRenewableSubscriptionStatusChanged(self):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def __destroyIfNotActual(self):
        ...

class AchievementSummaryViewEditModeWindow(LobbyWindow):
    def __init__(self, userID, parent):
        ...

# decorador original: @adisp_process
def _storeNewCustomization(backgroundID, ribbonID):
    ...
