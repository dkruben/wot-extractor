# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/user_account_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/header/user_account_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.subscriptions_model import SubscriptionsModel
from gui.impl.gen.view_models.views.lobby.page.header.user_info_model import UserInfoModel

class UserAccountModel(ViewModel):
    __slots__ = ('onOpenAccountDashboard', )

    def __init__(self, properties=2, commands=1):
        super(UserAccountModel, self).__init__(properties=properties, commands=commands)

    @property
    def userInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserInfoType():
        return UserInfoModel

    @property
    def subscriptions(self):
        return self._getViewModel(1)

    @staticmethod
    def getSubscriptionsType():
        return SubscriptionsModel

    def _initialize(self):
        super(UserAccountModel, self)._initialize()
        self._addViewModelProperty('userInfo', UserInfoModel())
        self._addViewModelProperty('subscriptions', SubscriptionsModel())
        self.onOpenAccountDashboard = self._addCommand('onOpenAccountDashboard')
