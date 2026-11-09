# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/halloween/gui/impl/lobby/page/hw_lobby_header.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/halloween/gui/impl/lobby/page/hw_lobby_header.py
from __future__ import absolute_import
from gui.impl.gen import R
from gui.impl.lobby.common.presenters.vehicles_info_presenter import VehiclesInfoPresenter
from gui.impl.lobby.page.fight_start import FightStartPresenter
from gui.impl.lobby.page.header_state_presenter import HeaderStatePresenter
from gui.impl.lobby.page.lobby_header import LobbyHeader
from gui.impl.lobby.page.navigation_presenter import NavigationPresenter
from gui.impl.lobby.page.prebattle_presenter import PrebattlePresenter
from gui.impl.lobby.page.prem_shop_presenter import PremShopPresenter
from gui.impl.lobby.page.user_account_presenter import UserAccountPresenter
from gui.impl.lobby.page.wallet_presenter import WalletPresenter, GoldProvider, CreditsProvider
from halloween.gui.impl.lobby.page.keys_presenter import KeysPresenter

class HWLobbyHeader(LobbyHeader):

    def __init__(self):
        super(HWLobbyHeader, self).__init__(R.views.halloween.mono.lobby.header())

    def _getChildComponents(self):
        header = R.aliases.lobby_header.default
        halloween = R.aliases.halloween.lobby_header
        return {(header.FightStart()): FightStartPresenter, 
           (header.NavigationBar()): NavigationPresenter, 
           (header.Prebattle()): PrebattlePresenter, 
           (halloween.Keys()): KeysPresenter, 
           (header.Wallet()): (lambda : WalletPresenter((
                             GoldProvider(),
                             CreditsProvider()))), 
           (header.UserAccount()): UserAccountPresenter, 
           (header.HeaderState()): HeaderStatePresenter, 
           (header.PremShop()): PremShopPresenter, 
           (header.CurrentVehicle()): (lambda : VehiclesInfoPresenter(self._currentVehicleFilter))}
