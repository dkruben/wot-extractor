# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/attachments_set_info_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/attachments_set_info_model.py
from frameworks.wulf import ViewModel

class AttachmentsSetInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(AttachmentsSetInfoModel, self).__init__(properties=properties, commands=commands)

    def getAttachmentsSetName(self):
        return self._getString(0)

    def setAttachmentsSetName(self, value):
        self._setString(0, value)

    def _initialize(self):
        super(AttachmentsSetInfoModel, self)._initialize()
        self._addStringProperty('attachmentsSetName', '')
