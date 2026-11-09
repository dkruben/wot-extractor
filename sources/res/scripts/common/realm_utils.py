# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/realm_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/realm_utils.py
from __future__ import absolute_import
import ResMgr as rmgr
from constants import CURRENT_REALM, IS_CLIENT, IS_EDITOR, REALMS
from py2to3.patched_future import with_metaclass

def getRealmFilePath(filepath):
    parts = filepath.split('.')
    return ('.').join(parts[:-1] + [CURRENT_REALM] + parts[-1:])


def isFileWithRealm(fileName):
    parts = fileName.split('.')
    return len(parts) > 2 and parts[-2] in REALMS


def isFileWithCurrentRealm(fileName):
    parts = fileName.split('.')
    return len(parts) > 2 and parts[-2] == CURRENT_REALM


class _ResMgrMeta(type):

    def __getattr__(cls, item):
        if IS_CLIENT:
            return getattr(rmgr, item)
        return getattr(cls if item in ('openSection', 'purge') else rmgr, item)


class ResMgr(with_metaclass(_ResMgrMeta, object)):

    @staticmethod
    def openSection(filepath, createIfMissing=False):
        section = (IS_EDITOR or rmgr.openSection)(getRealmFilePath(filepath)) if 1 else None
        if section is not None:
            return section
        else:
            return rmgr.openSection(filepath, createIfMissing)

    @staticmethod
    def purge(filepath, recursive=False):
        if not filepath:
            return
        rmgr.purge(filepath, recursive)
        rmgr.purge(getRealmFilePath(filepath), recursive)
