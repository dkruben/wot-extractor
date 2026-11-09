# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/tutorial/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/tutorial/__init__.py
from __future__ import absolute_import
from helpers.tutorial.stubs import StubTutorialLoader
from skeletons.tutorial import ITutorialLoader

def getTutorialConfig(manager):
    manager.addInstance(ITutorialLoader, StubTutorialLoader(), finalizer='fini')
