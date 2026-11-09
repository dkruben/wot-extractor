# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tournaments/team_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/tournaments/team_model.py
from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.tournaments.team_logos_model import TeamLogosModel

class TeamModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(TeamModel, self).__init__(properties=properties, commands=commands)

    @property
    def logos(self):
        return self._getViewModel(0)

    @staticmethod
    def getLogosType():
        return TeamLogosModel

    def getTeamName(self):
        return self._getString(1)

    def setTeamName(self, value):
        self._setString(1, value)

    def getScore(self):
        return self._getNumber(2)

    def setScore(self, value):
        self._setNumber(2, value)

    def getPrize(self):
        return self._getNumber(3)

    def setPrize(self, value):
        self._setNumber(3, value)

    def getSharedPositionFrom(self):
        return self._getNumber(4)

    def setSharedPositionFrom(self, value):
        self._setNumber(4, value)

    def getSharedPositionTo(self):
        return self._getNumber(5)

    def setSharedPositionTo(self, value):
        self._setNumber(5, value)

    def _initialize(self):
        super(TeamModel, self)._initialize()
        self._addViewModelProperty('logos', TeamLogosModel())
        self._addStringProperty('teamName', '')
        self._addNumberProperty('score', 0)
        self._addNumberProperty('prize', 0)
        self._addNumberProperty('sharedPositionFrom', 0)
        self._addNumberProperty('sharedPositionTo', 0)
