# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_user_status_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/random/random_user_status_model.py
from gui.impl.gen.view_models.common.account_model import AccountModel
from gui.impl.gen.view_models.views.lobby.battle_results.user_status_model import UserStatusModel

class RandomUserStatusModel(UserStatusModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(RandomUserStatusModel, self).__init__(properties=properties, commands=commands)

    @property
    def killer(self):
        return self._getViewModel(3)

    @staticmethod
    def getKillerType():
        return AccountModel

    def _initialize(self):
        super(RandomUserStatusModel, self)._initialize()
        self._addViewModelProperty('killer', AccountModel())
