# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/animated_dog_tag_component.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/dog_tags/animated_dog_tag_component.py
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dt_dog_tag import DtDogTag

class AnimatedDogTagComponent(DtDogTag):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(AnimatedDogTagComponent, self).__init__(properties=properties, commands=commands)

    @property
    def requiredAchievement(self):
        return self._getViewModel(4)

    @staticmethod
    def getRequiredAchievementType():
        return AdvancedAchievementModel

    def getAnimation(self):
        return self._getString(5)

    def setAnimation(self, value):
        self._setString(5, value)

    def getIsSelected(self):
        return self._getBool(6)

    def setIsSelected(self, value):
        self._setBool(6, value)

    def getIsShowInPrebattle(self):
        return self._getBool(7)

    def setIsShowInPrebattle(self, value):
        self._setBool(7, value)

    def _initialize(self):
        super(AnimatedDogTagComponent, self)._initialize()
        self._addViewModelProperty('requiredAchievement', AdvancedAchievementModel())
        self._addStringProperty('animation', '')
        self._addBoolProperty('isSelected', False)
        self._addBoolProperty('isShowInPrebattle', False)
