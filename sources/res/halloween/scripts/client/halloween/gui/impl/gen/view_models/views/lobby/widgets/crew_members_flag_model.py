# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/crew_members_flag_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/gen/view_models/views/lobby/widgets/crew_members_flag_model.py
from frameworks.wulf import ViewModel

class CrewMembersFlagModel(ViewModel):
    __slots__ = ('onClick', )

    def __init__(self, properties=1, commands=1):
        super(CrewMembersFlagModel, self).__init__(properties=properties, commands=commands)

    def getIsHidden(self):
        return self._getBool(0)

    def setIsHidden(self, value):
        self._setBool(0, value)

    def _initialize(self):
        super(CrewMembersFlagModel, self)._initialize()
        self._addBoolProperty('isHidden', False)
        self.onClick = self._addCommand('onClick')
