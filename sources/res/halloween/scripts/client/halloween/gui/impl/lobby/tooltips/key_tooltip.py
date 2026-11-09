# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/key_tooltip.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/tooltips/key_tooltip.py
from __future__ import absolute_import
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from halloween.gui.impl.gen.view_models.views.lobby.tooltips.key_tooltip_view_model import KeyTooltipViewModel
from halloween.skeletons.halloween_artefacts_controller import IHalloweenArtefactsController
from halloween.skeletons.halloween_controller import IHalloweenController
from helpers import dependency

class KeyTooltipView(ViewImpl):
    __slots__ = ('__isPostBattle', '__ctx')
    _hwArtifactsCtrl = dependency.descriptor(IHalloweenArtefactsController)
    _hwController = dependency.descriptor(IHalloweenController)

    def __init__(self, isPostBattle, ctx=None, layoutID=R.views.halloween.mono.lobby.tooltips.key_tooltip()):
        settings = ViewSettings(layoutID)
        settings.model = KeyTooltipViewModel()
        super(KeyTooltipView, self).__init__(settings)
        self.__isPostBattle = isPostBattle
        self.__ctx = ctx

    @property
    def viewModel(self):
        return super(KeyTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(KeyTooltipView, self)._onLoading()
        with self.viewModel.transaction() as model:
            model.setIsPostBatle(self.__isPostBattle)
            model.setKeyCount(self._hwArtifactsCtrl.getArtefactKeyQuantity())
            model.setEndDate(self._hwController.getConfig().get('endDate', 0))
            if self.__isPostBattle:
                model.setEffective(self.__ctx.get('effective', 0))
                model.setBoss(self.__ctx.get('boss', 0))
                model.setDaily(self.__ctx.get('daily', 0))
                model.setSecret(self.__ctx.get('secret', 0))
