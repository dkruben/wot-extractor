# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/prestige/prestige_level_grades_tooltip_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/prestige/prestige_level_grades_tooltip_view.py
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel
from gui.impl.gen.view_models.views.lobby.prestige.tooltips.elite_level_grades_tooltip_model import EliteLevelGradesTooltipModel
from gui.prestige.prestige_helpers import getVehiclePrestige, fillPrestigeEmblemModel, getSortedGrades
from gui.impl.pub import ViewImpl

class PrestigeLevelGradesTooltipView(ViewImpl):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(layoutID=R.views.lobby.prestige.tooltips.EliteLevelGradesTooltip(), model=EliteLevelGradesTooltipModel(), args=args, kwargs=kwargs)
        super(PrestigeLevelGradesTooltipView, self).__init__(settings, *args, **kwargs)

    @property
    def viewModel(self):
        return super(PrestigeLevelGradesTooltipView, self).getViewModel()

    def _onLoading(self, vehIntCD, *args, **kwargs):
        currentLevel, _ = getVehiclePrestige(vehIntCD)
        with self.viewModel.transaction() as tx:
            tx.setCurrentLevel(currentLevel)
            emblems = tx.getEmblems()
            emblems.clear()
            for grade in getSortedGrades(vehIntCD, onlyMain=True):
                emblem = PrestigeEmblemModel()
                fillPrestigeEmblemModel(emblem, grade.level, vehIntCD)
                emblems.addViewModel(emblem)
