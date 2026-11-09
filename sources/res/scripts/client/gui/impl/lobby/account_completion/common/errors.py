# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/account_completion/common/errors.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/account_completion/common/errors.py
from gui.impl.backport import text as loc
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.field_email_model import FieldEmailModel
_res = R.strings.dialogs.accountCompletion

def emailIsTooShort():
    return loc(_res.emailIsTooShort(), amount=FieldEmailModel.EMAIL_LEN_MIN)


def emailIsTooLong():
    return loc(_res.emailIsTooLong(), amount=FieldEmailModel.EMAIL_LEN_MAX)


def emailIsInvalid():
    return loc(_res.errorIsWrong())


def emailRestrictedByCountry():
    return loc(_res.emailRestrictedByCountry())


def emailAlreadyTaken():
    return loc(_res.emailAlreadyTaken())


def serverUnavailableTimed():
    return loc(_res.warningServerUnavailableTimed())


def keyErrorResID():
    return _res.activate.keyError()


def tooManyIncorrectTriesResID():
    return _res.activate.tooManyIncorrectTries()
