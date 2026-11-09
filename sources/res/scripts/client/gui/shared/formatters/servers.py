# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/formatters/servers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/servers.py
from __future__ import absolute_import
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import icons
from gui.shared.formatters import text_styles
from predefined_hosts import HOST_AVAILABILITY, PING_STATUSES
_UNAVAILABLE_DATA_PLACEHOLDER = '--'

def formatPingStatus(csisStatus, isColorBlind, isSelected, pingStatus, pingValue, useBigSize=False):
    if pingStatus == PING_STATUSES.REQUESTED:
        return None
    else:
        if csisStatus != HOST_AVAILABILITY.NOT_AVAILABLE and pingStatus != PING_STATUSES.UNDEFINED:
            if pingStatus == PING_STATUSES.LOW:
                formattedPing = text_styles.goodPing(pingValue)
            else:
                formattedPing = text_styles.main(pingValue) if isSelected else text_styles.standartPing(pingValue)
        else:
            pingValue = _UNAVAILABLE_DATA_PLACEHOLDER
            pingStatus = PING_STATUSES.UNDEFINED
            formattedPing = text_styles.standartPing(pingValue)
        colorBlindName = ''
        if isColorBlind and pingStatus == PING_STATUSES.HIGH:
            colorBlindName = '_color_blind'
        pingStatusIcon = makePingStatusIcon(pingStatus, colorBlindName)
        if useBigSize:
            return text_styles.concatStylesToSingleLine(text_styles.main(' '), formattedPing, pingStatusIcon)
        return text_styles.concatStylesToSingleLine(formattedPing, '', pingStatusIcon)


def makePingStatusIcon(pingStatus, colorBlindName=''):
    icon = backport.image(R.images.gui.maps.icons.pingStatus.dyn(('stairs_indicator_{}{}').format(pingStatus, colorBlindName), R.invalid)())
    return icons.makeImageTag(icon, 14, 14, -3)
