# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/fo_precache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/fo_precache.py
from __future__ import absolute_import
import BigWorld
from debug_utils import LOG_ERROR, LOG_DEBUG
_IS_ENABLED = True
if _IS_ENABLED:

    def add(path, forced=False):
        result = True
        try:
            result = BigWorld.wg_precacheScaleformResource(path, forced)
            if result:
                LOG_DEBUG('Resource is added to precache', path)
        except AttributeError:
            LOG_ERROR('BigWorld package does not include function wg_precacheScaleformResource')

        return result


    def clear(path=''):
        try:
            BigWorld.wg_eraseScaleformResFromCache(path)
            LOG_DEBUG('Resource(s) is(are) cleared from precache', path)
        except AttributeError:
            LOG_ERROR('BigWorld package does not include function wg_eraseScaleformResFromCache')


else:

    def add(path, forced=False):
        return True


    def clear(path=''):
        pass
