# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/formatters/personal_reserves.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/formatters/personal_reserves.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from helpers import html
from messenger import g_settings
from messenger.formatters.service_channel import GeneralFormatter

class IPersonalReservesFormatter(GeneralFormatter):

    def __init__(self):
        super(IPersonalReservesFormatter, self).__init__('PersonalReservesMessage')


class IPersonalReservesExpirableFormatter(GeneralFormatter):

    def __init__(self):
        super(IPersonalReservesExpirableFormatter, self).__init__('PersonalReservesExpirableMessage')


class ReleaseFormatter(IPersonalReservesFormatter):

    def getTitle(self, message, *args):
        return backport.text(R.strings.messenger.serviceChannelMessages.personalReservesRelease.title())

    def getText(self, message, *args):
        return g_settings.htmlTemplates.format('personalReservesRelease', ctx={'boosterCount': (html.escape(message.get('values', '')))})


class PersonalReservesSoonExpirationFormatter(IPersonalReservesExpirableFormatter):

    def getTitle(self, message, *args):
        return backport.text(R.strings.messenger.serviceChannelMessages.personalReservesSoonExpire.title())

    def getText(self, message, *args):
        return g_settings.htmlTemplates.format('personalReservesSoonExpire', ctx={'boosterCount': (html.escape(message.get('values', '')))})
