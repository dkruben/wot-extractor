# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/base/hangar_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/base/hangar_interfaces.py
from __future__ import absolute_import
import typing
from gui.shared.utils.requesters import RequestCriteria
if typing.TYPE_CHECKING:
    from Event import Event
    from gui.shared.gui_items import Vehicle

class IVehicleFilter(object):
    onDiff = None

    @property
    def criteria(self):
        raise NotImplementedError

    @property
    def vehicles(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError


class IAccountStyles(object):
    onChanged = None

    @property
    def criteria(self):
        raise NotImplementedError

    def initialize(self):
        raise NotImplementedError

    def destroy(self):
        raise NotImplementedError
