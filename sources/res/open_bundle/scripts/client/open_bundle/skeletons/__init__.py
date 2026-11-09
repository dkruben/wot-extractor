# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/skeletons/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/skeletons/__init__.py
from __future__ import absolute_import
from gui.shared.system_factory import registerGameControllers
from open_bundle.gui.game_control.open_bundle_controller import OpenBundleController
from open_bundle.skeletons.open_bundle_controller import IOpenBundleController

def registerOpenBundleController():
    registerGameControllers([
     (
      IOpenBundleController, OpenBundleController, False)])
