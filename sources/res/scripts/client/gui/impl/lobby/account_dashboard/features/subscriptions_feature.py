# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/subscriptions_feature.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_dashboard/features/subscriptions_feature.py
from constants import PLAYER_SUBSCRIPTIONS_CONFIG
from gui.impl.gen.view_models.views.lobby.account_dashboard.subscriptions_entry_point_model import SubscriptionsEntryPointModel
from gui.impl.lobby.account_dashboard.features.base import FeatureItem
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.shared.event_dispatcher import showSubscriptionsPage
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from uilogging.wot_plus.loggers import WotPlusAccountDashboardWidgetLogger
from uilogging.wot_plus.logging_constants import AccountDashboardFeature

class SubscriptionsFeature(FeatureItem):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def initialize(self, *args, **kwargs):
        super(SubscriptionsFeature, self).initialize(*args, **kwargs)
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChanged
        self._viewModel.subscriptions.onClick += self.__onClick

    def finalize(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChanged
        self._viewModel.subscriptions.onClick -= self.__onClick
        super(SubscriptionsFeature, self).finalize()

    def _fillModel(self, model):
        self.__update(model=model)

    @replaceNoneKwargsModel
    def __update(self, model=None):
        submodel = model.subscriptions
        submodel.setIsEnabled(self.__lobbyContext.getServerSettings().isPlayerSubscriptionsEnabled())
        model.setIsPlayerSubscriptionsEntrypointHidden(self.__lobbyContext.getServerSettings().isPlayerSubscriptionsEntrypointHidden())

    def __onServerSettingsChanged(self, diff):
        if PLAYER_SUBSCRIPTIONS_CONFIG in diff:
            self.__update()

    @staticmethod
    def __onClick():
        WotPlusAccountDashboardWidgetLogger().logWidgetClickEvent(AccountDashboardFeature.SUBSCRIPTION_WIDGET)
        showSubscriptionsPage()
