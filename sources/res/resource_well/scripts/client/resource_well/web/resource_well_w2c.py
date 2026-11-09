# wot-extractor: codigo DESCOMPILADO de sources/res/resource_well/scripts/client/resource_well/web/resource_well_w2c.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: resource_well/scripts/client/resource_well/web/resource_well_w2c.py
from __future__ import absolute_import
import logging
from helpers import dependency
from resource_well.gui.shared.event_dispatcher import showMainWindow
from skeletons.gui.resource_well import IResourceWellController
from web.web_client_api.ui import OpenTabWebApi
_logger = logging.getLogger(__name__)

def registerResourceWellOpenTabWebApi():

    @dependency.replace_none_kwargs(resourceWell=IResourceWellController)
    def _showResourceWell(_, cmd, resourceWell=None):
        if resourceWell.isActive():
            showMainWindow()
        else:
            _logger.error('Resource Well is not active at the moment!')

    OpenTabWebApi.addTabIdCallback('resource_well', _showResourceWell)
    return
