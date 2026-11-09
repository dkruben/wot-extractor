# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/account_completion/tooltips/hangar_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/tooltips/hangar_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.lobby.account_completion.utils.common import fillRewards
from gui.impl.pub import ViewImpl
from gui.impl.gen.view_models.views.lobby.account_completion.tooltips.hangar_tooltip_model import HangarTooltipModel

class HangarTooltipView(ViewImpl):

    def __init__(self, email):
        settings = ViewSettings(R.views.lobby.account_completion.tooltips.HangarTooltip())
        settings.model = HangarTooltipModel()
        super(HangarTooltipView, self).__init__(settings)
        self.__email = email

    def _onLoading(self, *args, **kwargs):
        with self.getViewModel().transaction() as model:
            self._fillModel(model)

    def _fillModel(self, model):
        if self.__email:
            model.setEmail(self.__email)
        fillRewards(model)
