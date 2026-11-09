# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/dialogs/punishment_dialog_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/hangar/dialogs/punishment_dialog_model.py
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel

class PunishmentDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=2):
        super(PunishmentDialogModel, self).__init__(properties=properties, commands=commands)

    def getTitle(self):
        return self._getString(6)

    def setTitle(self, value):
        self._setString(6, value)

    def getText(self):
        return self._getString(7)

    def setText(self, value):
        self._setString(7, value)

    def getInfoText(self):
        return self._getString(8)

    def setInfoText(self, value):
        self._setString(8, value)

    def _initialize(self):
        super(PunishmentDialogModel, self)._initialize()
        self._addStringProperty('title', '')
        self._addStringProperty('text', '')
        self._addStringProperty('infoText', '')
