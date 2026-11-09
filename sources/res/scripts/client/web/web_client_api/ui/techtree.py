# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/techtree.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/techtree.py
from __future__ import absolute_import
from helpers import dependency
from gui.shared import event_dispatcher
from skeletons.gui.shared import IItemsCache
from web.web_client_api import W2CSchema, w2c, Field

class _OpenTechTreeSchema(W2CSchema):
    vehicle_id = Field(required=True, type=int)


class TechTreeTabWebApiMixin(object):
    itemsCache = dependency.descriptor(IItemsCache)

    @w2c(_OpenTechTreeSchema, 'tech_tree')
    def openTechTree(self, cmd):
        event_dispatcher.showTechTree(cmd.vehicle_id)

    @w2c(_OpenTechTreeSchema, 'research')
    def openResearch(self, cmd):
        event_dispatcher.showResearchView(cmd.vehicle_id)

    @w2c(_OpenTechTreeSchema, 'vehicleHubOverview')
    def openVehicleHubOverview(self, cmd):
        event_dispatcher.showVehicleHubOverview(cmd.vehicle_id)
