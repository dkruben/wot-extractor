# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/crew/container_vews/service_record/context.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/crew/container_vews/service_record/context.py
from gui.impl.lobby.crew.container_vews.common.base_personal_case_context import BasePersonalCaseContext

class ServiceRecordViewContext(BasePersonalCaseContext):
    __slots__ = ('_dossier', )

    def __init__(self, tankmanID):
        self._dossier = None
        super(ServiceRecordViewContext, self).__init__(tankmanID)
        return

    @property
    def dossier(self):
        return self._dossier

    def update(self, tankmanID=None):
        if tankmanID:
            super(ServiceRecordViewContext, self).update(tankmanID)
            self._dossier = self.itemsCache.items.getTankmanDossier(tankmanID)
