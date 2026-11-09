# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/collector_vehicle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/collector_vehicle.py
from __future__ import absolute_import

class CollectorVehicleConsts(object):
    CONFIG_NAME = 'collector_vehicle_config'
    COLLECTOR_VEHICLES_TAG = 'collectorVehicle'
    COLLECTOR_MEDAL_PREFIX = 'collectorVehicle'
    IS_ENABLED = 'enabled'


class CollectorVehicleConfig(object):
    __slots__ = ('__config', )

    def __init__(self, config):
        self.__config = config

    @property
    def isEnabled(self):
        return self.__config.get(CollectorVehicleConsts.IS_ENABLED, False)
