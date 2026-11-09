# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/role_presenter_helper.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/role_presenter_helper.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R

def getRoleUserName(role):
    return backport.text(R.strings.item_types.tankman.roles.dyn(role)())


def getRoleWithFeminineUserName(role, isFemale):
    loc = R.strings.item_types.tankman.roles.female if isFemale else R.strings.item_types.tankman.roles
    return str(backport.text(loc.dyn(role)()))


def getRolePossessiveCaseUserName(role, isFemale):
    loc = R.strings.item_types.tankman.roles.female.possessiveCase if isFemale else R.strings.item_types.tankman.roles.possessiveCase
    return str(backport.text(loc.dyn(role)()))
