# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dossiers2/custom/tankman_layout.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/custom/tankman_layout.py
from __future__ import absolute_import
from dossiers2.common.DossierBlockBuilders import *
_tmanTotalBlockLayout = [
 'battlesCount']
_tmanTotalBlockBuilder = StaticSizeBlockBuilder('total', _tmanTotalBlockLayout, {}, [])
TMAN_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'warrior', 
 'invader', 
 'sniper', 
 'defender', 
 'steelwall', 
 'supporter', 
 'scout', 
 'evileye', 
 'medalWittmann', 
 'medalOrlik', 
 'medalOskin', 
 'medalHalonen', 
 'medalBurda', 
 'medalBillotte', 
 'medalKolobanov', 
 'medalFadin', 
 'medalRadleyWalters', 
 'medalBrunoPietro', 
 'medalTarczay', 
 'medalPascucci', 
 'medalDumitru', 
 'medalLehvaslaiho', 
 'medalNikolas', 
 'medalLafayettePool', 
 'heroesOfRassenay', 
 'medalDeLanglade', 
 'medalTamadaYoshio', 
 'huntsman', 
 'sniper2', 
 'mainGun']
_tankmanAchievementsBlockBuilder = StaticSizeBlockBuilder('achievements', TMAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, [])
tmanDossierLayout = (
 _tmanTotalBlockBuilder,
 _tankmanAchievementsBlockBuilder)
