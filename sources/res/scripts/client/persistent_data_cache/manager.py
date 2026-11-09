# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/persistent_data_cache/manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/persistent_data_cache/manager.py
from __future__ import absolute_import
import BigWorld, wg_async
from helpers import ExitCode
from persistent_data_cache_common.manager import ForceCreatingPDCManager

class ClientForceCreatingPDCManager(ForceCreatingPDCManager):
    __slots__ = ()

    @wg_async.wg_async
    def _start(self):
        super(ClientForceCreatingPDCManager, self)._start()
        saved = yield wg_async.wg_await(self.save())
        if not saved:
            self._logger.error("Couldn't create cache!")
        BigWorld.quitWithExitCode(ExitCode.SUCCESS if saved else ExitCode.FAILED)
