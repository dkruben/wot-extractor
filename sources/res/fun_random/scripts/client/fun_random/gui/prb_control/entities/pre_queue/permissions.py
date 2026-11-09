# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/permissions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/prb_control/entities/pre_queue/permissions.py
from __future__ import absolute_import
from fun_random.gui.feature.util.fun_mixins import FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions

class FunRandomPermissions(PreQueuePermissions, FunSubModesWatcher):

    @hasDesiredSubMode(defReturn=False)
    def canCreateSquad(self):
        canCreateSquad = super(FunRandomPermissions, self).canCreateSquad()
        return canCreateSquad and self.getDesiredSubMode().isSquadAvailable()
