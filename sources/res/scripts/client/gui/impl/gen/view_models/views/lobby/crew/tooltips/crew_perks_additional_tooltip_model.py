# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/crew_perks_additional_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/crew/tooltips/crew_perks_additional_tooltip_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_extended_model import SkillExtendedModel
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_progression_model import SkillProgressionModel

class CrewPerksAdditionalTooltipModel(SkillExtendedModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(CrewPerksAdditionalTooltipModel, self).__init__(properties=properties, commands=commands)

    @property
    def skillProgression(self):
        return self._getViewModel(9)

    @staticmethod
    def getSkillProgressionType():
        return SkillProgressionModel

    def getInfo(self):
        return self._getString(10)

    def setInfo(self, value):
        self._setString(10, value)

    def getSkillType(self):
        return self._getString(11)

    def setSkillType(self, value):
        self._setString(11, value)

    def getAnimationName(self):
        return self._getString(12)

    def setAnimationName(self, value):
        self._setString(12, value)

    def getIsDisabled(self):
        return self._getBool(13)

    def setIsDisabled(self, value):
        self._setBool(13, value)

    def getShowSkillProgression(self):
        return self._getBool(14)

    def setShowSkillProgression(self, value):
        self._setBool(14, value)

    def getPopularityList(self):
        return self._getArray(15)

    def setPopularityList(self, value):
        self._setArray(15, value)

    @staticmethod
    def getPopularityListType():
        return int

    def _initialize(self):
        super(CrewPerksAdditionalTooltipModel, self)._initialize()
        self._addViewModelProperty('skillProgression', SkillProgressionModel())
        self._addStringProperty('info', '')
        self._addStringProperty('skillType', '')
        self._addStringProperty('animationName', '')
        self._addBoolProperty('isDisabled', False)
        self._addBoolProperty('showSkillProgression', False)
        self._addArrayProperty('popularityList', Array())
