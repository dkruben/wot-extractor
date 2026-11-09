# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/notifications/manual_claim_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/notifications/manual_claim_model.py
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class ManualClaimModel(NotificationBaseModel):
    __slots__ = ('onClick', 'onClose')

    def __init__(self, properties=1, commands=2):
        super(ManualClaimModel, self).__init__(properties=properties, commands=commands)

    def _initialize(self):
        super(ManualClaimModel, self)._initialize()
        self.onClick = self._addCommand('onClick')
        self.onClose = self._addCommand('onClose')
