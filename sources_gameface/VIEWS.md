# Views Gameface

Gerado pelo wot-extractor. **O JavaScript/CSS formatado em `js/` e `css/` não é o código-fonte original**
(o webpack encurtou nomes e removeu comentários; só foram acrescentados espaços e quebras de linha).
O id `R.views` de cada view vem do mapeamento oficial `gui/gen_resources/*_layouts.json` (assinalado com *
quando não existe e foi deduzido pela pasta). As ligações ao Python (classes que usam a view e o seu
ViewModel) são **prováveis**: deduzidas pelas referências `R.views` no Python descompilado e pelo ViewModel.

Views: 713 · ficheiros .unbound: 190 · TypeScript: 17 · assets indexados: 44

| R.views | Confiança | ViewModel | Nomes do VM no JS | Python |
|---|---|---|---|---|
| `R.views.battle.battleRoyale.select_respawn.SelectRespawn` | provavel | - | - | `res/battle_royale/scripts/client/battle_royale/gui/Scaleform/daapi/view/battle/select_respawn.py` |
| `R.views.battle.battle_notifier.BattleNotifierView` | provavel-forte | BattleNotifierViewModel | 10/10 | `res/scripts/client/gui/impl/battle/battle_notifier/battle_notifier_view.py` |
| `R.views.battle.battle_page.EpicRespawnAmmunitionPanelView` | provavel-forte | RespawnAmmunitionPanelViewModel | 8/9 | `res/frontline/scripts/client/frontline/gui/impl/battle/battle_page/respawn_ammunition_panel_view.py` |
| `R.views.battle.battle_page.PersonalReservesTabView` | provavel-forte | PersonalReservesTabViewModel | 3/3 | `res/scripts/client/gui/impl/battle/battle_page/full_stats/personal_reserves_tab_view.py` |
| `R.views.battle.battle_page.PrebattleAmmunitionPanelView` | provavel-forte | PrebattleAmmunitionPanelViewModel | 9/10 | `res/scripts/client/gui/impl/battle/battle_page/ammunition_panel/prebattle_ammunition_panel_view.py` |
| `R.views.battle.battle_page.TabView` | provavel-forte | TabViewModel | 2/4 | `res/scripts/client/gui/Scaleform/daapi/view/battle/shared/tab_content.py` |
| `R.views.battle.death_cam.DeathCamHudView` | provavel-forte | DeathCamHudViewModel | 35/35 | `res/scripts/client/gui/impl/battle/death_cam/death_cam_hud_view.py` |
| `R.views.battle.death_cam.DeathCamUIView` | nao-encontrada | - | - | - |
| `R.views.battle.death_cam.MarkerView` | nao-encontrada | - | - | - |
| `R.views.battle.dog_tags.DogTagMarkerView` | provavel-forte | DogTagMarkerViewModel | 3/5 | `res/scripts/client/gui/impl/battle/dog_tags/dog_tag_marker_view.py` |
| `R.views.battle.postmortem_panel.PostmortemPanelView` | provavel | - | - | `res/scripts/client/gui/impl/battle/postmortem_panel/postmortem_panel_view.py` |
| `R.views.battle.prebattle.PrebattleHintsView` | provavel-forte | PrebattleHintsViewModel | 3/3 | `res/scripts/client/gui/impl/battle/prebattle/prebattle_hints_view.py` |
| `R.views.battle.timer.TimerView` | nao-encontrada | - | - | - |
| `R.views.battle_modifiers.lobby.tooltips.ModifiersDomainTooltipView` | provavel-forte | ModifiersDomainTooltipViewModel | 2/2 | `res/battle_modifiers/scripts/client/battle_modifiers/gui/impl/lobby/tooltips/modifiers_domain_tooltip_view.py` (+4) |
| `R.views.battle_royale.battle.views.LeaveBattleView` | provavel | - | - | `res/battle_royale/scripts/client/battle_royale/gui/impl/battle/views/leave_battle_view.py` |
| `R.views.battle_royale.lobby.BattleRoyaleBattleCard` | provavel | - | - | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/mode_selector/items/battle_royale_mode_selector_item.py` |
| `R.views.battle_royale.lobby.views.PreBattleView` | provavel-forte | PreBattleViewModel | 4/7 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/pre_battle.py` |
| `R.views.battle_royale.mono.lobby.battle_quest_awards_view` | provavel-forte | BattleQuestAwardsModel | 4/6 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_quest_awards_view.py` |
| `R.views.battle_royale.mono.lobby.battle_results` | provavel-forte | BattleResultViewModel | 4/6 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_result_view/battle_result_view.py` |
| `R.views.battle_royale.mono.lobby.hangar` | provavel | RouterModel | 1/4 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_royale_hangar_view.py` |
| `R.views.battle_royale.mono.lobby.info_page` | provavel-forte | InfoPageModel | 7/11 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/info_page.py` |
| `R.views.battle_royale.mono.lobby.progression_main_view` | provavel | ProgressionMainViewModel | 0/2 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/progression_main_view.py` |
| `R.views.battle_royale.mono.lobby.tooltips.ability` | nao-encontrada | - | - | - |
| `R.views.battle_royale.mono.lobby.tooltips.all_quests_done_tooltip` | provavel | QuestsListModel | 0/3 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/quests_presenter.py` |
| `R.views.battle_royale.mono.lobby.tooltips.banner` | provavel-forte | BannerTooltipViewModel | 2/4 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/banner_tooltip_view.py` |
| `R.views.battle_royale.mono.lobby.tooltips.battle_selector` | nao-encontrada | - | - | - |
| `R.views.battle_royale.mono.lobby.tooltips.ceasefire` | nao-encontrada | - | - | - |
| `R.views.battle_royale.mono.lobby.tooltips.commander` | nao-encontrada | - | - | - |
| `R.views.battle_royale.mono.lobby.tooltips.leaderboard_reward_tooltip_view` | provavel-forte | LeaderboardRewardTooltipModel | 2/2 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/leaderboard_reward_tooltip_view.py` (+1) |
| `R.views.battle_royale.mono.lobby.tooltips.progression_quest` | provavel | WidgetQuestModel | 3/15 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/progression_quest_tooltip.py` |
| `R.views.battle_royale.mono.lobby.tooltips.progression_widget` | provavel | ProgressionModel | 1/15 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/progression_widget_tooltip.py` (+1) |
| `R.views.battle_royale.mono.lobby.tooltips.proxy_currency_tooltip` | provavel | ProxyCurrencyTooltipViewModel | 0/1 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/proxy_currency_tooltip_view.py` (+3) |
| `R.views.battle_royale.mono.lobby.tooltips.respawn` | nao-encontrada | - | - | - |
| `R.views.battle_royale.mono.lobby.tooltips.reward_currency_tooltip` | provavel-forte | RewardCurrencyTooltipViewModel | 2/4 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/reward_currency_tooltip_view.py` (+1) |
| `R.views.battle_royale.mono.lobby.tooltips.shop_button` | provavel-forte | ShopButtonTooltipViewModel | 1/1 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/shop_button_tooltip_view.py` (+1) |
| `R.views.battle_royale.mono.lobby.tooltips.upgrades_button` | nao-encontrada | - | - | - |
| `R.views.battle_royale.mono.lobby.tooltips.vehicle` | provavel-forte | VehicleTooltipViewModel | 4/8 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/tooltips/vehicle_tooltip_view.py` (+1) |
| `R.views.common.BackportContextMenu` | provavel | BarracksViewModel | 0/20 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_result_view/battle_result_view.py` (+14) |
| `R.views.common.Browser` | provavel | - | - | `res/scripts/client/gui/impl/common/browser.py` |
| `R.views.common.FadingCoverView` | provavel-forte | FadingCoverViewModel | 6/6 | `res/scripts/client/gui/impl/common/fade_manager.py` |
| `R.views.common.HintButton` | nao-encontrada | - | - | - |
| `R.views.common.context_menu_window.context_menu_content.ContextMenuContent` | provavel | - | - | `res/scripts/client/gui/impl/pub/context_menu_window.py` |
| `R.views.common.context_menu_window.context_menu_window.ContextMenuWindow` | nao-encontrada | - | - | - |
| `R.views.common.dialog_view.components.balance_contents.CommonBalanceContent` | provavel | - | - | `res/scripts/client/gui/impl/lobby/dialogs/contents/common_balance_content.py` |
| `R.views.common.dialog_view.components.checkbox_content.CheckBoxDialogContent` | provavel | - | - | `res/scripts/client/gui/impl/lobby/dialogs/contents/checkbox_content.py` |
| `R.views.common.dialog_view.components.dialog_prices_content.DialogPricesContent` | provavel-forte | DialogPricesContentModel | 4/4 | `res/scripts/client/gui/impl/lobby/dialogs/contents/prices_content.py` |
| `R.views.common.dialog_view.components.dialog_prices_tooltip.DialogPricesTooltip` | provavel-forte | DialogPricesTooltipModel | 8/8 | `res/scripts/client/gui/impl/lobby/dialogs/dialog_prices_tooltip.py` |
| `R.views.common.dialog_view.dialog_window.DialogWindow` | provavel-forte | DialogWindowModel | 15/16 | `res/scripts/client/gui/impl/pub/dialog_window.py` |
| `R.views.common.dialog_view.simple_dialog_content.SimpleDialogContent` | provavel-forte | SimpleDialogWindowModel | 5/5 | `res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py` (+2) |
| `R.views.common.drop_down_menu_window.drop_down_menu_content.DropDownMenuContent` | nao-encontrada | - | - | - |
| `R.views.common.drop_down_menu_window.drop_down_menu_window.DropDownMenuWindow` | nao-encontrada | - | - | - |
| `R.views.common.personal_reserves.ReservesDisabledTooltip` | provavel | ReservesActivationViewModel | 0/10 | `res/scripts/client/gui/impl/battle/battle_page/full_stats/personal_reserves_tab_view.py` (+2) |
| `R.views.common.pop_over_window.backport_pop_over.BackportPopOverWindow` | nao-encontrada | - | - | - |
| `R.views.common.pop_over_window.pop_over_window.PopOverWindow` | nao-encontrada | - | - | - |
| `R.views.common.standard_window.standard_window.StandardWindow` | provavel | - | - | `res/scripts/client/gui/impl/pub/window_view.py` |
| `R.views.common.tooltip_window.advanced_tooltip_content.AdvandcedAnimatedTooltipContent` | provavel-forte | AdvancedAnimatedTooltipContentModel | 3/3 | `res/scripts/client/gui/impl/pub/tooltip_window.py` |
| `R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent` | provavel | CommonBattleQuestProgressModel | 0/8 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/battle_result_view/battle_result_view.py` (+28) |
| `R.views.common.tooltip_window.loot_box_compensation_tooltip.LootBoxVehicleCompensationTooltipContent` | provavel | MultipleAwardsViewModel | 0/12 | `res/scripts/client/gui/impl/auxiliary/rewards_helper.py` (+4) |
| `R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipHtmlContent` | provavel | PrebattleAmmunitionPanelViewModel | 0/10 | `res/scripts/client/gui/impl/battle/battle_page/ammunition_panel/prebattle_ammunition_panel_view.py` (+1) |
| `R.views.common.tooltip_window.tooltip_window.TooltipWindow` | provavel | - | - | `res/scripts/client/gui/impl/backport/backport_tooltip.py` |
| `R.views.comp7.lobby.Comp7BattleCard` | provavel | - | - | `res/comp7/scripts/client/comp7/gui/impl/lobby/mode_selector/items/comp7_mode_selector_item.py` |
| `R.views.comp7.lobby.MembersWindow` | provavel | - | - | `res/comp7/scripts/client/Comp7ExtensionPersonality.py` (+1) |
| `R.views.comp7.lobby.PlatoonDropdown` | provavel | - | - | `res/comp7/scripts/client/Comp7ExtensionPersonality.py` (+1) |
| `R.views.comp7.lobby.RewardsSelectionScreen` | provavel | - | - | `res/comp7/scripts/client/comp7/gui/impl/lobby/rewards_selection_screen.py` |
| `R.views.comp7.mono.battle.ban_progression` | provavel | BanProgressionModel | 0/5 | `res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_progression.py` |
| `R.views.comp7.mono.battle.ban_view` | provavel-forte | BanViewModel | 10/10 | `res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_view.py` (+1) |
| `R.views.comp7.mono.battle.ban_widget` | provavel | BanWidgetModel | 5/12 | `res/comp7/scripts/client/comp7/gui/impl/battle/vehicle_ban/ban_widget.py` |
| `R.views.comp7.mono.battle.tooltips.ban_show_tooltip` | provavel | BanViewModel | 0/10 | `res/comp7/scripts/client/comp7/gui/impl/battle/tooltips/ban_show_tooltip.py` (+1) |
| `R.views.comp7.mono.lobby.dialogs.purchase_dialog` | provavel | RootViewModel | 1/12 | `res/comp7/scripts/client/comp7/gui/impl/lobby/dialogs/purchase_dialog.py` (+1) |
| `R.views.comp7.mono.lobby.flag` | provavel | - | - | `res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/comp7_flag_view.py` |
| `R.views.comp7.mono.lobby.hangar` | provavel-forte | RouterModel | 3/4 | `res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/comp7_hangar.py` |
| `R.views.comp7.mono.lobby.intro_screen` | provavel | - | - | `res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/states.py` |
| `R.views.comp7.mono.lobby.meta_root_view` | provavel | - | - | `res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/states.py` (+1) |
| `R.views.comp7.mono.lobby.no_vehicles_screen` | provavel | - | - | `res/comp7/scripts/client/comp7/gui/impl/lobby/hangar/states.py` |
| `R.views.comp7.mono.lobby.post_battle_results_view` | provavel-forte | Comp7BattleResultsViewModel | 21/23 | `res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/comp7_battle_results_view.py` |
| `R.views.comp7.mono.lobby.rewards_screen` | provavel-forte | RewardsScreenModel | 13/22 | `res/comp7/scripts/client/comp7/gui/impl/lobby/rewards_screen.py` |
| `R.views.comp7.mono.lobby.season_statistics` | provavel | SeasonStatisticsModel | 0/1 | `res/comp7/scripts/client/comp7/gui/impl/lobby/season_statistics.py` |
| `R.views.comp7.mono.lobby.tooltips.battles_indicator_tooltip` | provavel | CustomizationTasksModel | 0/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.crew_members_tooltip` | provavel | Comp7BonusModel | 0/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_bonus_packer.py` (+2) |
| `R.views.comp7.mono.lobby.tooltips.damage_indicator_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.day_tooltip` | provavel | CustomizationTasksModel | 0/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.division_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+2) |
| `R.views.comp7.mono.lobby.tooltips.entry_point_tooltip` | provavel-forte | EntryPointTooltipModel | 2/3 | `res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/entry_point_tooltip.py` |
| `R.views.comp7.mono.lobby.tooltips.fifth_rank_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/leaderboard_page.py` (+6) |
| `R.views.comp7.mono.lobby.tooltips.general_rank_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+5) |
| `R.views.comp7.mono.lobby.tooltips.last_update_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/leaderboard_page.py` (+2) |
| `R.views.comp7.mono.lobby.tooltips.prestige_indicator_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.prestige_points_info_tooltip` | nao-encontrada | - | - | - |
| `R.views.comp7.mono.lobby.tooltips.progression_table_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.progression_tooltip` | provavel | EntryPointModel | 3/14 | `res/comp7/scripts/client/comp7/gui/impl/lobby/entry_point_presenter.py` (+3) |
| `R.views.comp7.mono.lobby.tooltips.rank_compatibility_tooltip` | provavel | RankCompatibilityTooltipModel | 0/3 | `res/comp7/scripts/client/comp7/gui/impl/lobby/platoon/view/platoon_members_view.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.rank_inactivity_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+3) |
| `R.views.comp7.mono.lobby.tooltips.rank_indicator_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.season_point_tooltip` | provavel | SeasonStatisticsModel | 0/1 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/yearly_rewards_page.py` (+2) |
| `R.views.comp7.mono.lobby.tooltips.sixth_rank_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/leaderboard_page.py` (+6) |
| `R.views.comp7.mono.lobby.tooltips.style3d_tooltip` | provavel | Style3dTooltipModel | 0/2 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/yearly_rewards_page.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.tournament_entry_point_tooltip` | provavel | TournamentEntryPointTooltipModel | 0/6 | `res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/entry_point_tooltip_tournament.py` |
| `R.views.comp7.mono.lobby.tooltips.weekly_quest_widget_tooltip` | provavel-forte | WeeklyQuestWidgetTooltipModel | 4/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/tooltips/weekly_quest_widget_tooltip.py` (+1) |
| `R.views.comp7.mono.lobby.tooltips.wins_indicator_tooltip` | provavel | CustomizationTasksModel | 1/7 | `res/comp7/scripts/client/comp7/gui/impl/lobby/meta_view/pages/progression_page.py` (+1) |
| `R.views.comp7.mono.lobby.tournaments.ols_view` | provavel | - | - | `res/comp7/scripts/client/Comp7ExtensionPersonality.py` (+2) |
| `R.views.comp7.mono.lobby.tournaments.wci_view` | provavel | - | - | `res/comp7/scripts/client/Comp7ExtensionPersonality.py` (+2) |
| `R.views.comp7.mono.lobby.whats_new_view` | provavel-forte | WhatsNewViewModel | 3/4 | `res/comp7/scripts/client/comp7/gui/impl/lobby/whats_new_view.py` |
| `R.views.comp7_core.mono.lobby.tooltips.modifiers_domain_tooltip` | provavel | - | - | `res/comp7_core/scripts/client/comp7_core/gui/impl/lobby/tooltips/comp7_core_modifiers_tooltip_view.py` |
| `R.views.comp7_light.lobby.Comp7LightBattleCard` | provavel | - | - | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/mode_selector/items/comp7_light_mode_selector_item.py` |
| `R.views.comp7_light.lobby.MembersWindow` | provavel | - | - | `res/comp7_light/scripts/client/Comp7LightPersonality.py` (+1) |
| `R.views.comp7_light.lobby.PlatoonDropdown` | provavel | - | - | `res/comp7_light/scripts/client/Comp7LightPersonality.py` (+1) |
| `R.views.comp7_light.mono.lobby.battle_quest_awards_view` | provavel-forte | BattleQuestAwardsModel | 3/5 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_quest_awards_view.py` |
| `R.views.comp7_light.mono.lobby.entry_point_tooltip` | provavel-forte | EntryPointTooltipModel | 2/3 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/tooltips/entry_point_tooltip.py` |
| `R.views.comp7_light.mono.lobby.flag` | provavel | - | - | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_flag_view.py` |
| `R.views.comp7_light.mono.lobby.hangar` | provavel-forte | RouterModel | 3/4 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/comp7_light_hangar.py` |
| `R.views.comp7_light.mono.lobby.intro_screen` | provavel | - | - | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/states.py` |
| `R.views.comp7_light.mono.lobby.leaderboard_reward_tooltip_view` | provavel | EntryPointModel | 0/9 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/entry_point_presenter.py` (+2) |
| `R.views.comp7_light.mono.lobby.no_vehicles_screen` | provavel | - | - | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/states.py` |
| `R.views.comp7_light.mono.lobby.post_battle_results_view` | provavel-forte | Comp7LightBattleResultsViewModel | 11/13 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/battle_results/comp7_light_battle_results_view.py` |
| `R.views.comp7_light.mono.lobby.progression_main_view` | provavel | ProgressionMainViewModel | 0/2 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/hangar/states.py` (+1) |
| `R.views.comp7_light.mono.lobby.tooltips.all_quests_done_tooltip` | provavel | ProgressionQuestsModel | 0/4 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/progression_quests_presenter.py` (+1) |
| `R.views.comp7_light.mono.lobby.tooltips.battle_quest_tooltip` | provavel | ProgressionQuestsModel | 0/4 | `res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/progression_quests_presenter.py` (+1) |
| `R.views.comp7_light.mono.lobby.tooltips.prestige_points_info_tooltip` | nao-encontrada | - | - | - |
| `R.views.dialogs.DefaultDialog` | provavel | CrewModel | 1/15 | `res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py` (+4) |
| `R.views.dialogs.common.DialogTemplateGenericTooltip` | provavel | SelectOptionViewModel | 0/4 | `res/scripts/client/gui/impl/dialogs/dialog_template.py` (+8) |
| `R.views.dialogs.sub_views.common.SimpleText` | provavel-forte | SimpleTextViewModel | 2/2 | `res/scripts/client/gui/impl/dialogs/sub_views/common/simple_text.py` |
| `R.views.dialogs.sub_views.common.SinglePrice` | provavel | SinglePriceViewModel | 1/3 | `res/scripts/client/gui/impl/dialogs/sub_views/common/single_price.py` |
| `R.views.dialogs.sub_views.content.SelectOptionContent` | provavel-forte | SelectOptionViewModel | 2/4 | `res/scripts/client/gui/impl/dialogs/sub_views/content/select_option_content.py` |
| `R.views.dialogs.sub_views.content.SimpleTextContent` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/sub_views/content/simple_text_content.py` |
| `R.views.dialogs.sub_views.content.SinglePriceContent` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/sub_views/content/single_price_content.py` |
| `R.views.dialogs.sub_views.content.TextWithWarning` | provavel-forte | TextWithWarningViewModel | 2/2 | `res/scripts/client/gui/impl/dialogs/sub_views/content/text_warning_content.py` |
| `R.views.dialogs.sub_views.footer.SimpleTextFooter` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/sub_views/footer/simple_text_footer.py` |
| `R.views.dialogs.sub_views.footer.SinglePriceFooter` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/sub_views/footer/single_price_footer.py` |
| `R.views.dialogs.sub_views.icon.MultipleIconsSet` | provavel-forte | MultipleIconsSetViewModel | 3/4 | `res/scripts/client/gui/impl/dialogs/sub_views/icon/multiple_icons_set.py` |
| `R.views.dialogs.sub_views.title.SimpleTextTitle` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/sub_views/title/simple_text_title.py` |
| `R.views.dialogs.sub_views.topRight.MoneyBalance` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/sub_views/top_right/money_balance.py` |
| `R.views.dialogs.widgets.IconSet` | provavel | - | - | `res/scripts/client/gui/impl/lobby/hangar/notifications/punishment_notification_view.py` |
| `R.views.dialogs.widgets.MoneyBalance` | provavel | BuyVehicleViewModel | 0/22 | `res/scripts/client/gui/impl/lobby/crew/dialogs/perks_reset_dialog.py` (+1) |
| `R.views.dialogs.widgets.SinglePrice` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/widgets/single_price.py` |
| `R.views.dialogs.widgets.WarningText` | provavel-forte | SimpleTextViewModel | 1/2 | `res/scripts/client/gui/impl/dialogs/widgets/warning_text.py` (+1) |
| `R.views.fort_rush.mono.battle.fort_rush_hud` | provavel-forte | FortRushHudViewModel | 15/21 | `res/fort_rush/scripts/client/fort_rush/gui/impl/battle/fort_rush_hud.py` (+1) |
| `R.views.fort_rush.mono.battle.fort_rush_vehicle_selector` | provavel-forte | FortRushVehicleSelectorViewModel | 12/12 | `res/fort_rush/scripts/client/fort_rush/gui/impl/battle/fort_rush_vehicle_selector.py` |
| `R.views.fort_rush.mono.lobby.battle_results` | provavel | - | - | `res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/battle_results_view.py` |
| `R.views.fort_rush.mono.lobby.hangar` | provavel-forte | RouterModel | 3/4 | `res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/hangar_view.py` (+1) |
| `R.views.fort_rush.mono.lobby.progression` | nao-encontrada | - | - | - |
| `R.views.fort_rush.mono.lobby.progression_view` | provavel | - | - | `res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/states.py` |
| `R.views.fort_rush.mono.lobby.reward_screen` | provavel-forte | FortRushRewardsScreenViewModel | 2/3 | `res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_reward_view.py` |
| `R.views.fort_rush.mono.lobby.rewards` | nao-encontrada | - | - | - |
| `R.views.fort_rush.mono.lobby.tier_list` | nao-encontrada | - | - | - |
| `R.views.fort_rush.mono.lobby.tooltips.banner_tooltip` | provavel | FortRushEventBannerViewModel | 0/8 | `res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/tooltips/fort_rush_event_banner_tooltip.py` |
| `R.views.fort_rush.mono.lobby.tooltips.battle_results_economic_tooltip` | nao-encontrada | - | - | - |
| `R.views.fort_rush.mono.lobby.tooltips.loot_box_tooltip` | nao-encontrada | - | - | - |
| `R.views.fort_rush.mono.lobby.tooltips.param_tooltip` | nao-encontrada | - | - | - |
| `R.views.fort_rush.mono.lobby.tooltips.progression_widget_tooltip` | provavel | FortRushProgressionTooltipViewModel | 1/7 | `res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/presenters/fort_rush_progression_entry_point_presenter.py` (+1) |
| `R.views.fort_rush.mono.lobby.welcome_screen_view` | provavel | - | - | `res/fort_rush/scripts/client/fort_rush/gui/impl/lobby/fort_rush_welcome_screen.py` |
| `R.views.frontline.lobby.RewardsSelectionView` | provavel | - | - | `res/frontline/scripts/client/frontline/gui/impl/lobby/views/rewards_selection_view.py` |
| `R.views.frontline.lobby.WelcomeView` | provavel | - | - | `res/frontline/scripts/client/frontline/gui/impl/lobby/views/welcome_view.py` |
| `R.views.frontline.mono.lobby.dialogs.battle_abilities_confirm_dialog` | provavel-forte | BattleAbilitiesConfirmDialogModel | 14/14 | `res/frontline/scripts/client/frontline/gui/impl/lobby/dialogs/battle_abilities_confirm_dialog.py` |
| `R.views.frontline.mono.lobby.hangar` | provavel-forte | RouterModel | 3/4 | `res/frontline/scripts/client/frontline/gui/impl/lobby/hangar_view.py` |
| `R.views.frontline.mono.lobby.info_view` | provavel | - | - | `res/frontline/scripts/client/frontline/gui/impl/lobby/views/info_view.py` |
| `R.views.frontline.mono.lobby.post_battle_results_view` | provavel | - | - | `res/frontline/scripts/client/frontline/gui/impl/lobby/views/frontline_battle_results_view.py` |
| `R.views.frontline.mono.lobby.post_battle_rewards_view` | provavel-forte | PostBattleRewardsViewModel | 15/15 | `res/frontline/scripts/client/frontline/gui/impl/lobby/post_battle_rewards_view.py` |
| `R.views.frontline.mono.lobby.progression_screen` | provavel-forte | ProgressionScreenModel | 11/11 | `res/frontline/scripts/client/frontline/gui/impl/lobby/progression_screen_view.py` (+1) |
| `R.views.frontline.mono.lobby.tooltips.banner_tooltip` | provavel-forte | BannerTooltipModel | 9/9 | `res/frontline/scripts/client/frontline/gui/impl/lobby/tooltips/banner_tooltip.py` |
| `R.views.frontline.mono.lobby.tooltips.battle_ability_alt_tooltip` | provavel-forte | BattleAbilityAltTooltipModel | 3/3 | `res/frontline/scripts/client/frontline/gui/impl/lobby/tooltips/battle_ability_alt_tooltip.py` |
| `R.views.frontline.mono.lobby.tooltips.battle_ability_tooltip` | provavel-forte | BattleAbilityTooltipModel | 6/6 | `res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/frontline_loadout_presenter.py` (+1) |
| `R.views.frontline.mono.lobby.tooltips.level_reserves_tooltip` | provavel | RouterModel | 0/4 | `res/frontline/scripts/client/frontline/gui/impl/lobby/hangar_view.py` (+1) |
| `R.views.frontline.mono.lobby.tooltips.skill_order_tooltip` | provavel | BattleAbilitiesSetupModel | 0/13 | `res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/frontline_ability_presenter.py` (+1) |
| `R.views.fun_random.lobby.feature.FunRandomModeSubSelector` | provavel | - | - | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/mode_selector/states.py` |
| `R.views.fun_random.mono.lobby.battle_results` | provavel | - | - | `res/fun_random/scripts/client/fun_random/gui/battle_results/__init__.py` |
| `R.views.fun_random.mono.lobby.hangar` | provavel-forte | RouterModel | 3/4 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/fun_random_hangar.py` |
| `R.views.fun_random.mono.lobby.progression` | provavel-forte | FunRandomProgressionViewModel | 10/11 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/fun_random_progression_view.py` |
| `R.views.fun_random.mono.lobby.rewards` | provavel-forte | FunRandomRewardsViewModel | 3/4 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/fun_random_rewards_view.py` |
| `R.views.fun_random.mono.lobby.tier_list` | provavel | - | - | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/states.py` |
| `R.views.fun_random.mono.lobby.tooltips.battle_results_economic_tooltip` | provavel-forte | FunRandomEconomicTooltipViewModel | 5/6 | `res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_personal_rewards.py` (+1) |
| `R.views.fun_random.mono.lobby.tooltips.entry_point_tooltip` | provavel | FunRandomEntryPointTooltipViewModel | 1/6 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/tooltips/fun_random_entry_point_tooltip_view.py` |
| `R.views.fun_random.mono.lobby.tooltips.loot_box_tooltip` | provavel | FunRandomProgressionViewModel | 0/11 | `res/fun_random/scripts/client/fun_random/gui/battle_results/sub_presenters/fun_progression.py` (+4) |
| `R.views.fun_random.mono.lobby.tooltips.no_quests_tooltip` | nao-encontrada | - | - | - |
| `R.views.fun_random.mono.lobby.tooltips.progression_quest_tooltip` | provavel | FunRandomProgressionQuestsModel | 2/6 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_progression_quests_presenter.py` (+1) |
| `R.views.fun_random.mono.lobby.tooltips.progression_tooltip` | provavel | FunRandomProgressionEntryPointModel | 1/3 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/hangar/presenters/fun_random_progression_presenter.py` (+3) |
| `R.views.halloween.lobby.MembersWindow` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/lobby/platoon_members_view.py` (+1) |
| `R.views.halloween.mono.battle.anomaly_recipes` | provavel-forte | AnomalyRecipesViewModel | 1/2 | `res/halloween/scripts/client/halloween/gui/impl/battle/anomaly_recipes_view.py` |
| `R.views.halloween.mono.battle.battle_loading` | provavel-forte | EventLoadingViewModel | 1/1 | `res/halloween/scripts/client/halloween/gui/impl/battle/halloween_battle_loading.py` (+1) |
| `R.views.halloween.mono.battle.help` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/battle/help_view.py` (+1) |
| `R.views.halloween.mono.battle.tab_screen` | provavel-forte | FullStatsViewModel | 2/4 | `res/halloween/scripts/client/halloween/gui/impl/battle/full_stats.py` (+3) |
| `R.views.halloween.mono.lobby.anomalies` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/lobby/anomalies_view.py` |
| `R.views.halloween.mono.lobby.attachments_reward_view` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/lobby/attachment_reward_view.py` |
| `R.views.halloween.mono.lobby.award_congrats_screen` | provavel-forte | AwardCongratsViewModel | 3/4 | `res/halloween/scripts/client/halloween/gui/impl/lobby/award_congrats_view.py` (+1) |
| `R.views.halloween.mono.lobby.battle_result` | provavel-forte | BattleResultViewModel | 5/7 | `res/halloween/scripts/client/halloween/gui/game_control/award_handlers.py` (+2) |
| `R.views.halloween.mono.lobby.bestiary` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/lobby/bestiary_view.py` |
| `R.views.halloween.mono.lobby.bundles_shop` | provavel-forte | BundleViewModel | 4/8 | `res/halloween/scripts/client/halloween/gui/impl/lobby/bundle_view.py` (+1) |
| `R.views.halloween.mono.lobby.comparison` | provavel-forte | ComparisonViewModel | 1/1 | `res/halloween/scripts/client/halloween/gui/impl/lobby/comparison_window_view.py` (+1) |
| `R.views.halloween.mono.lobby.crew_showcase` | provavel-forte | CrewShowcaseViewModel | 7/7 | `res/halloween/scripts/client/halloween/gui/impl/lobby/crew_showcase_view.py` |
| `R.views.halloween.mono.lobby.decrypt` | provavel-forte | DecryptViewModel | 14/15 | `res/halloween/scripts/client/halloween/gui/impl/lobby/decrypt_view.py` (+1) |
| `R.views.halloween.mono.lobby.dialogs.abilities_incomplete_confirm` | provavel-forte | AbilitiesInclompleteDialogModel | 3/3 | `res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py` (+2) |
| `R.views.halloween.mono.lobby.dialogs.story_choice_confirm` | provavel-forte | StoryChoiceDialogModel | 4/4 | `res/halloween/scripts/client/halloween/gui/impl/lobby/dialogs/story_choice_dialog.py` (+1) |
| `R.views.halloween.mono.lobby.difficulty_congrat` | provavel-forte | DifficultyWindowViewModel | 2/4 | `res/halloween/scripts/client/halloween/gui/impl/lobby/difficulty_window_view.py` (+1) |
| `R.views.halloween.mono.lobby.hangar` | provavel-forte | HangarViewModel | 16/28 | `res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py` (+6) |
| `R.views.halloween.mono.lobby.header` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/lobby/page/hw_lobby_header.py` |
| `R.views.halloween.mono.lobby.king_reward_congrat` | provavel-forte | KingRewardCongratsViewModel | 5/5 | `res/halloween/scripts/client/halloween/gui/impl/lobby/king_reward_congrats_view.py` (+1) |
| `R.views.halloween.mono.lobby.meta_intro` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/lobby/meta_intro_view.py` (+1) |
| `R.views.halloween.mono.lobby.notifications.crew_reward_notification` | provavel | - | - | `res/halloween/scripts/client/halloween_personality.py` |
| `R.views.halloween.mono.lobby.pre_battle_queue_view` | provavel | PreBattleQueueViewModel | 4/11 | `res/halloween/scripts/client/halloween/gui/impl/lobby/pre_battle_queue_view.py` (+1) |
| `R.views.halloween.mono.lobby.promo` | provavel | - | - | `res/halloween/scripts/client/halloween/gui/impl/lobby/promo_window_view.py` (+1) |
| `R.views.halloween.mono.lobby.reward_path` | provavel-forte | RewardPathViewModel | 9/10 | `res/halloween/scripts/client/halloween/gui/impl/lobby/reward_path_view.py` |
| `R.views.halloween.mono.lobby.reward_selection` | provavel-forte | RewardSelectionViewModel | 5/5 | `res/halloween/scripts/client/halloween/gui/impl/lobby/reward_selection_view.py` (+1) |
| `R.views.halloween.mono.lobby.story_choice` | provavel-forte | StoryChoiceViewModel | 2/2 | `res/halloween/scripts/client/halloween/gui/impl/lobby/story_choice.py` (+1) |
| `R.views.halloween.mono.lobby.tooltips.ability_tooltip` | provavel | ExtAmmoPanelView | 0/3 | `res/halloween/scripts/client/halloween/gui/impl/lobby/widgets/hw_loadout.py` |
| `R.views.halloween.mono.lobby.tooltips.anomalies_entry_point_tooltip` | provavel | ExtAmmoPanelView | 0/3 | `res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/anomalies_entry_point_tooltip.py` (+1) |
| `R.views.halloween.mono.lobby.tooltips.anomaly_tooltip` | provavel | AnomalyRecipesViewModel | 0/2 | `res/halloween/scripts/client/halloween/gui/impl/battle/anomaly_recipes_view.py` (+2) |
| `R.views.halloween.mono.lobby.tooltips.banner_tooltip` | provavel | EventBannerViewModel | 1/4 | `res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/event_banner_tooltip.py` |
| `R.views.halloween.mono.lobby.tooltips.daily_quests_tooltip` | provavel | DailyTooltipViewModel | 2/5 | `res/halloween/scripts/client/halloween/gui/impl/lobby/gsw_cards/quests_card_presenter.py` (+1) |
| `R.views.halloween.mono.lobby.tooltips.difficulty_tooltip` | provavel | DifficultyItemModel | 1/4 | `res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/difficulty_tooltip.py` (+1) |
| `R.views.halloween.mono.lobby.tooltips.empty_ability_slot_tooltip` | nao-encontrada | - | - | - |
| `R.views.halloween.mono.lobby.tooltips.key_tooltip` | provavel | BattleResultViewModel | 0/7 | `res/halloween/scripts/client/halloween/gui/impl/lobby/battle_result_view.py` (+5) |
| `R.views.halloween.mono.lobby.tooltips.mission_tooltip` | provavel | RewardPathViewModel | 1/10 | `res/halloween/scripts/client/halloween/gui/impl/lobby/reward_path_view.py` (+2) |
| `R.views.halloween.mono.lobby.tooltips.simple_format_tooltip` | provavel | HangarCarouselVehicleViewModel | 0/7 | `res/halloween/scripts/client/halloween/gui/impl/lobby/tooltips/simple_format_tooltip.py` (+1) |
| `R.views.halloween.mono.lobby.tooltips.vehicle_tooltip` | provavel | BundleViewModel | 0/8 | `res/halloween/scripts/client/halloween/gui/impl/lobby/bundle_view.py` (+5) |
| `R.views.last_stand.lobby.MembersWindow` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/platoon_members_view.py` (+1) |
| `R.views.last_stand.lobby.PlatoonDropdown` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/platoon/platoon_welcome_view.py` (+1) |
| `R.views.last_stand.lobby.SearchingDropdown` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/platoon/platoon_search_view.py` (+1) |
| `R.views.last_stand.mono.battle.battle_loading` | provavel-forte | EventLoadingViewModel | 1/1 | `res/last_stand/scripts/client/last_stand/gui/impl/battle/battle_loading_view.py` (+1) |
| `R.views.last_stand.mono.battle.help_view` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/battle/help_view.py` |
| `R.views.last_stand.mono.battle.tab_screen` | provavel | FullStatsViewModel | 0/3 | `res/last_stand/scripts/client/last_stand/gui/impl/battle/full_stats.py` |
| `R.views.last_stand.mono.lobby.attachments_reward_view` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/attachment_reward_view.py` |
| `R.views.last_stand.mono.lobby.battle_result_view` | provavel-forte | BattleResultViewModel | 6/11 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/battle_result_view.py` (+1) |
| `R.views.last_stand.mono.lobby.dialogs.abilities_incomplete_confirm` | provavel-forte | AbilitiesInclompleteDialogModel | 3/3 | `res/last_stand/scripts/client/last_stand/gui/game_control/ls_controller.py` (+2) |
| `R.views.last_stand.mono.lobby.difficulty_congratulation_view` | provavel-forte | DifficultyWindowViewModel | 2/4 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/difficulty_window_view.py` (+1) |
| `R.views.last_stand.mono.lobby.hangar` | provavel-forte | HangarViewModel | 6/12 | `res/last_stand/scripts/client/last_stand/gui/game_control/ls_controller.py` (+4) |
| `R.views.last_stand.mono.lobby.meta_intro` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/meta_intro_view.py` (+1) |
| `R.views.last_stand.mono.lobby.narration_view` | provavel-forte | NarrationViewModel | 4/7 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/narration_view.py` (+1) |
| `R.views.last_stand.mono.lobby.prebattle_queue_view` | provavel-forte | PreBattleQueueViewModel | 8/8 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/pre_battle_queue_view.py` (+1) |
| `R.views.last_stand.mono.lobby.promo_view` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/promo_window_view.py` (+1) |
| `R.views.last_stand.mono.lobby.reward_path_view` | provavel-forte | RewardPathViewModel | 9/9 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/reward_path_view.py` |
| `R.views.last_stand.mono.lobby.stage_reward_view` | provavel-forte | StageRewardViewModel | 5/5 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/stage_reward_view.py` |
| `R.views.last_stand.mono.lobby.tooltips.additional_data_tooltip` | provavel | RewardPathViewModel | 0/9 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/reward_path_view.py` (+1) |
| `R.views.last_stand.mono.lobby.tooltips.banner_tooltip` | provavel | EventBannerViewModel | 1/4 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/event_banner_tooltip.py` |
| `R.views.last_stand.mono.lobby.tooltips.battle_pass_tooltip` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/battle_pass_in_progress_tooltip.py` |
| `R.views.last_stand.mono.lobby.tooltips.booster_tooltip` | provavel | RewardPathViewModel | 0/9 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/ls_helpers/bonuses_formatters.py` (+3) |
| `R.views.last_stand.mono.lobby.tooltips.daily_quests_tooltip` | provavel-forte | DailyTooltipViewModel | 3/6 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/gsw_cards/quests_card_presenter.py` (+1) |
| `R.views.last_stand.mono.lobby.tooltips.difficulty_tooltip` | provavel | BattleResultViewModel | 1/11 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/battle_result_view.py` (+3) |
| `R.views.last_stand.mono.lobby.tooltips.points_tooltip` | provavel | BattleResultViewModel | 0/11 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/battle_result_view.py` (+4) |
| `R.views.last_stand.mono.lobby.tooltips.reward_path_tooltip` | provavel | RewardPathViewModel | 0/9 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/gsw_cards/reward_path_presenter.py` (+1) |
| `R.views.last_stand.mono.lobby.tooltips.simple_format_tooltip` | provavel | VehiclesDailyModel | 0/1 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/simple_format_tooltip.py` (+1) |
| `R.views.last_stand.mono.lobby.tooltips.vehicle_tooltip` | provavel | - | - | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/tooltips/ls_carousel_tooltip_view.py` |
| `R.views.loading.GameLoadingView` | provavel-forte | - | - | - |
| `R.views.lobby.account_completion.AddCredentialsView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/account_completion/common/base_credentials_overlay_view.py` |
| `R.views.lobby.account_completion.ConfirmCredentialsView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/account_completion/common/base_confirm_credentials_overlay_view.py` |
| `R.views.lobby.account_completion.CurtainView` | provavel-forte | CurtainViewModel | 6/6 | `res/scripts/client/gui/impl/lobby/account_completion/curtain/curtain_view.py` |
| `R.views.lobby.account_completion.SteamEmailConfirmRewardsView` | provavel-forte | SteamEmailConfirmRewardsViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/account_completion/steam_email_confirm_rewards_view.py` |
| `R.views.lobby.account_completion.tooltips.HangarTooltip` | provavel-forte | HangarTooltipModel | 2/2 | `res/scripts/client/gui/impl/lobby/account_completion/tooltips/hangar_tooltip_view.py` (+1) |
| `R.views.lobby.account_dashboard.AccountDashboard` | provavel-forte | AccountDashboardModel | 11/12 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+1) |
| `R.views.lobby.account_dashboard.DailyExperienceView` | provavel-forte | DailyExperienceViewModel | 12/13 | `res/scripts/client/gui/impl/lobby/daily_experience/states.py` |
| `R.views.lobby.achievements.AchievementsMainView` | provavel-forte | AchievementsMainViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/achievements/achievements_main_view.py` (+1) |
| `R.views.lobby.achievements.CatalogView` | provavel-forte | CatalogViewModel | 15/15 | `res/scripts/client/gui/impl/lobby/achievements/catalog_view.py` (+1) |
| `R.views.lobby.achievements.EarningPopUpView` | provavel-forte | AchievementsEarningViewModel | 4/4 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/earning_pop_up_view.py` |
| `R.views.lobby.achievements.EditView` | provavel-forte | EditViewModel | 14/14 | `res/scripts/client/gui/impl/lobby/achievements/edit_view.py` |
| `R.views.lobby.achievements.RewardView` | provavel-forte | RewardViewModel | 9/9 | `res/scripts/client/gui/impl/lobby/achievements/reward_view.py` (+1) |
| `R.views.lobby.achievements.dialogs.EditConfirm` | provavel-forte | EditConfirmModel | 4/4 | `res/scripts/client/gui/impl/lobby/achievements/dialogs/achievement_edit_confirm.py` |
| `R.views.lobby.achievements.tooltips.AutoSettingTooltip` | provavel-forte | AutoSettingTooltipModel | 1/1 | `res/scripts/client/gui/impl/lobby/achievements/edit_view.py` (+1) |
| `R.views.lobby.achievements.tooltips.BattlesKPITooltip` | provavel-forte | BattlesKpiTooltipViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/achievements/tooltips/battles_kpi_tooltip.py` |
| `R.views.lobby.achievements.tooltips.EditingTooltip` | provavel-forte | EditingTooltipViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/achievements/edit_view.py` (+2) |
| `R.views.lobby.achievements.tooltips.KPITooltip` | provavel-forte | KpiTooltipViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/achievements/summary/summary_view.py` (+1) |
| `R.views.lobby.achievements.tooltips.WOTPRMainTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/achievements/summary/summary_view.py` (+1) |
| `R.views.lobby.achievements.tooltips.WTRInfoTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/achievements/summary/summary_view.py` (+1) |
| `R.views.lobby.achievements.tooltips.WTRMainTooltip` | provavel-forte | WtrMainTooltipViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/achievements/summary/summary_view.py` (+1) |
| `R.views.lobby.awards.BadgeAwardView` | provavel-forte | BadgeAwardViewModel | 1/1 | `res/scripts/client/gui/impl/lobby/awards/badge_award_view.py` |
| `R.views.lobby.awards.MultipleAwardsView` | provavel-forte | MultipleAwardsViewModel | 12/12 | `res/scripts/client/gui/impl/lobby/awards/multiple_awards_view.py` |
| `R.views.lobby.awards.tooltips.RewardCompensationTooltip` | provavel | BonusModel | 0/2 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/common/lootboxes.py` (+6) |
| `R.views.lobby.awards.tooltips.VehicleForChooseTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/awards/tooltip/__init__.py` |
| `R.views.lobby.battle_matters.BattleMattersEntryPointView` | provavel-forte | BattleMattersEntryPointViewModel | 6/6 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_entry_point_view.py` |
| `R.views.lobby.battle_matters.BattleMattersExchangeRewards` | provavel-forte | BattleMattersExchangeRewardsModel | 4/4 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_exchange_rewards.py` |
| `R.views.lobby.battle_matters.BattleMattersMainRewardView` | provavel-forte | BattleMattersMainRewardViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_main_reward_view.py` |
| `R.views.lobby.battle_matters.BattleMattersMainView` | provavel-forte | BattleMattersMainViewModel | 10/10 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_main_view.py` |
| `R.views.lobby.battle_matters.BattleMattersPausedView` | provavel-forte | BattleMattersPausedViewModel | 1/1 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_paused_view.py` |
| `R.views.lobby.battle_matters.BattleMattersRewardsView` | provavel-forte | BattleMattersRewardsViewModel | 10/10 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_rewards_view.py` |
| `R.views.lobby.battle_matters.BattleMattersVehicleSelectionView` | provavel-forte | BattleMattersVehicleSelectionViewModel | 7/7 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_vehicle_selection_view.py` |
| `R.views.lobby.battle_matters.popovers.BattleMattersFilterPopoverView` | provavel | BattleMattersVehicleSelectionViewModel | 0/7 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_vehicle_selection_view.py` (+2) |
| `R.views.lobby.battle_matters.tooltips.BattleMattersEntryTooltipView` | provavel-forte | BattleMattersEntryPointViewModel | 3/6 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_entry_point_view.py` (+1) |
| `R.views.lobby.battle_matters.tooltips.BattleMattersTokenTooltipView` | provavel | BattleMattersMainViewModel | 0/10 | `res/scripts/client/gui/impl/lobby/battle_matters/battle_matters_main_view.py` (+2) |
| `R.views.lobby.battle_pass.trophy_device_confirm_dialog.TrophyDeviceConfirmDialogContent` | provavel-forte | TrophyDeviceConfirmDialogModel | 3/4 | `res/scripts/client/gui/impl/lobby/battle_pass/trophy_device_confirm_view.py` |
| `R.views.lobby.blueprints.Confirm` | provavel-forte | BlueprintConvertModel | 15/24 | `res/scripts/client/gui/impl/dialogs/dialogs.py` (+1) |
| `R.views.lobby.blueprints.blueprint_screen.blueprint_screen.BlueprintScreen` | provavel | - | - | `res/scripts/client/gui/game_control/AwardController.py` (+1) |
| `R.views.lobby.blueprints.fragments_balance_content.FragmentsBalanceContent` | provavel-forte | BlueprintBalanceContentModel | 3/3 | `res/scripts/client/gui/impl/lobby/blueprints/fragments_balance_content.py` |
| `R.views.lobby.blueprints.tooltips.BlueprintsAlliancesTooltipView` | provavel | BlueprintBalanceContentModel | 1/3 | `res/scripts/client/gui/impl/lobby/blueprints/blueprints_alliance_tooltip_view.py` (+2) |
| `R.views.lobby.clan_supply.ClanSupply` | provavel-forte | ClanSupplyModel | 5/7 | `res/scripts/client/gui/impl/lobby/clan_supply/states.py` |
| `R.views.lobby.clan_supply.RewardsView` | provavel-forte | RewardsViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/clan_supply/rewards_view.py` |
| `R.views.lobby.collection.AwardsView` | provavel | AwardsViewModel | 2/8 | `res/scripts/client/gui/impl/lobby/collection/awards_view.py` (+1) |
| `R.views.lobby.collection.CollectionItemPreview` | provavel-forte | CollectionItemPreviewModel | 12/12 | `res/scripts/client/gui/impl/lobby/collection/collection_item_preview.py` (+1) |
| `R.views.lobby.collection.CollectionView` | provavel-forte | CollectionViewModel | 20/23 | `res/scripts/client/gui/impl/lobby/collection/collection.py` |
| `R.views.lobby.collection.CollectionsMainView` | provavel-forte | CollectionsMainViewModel | 6/6 | `res/scripts/client/gui/impl/lobby/collection/collections_main_view.py` |
| `R.views.lobby.collection.IntroView` | provavel | CollectionsMainViewModel | 2/6 | `res/scripts/client/gui/impl/lobby/collection/collections_main_view.py` (+1) |
| `R.views.lobby.collection.tooltips.CollectionItemTooltipView` | provavel | RewardModel | 0/13 | `res/scripts/client/gui/impl/auxiliary/collections_helper.py` (+3) |
| `R.views.lobby.common.AwardsView` | provavel | AwardsViewModel | 1/8 | `res/frontline/scripts/client/frontline/gui/impl/lobby/views/awards_view.py` (+1) |
| `R.views.lobby.common.BrowserView` | provavel | - | - | `res/scripts/client/gui/game_control/PromoController.py` (+2) |
| `R.views.lobby.common.RewardSelection` | nao-encontrada | - | - | - |
| `R.views.lobby.common.SelectSlotSpecDialog` | provavel-forte | SelectSlotSpecDialogModel | 14/20 | `res/scripts/client/gui/impl/lobby/common/select_slot_spec_dialog.py` (+1) |
| `R.views.lobby.common.SelectableRewardBase` | provavel | SelectableRewardBaseModel | 0/1 | - |
| `R.views.lobby.common.congrats.common_congrats_view.CommonCongratsView` | provavel-forte | CommonCongratsViewModel | 11/11 | `res/scripts/client/gui/impl/lobby/common/congrats/common_congrats_view.py` |
| `R.views.lobby.common.tooltips.ExtendedTextTooltip` | provavel | ChallengesMissionsProgressModel | 0/2 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/progression_main_view.py` (+27) |
| `R.views.lobby.common.tooltips.SelectedRewardsTooltipView` | provavel-forte | SelectedRewardsTooltipViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/common/selectable_reward_base.py` (+1) |
| `R.views.lobby.common.tooltips.SimpleIconTooltip` | provavel-forte | SimpleIconTooltipModel | 4/4 | `res/fun_random/scripts/client/fun_random/gui/impl/lobby/mode_selector/fun_sub_selector_view.py` (+2) |
| `R.views.lobby.crew.BarracksView` | provavel-forte | BarracksViewModel | 20/20 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+4) |
| `R.views.lobby.crew.ConversionConfirmView` | provavel-forte | ConversionConfirmViewModel | 6/6 | `res/scripts/client/gui/impl/lobby/crew/conversion_confirm_view.py` |
| `R.views.lobby.crew.CrewHeaderTooltipView` | provavel | CrewWidgetModel | 0/15 | `res/scripts/client/gui/impl/lobby/crew/crew_header_tooltip_view.py` (+2) |
| `R.views.lobby.crew.CrewPostProgressionView` | provavel-forte | CrewPostProgressionViewModel | 8/8 | `res/scripts/client/gui/impl/lobby/crew/crew_post_progression_view.py` (+1) |
| `R.views.lobby.crew.HangarCrewWidget` | provavel-forte | HangarCrewWidgetModel | 1/1 | `res/scripts/client/gui/impl/lobby/crew/hangar_crew_widget.py` |
| `R.views.lobby.crew.HelpView` | provavel-forte | HelpViewModel | 3/3 | `res/scripts/client/gui/impl/lobby/crew/help_view.py` |
| `R.views.lobby.crew.JunkTankmenView` | provavel-forte | JunkTankmenViewModel | 6/6 | `res/scripts/client/gui/impl/lobby/crew/junk_tankmen_view.py` |
| `R.views.lobby.crew.MemberChangeView` | provavel-forte | MemberChangeViewModel | 23/24 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+1) |
| `R.views.lobby.crew.MentorAssigmentView` | provavel-forte | MentorAssigmentViewModel | 19/21 | `res/scripts/client/gui/impl/lobby/crew/mentor_assigment_view.py` |
| `R.views.lobby.crew.QuickTrainingView` | provavel-forte | QuickTrainingViewModel | 19/20 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+2) |
| `R.views.lobby.crew.SkillsTrainingView` | provavel-forte | SkillsTrainingViewModel | 16/16 | `res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/skills_training_view.py` (+1) |
| `R.views.lobby.crew.TankChangeView` | provavel-forte | TankChangeViewModel | 9/10 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+1) |
| `R.views.lobby.crew.TankmanContainerView` | provavel | SkillsTrainingViewModel | 6/16 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+3) |
| `R.views.lobby.crew.dialogs.CrewBooksPurchaseDialog` | provavel-forte | CrewBooksPurchaseDialogModel | 13/13 | `res/scripts/client/gui/impl/lobby/crew/dialogs/crew_books_purchase_dialog.py` |
| `R.views.lobby.crew.dialogs.DismissTankmanDialog` | provavel-forte | DismissTankmanDialogModel | 17/17 | `res/scripts/client/gui/impl/lobby/crew/dialogs/dismiss_tankman_dialog.py` |
| `R.views.lobby.crew.dialogs.DocumentChangeDialog` | provavel-forte | DocumentChangeDialogModel | 14/14 | `res/scripts/client/gui/impl/lobby/crew/dialogs/document_change_dialog.py` |
| `R.views.lobby.crew.dialogs.EnlargeBarracksDialog` | provavel-forte | EnlargeBarracksDialogModel | 13/13 | `res/scripts/client/gui/impl/lobby/crew/dialogs/enlarge_barracks_dialog.py` |
| `R.views.lobby.crew.dialogs.FillAllPerksDialog` | provavel-forte | FillAllPerksDialogModel | 12/12 | `res/scripts/client/gui/impl/lobby/crew/dialogs/fill_all_perks_dialog.py` |
| `R.views.lobby.crew.dialogs.MentorAssignmentDialog` | provavel-forte | MentorAssignmentDialogModel | 17/17 | `res/scripts/client/gui/impl/lobby/crew/dialogs/mentor_assignment_dialog.py` |
| `R.views.lobby.crew.dialogs.PerksResetDialog` | provavel-forte | PerksResetDialogModel | 13/13 | `res/scripts/client/gui/impl/lobby/crew/dialogs/perks_reset_dialog.py` |
| `R.views.lobby.crew.dialogs.RecruitConfirmIrrelevantDialog` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/confirm_irrelevant_perk_reset_dialog.py` |
| `R.views.lobby.crew.dialogs.RecruitDialog` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_window/recruit_dialog.py` |
| `R.views.lobby.crew.dialogs.RecruitNewTankmanDialog` | provavel-forte | RecruitNewTankmanDialogModel | 11/13 | `res/scripts/client/gui/impl/lobby/crew/dialogs/recruit_new_tankman_dialog.py` |
| `R.views.lobby.crew.dialogs.RestoreTankmanDialog` | provavel-forte | RestoreTankmanDialogModel | 9/9 | `res/scripts/client/gui/impl/lobby/crew/dialogs/restore_tankman_dialog.py` |
| `R.views.lobby.crew.dialogs.RetrainMassiveDialog` | provavel-forte | RetrainMassiveDialogModel | 12/12 | `res/scripts/client/gui/impl/lobby/crew/dialogs/retrain_massive_dialog.py` |
| `R.views.lobby.crew.dialogs.RetrainPremiumVehicleDialog` | provavel-forte | RetrainPremiumVehicleDialogModel | 10/10 | `res/scripts/client/gui/impl/lobby/crew/dialogs/retrain_premium_vehicle_dialog.py` |
| `R.views.lobby.crew.dialogs.RetrainSingleDialog` | provavel-forte | RetrainSingleDialogModel | 18/18 | `res/scripts/client/gui/impl/lobby/crew/dialogs/retrain_single_dialog.py` |
| `R.views.lobby.crew.dialogs.SkillsTrainingConfirmDialog` | provavel-forte | SkillsTrainingConfirmDialogModel | 9/9 | `res/scripts/client/gui/impl/lobby/crew/dialogs/skills_training_confirm_dialog.py` |
| `R.views.lobby.crew.dialogs.SkinApplyDialog` | provavel-forte | SkinApplyDialogModel | 9/9 | `res/scripts/client/gui/impl/lobby/crew/dialogs/skin_apply_dialog.py` |
| `R.views.lobby.crew.personal_case.PersonalDataView` | provavel | TankmanContainerViewModel | 1/12 | `res/scripts/client/gui/impl/lobby/crew/personal_case/personal_data_view.py` (+1) |
| `R.views.lobby.crew.personal_case.PersonalFileView` | provavel | QuickTrainingViewModel | 0/20 | `res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/__init__.py` (+4) |
| `R.views.lobby.crew.personal_case.ServiceRecordView` | provavel | TankmanContainerViewModel | 1/12 | `res/scripts/client/gui/impl/lobby/crew/container_vews/service_record/service_record_view.py` (+1) |
| `R.views.lobby.crew.popovers.FilterPopoverView` | provavel | FilterPanelWidgetModel | 4/18 | `res/scripts/client/gui/impl/lobby/crew/filter/filter_panel_widget.py` (+1) |
| `R.views.lobby.crew.tooltips.AdvancedTooltipView` | provavel-forte | AdvancedTooltipViewModel | 3/3 | `res/scripts/client/gui/impl/lobby/crew/tooltips/advanced_tooltip_view.py` |
| `R.views.lobby.crew.tooltips.BonusPerksTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/components/skill_matrix_component.py` (+1) |
| `R.views.lobby.crew.tooltips.BunksConfirmDiscountTooltip` | provavel | BarracksViewModel | 0/20 | `res/scripts/client/gui/impl/lobby/crew/barracks_view.py` (+2) |
| `R.views.lobby.crew.tooltips.ConversionTooltip` | provavel | AwardsViewModel | 0/8 | `res/scripts/client/gui/impl/lobby/crew/conversion_awards_view.py` (+3) |
| `R.views.lobby.crew.tooltips.CrewBookMouseTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/books_list_component.py` (+1) |
| `R.views.lobby.crew.tooltips.CrewPerksAdditionalTooltip` | provavel-forte | CrewPerksAdditionalTooltipModel | 9/9 | `res/scripts/client/gui/impl/lobby/crew/tooltips/commander_bonus_additional_tooltip.py` (+1) |
| `R.views.lobby.crew.tooltips.CrewPerksTooltip` | provavel-forte | CrewPerksTooltipModel | 11/11 | `res/scripts/client/gui/impl/lobby/crew/tooltips/commander_bonus_tooltip.py` (+1) |
| `R.views.lobby.crew.tooltips.DirectiveConversionTooltip` | provavel-forte | DirectiveConversionTooltipModel | 3/3 | `res/scripts/client/gui/impl/lobby/crew/tooltips/directive_conversion_tooltip.py` (+1) |
| `R.views.lobby.crew.tooltips.DismissedToggleTooltip` | provavel | FilterPopoverViewModel | 0/6 | `res/scripts/client/gui/impl/lobby/crew/base_tankman_list_view.py` (+3) |
| `R.views.lobby.crew.tooltips.EmptySkillTooltip` | provavel | CrewWidgetModel | 0/15 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/crew_tab_view.py` (+5) |
| `R.views.lobby.crew.tooltips.ExperienceStepperTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/freexp_book_component.py` (+1) |
| `R.views.lobby.crew.tooltips.MentorAssignmentTooltip` | provavel-forte | MentorAssignmentTooltipModel | 2/2 | `res/scripts/client/gui/impl/lobby/crew/tooltips/mentor_assignment_tooltip.py` |
| `R.views.lobby.crew.tooltips.MentoringLicenseTooltip` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/mentoring_license_component.py` (+4) |
| `R.views.lobby.crew.tooltips.PostProgressionTooltip` | provavel-forte | PostProgressionTooltipModel | 4/4 | `res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/components/post_progression_widget_component.py` (+1) |
| `R.views.lobby.crew.tooltips.PremiumVehicleTooltip` | provavel-forte | PremiumVehicleTooltipViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/crew/container_vews/common/tankman_info_component.py` (+1) |
| `R.views.lobby.crew.tooltips.QualificationTooltip` | provavel-forte | QualificationTooltipViewModel | 4/4 | `res/scripts/client/gui/impl/lobby/crew/container_vews/personal_file/components/skill_matrix_component.py` (+1) |
| `R.views.lobby.crew.tooltips.QuickTrainingDiscountTooltip` | provavel-forte | QuickTrainingDiscountTooltipModel | 4/4 | `res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/freexp_book_component.py` (+1) |
| `R.views.lobby.crew.tooltips.QuickTrainingLostXpTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/container_vews/quick_training/components/books_list_component.py` (+1) |
| `R.views.lobby.crew.tooltips.RetireUndertrainedTooltip` | provavel | BarracksViewModel | 1/20 | `res/scripts/client/gui/impl/lobby/crew/barracks_view.py` (+1) |
| `R.views.lobby.crew.tooltips.SkillUntrainedAdditionalTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/tooltips/skill_untrained_additional_tooltip.py` |
| `R.views.lobby.crew.tooltips.SkillUntrainedTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/crew/tooltips/skill_untrained_tooltip.py` |
| `R.views.lobby.crew.tooltips.SkillsEfficiencyTooltip` | provavel-forte | SkillsEfficiencyTooltipModel | 4/4 | `res/scripts/client/gui/impl/lobby/crew/tooltips/skills_efficiency_tooltip.py` |
| `R.views.lobby.crew.tooltips.SortingDropdownTooltip` | provavel | SkillsTrainingViewModel | 1/16 | `res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/skills_training_view.py` |
| `R.views.lobby.crew.tooltips.SpecializationWotPlusTooltip` | provavel-forte | SpecializationWotPlusTooltipModel | 1/1 | `res/scripts/client/gui/impl/lobby/crew/container_vews/common/tankman_info_component.py` (+1) |
| `R.views.lobby.crew.tooltips.TankmanTooltip` | provavel-forte | TankmanTooltipModel | 18/18 | `res/scripts/client/gui/impl/lobby/crew/tooltips/tankman_tooltip.py` |
| `R.views.lobby.crew.tooltips.VehCmpSkillsTooltip` | provavel-forte | VehCmpSkillsTooltipModel | 1/1 | `res/scripts/client/gui/impl/lobby/crew/tooltips/veh_cmp_skills_tooltip.py` (+1) |
| `R.views.lobby.crew.tooltips.VehicleParamsTooltipView` | provavel-forte | VehicleParamsTooltipViewModel | 10/10 | `res/scripts/client/gui/impl/lobby/crew/tooltips/vehicle_params_tooltip_view.py` |
| `R.views.lobby.crew.widgets.CrewBannerWidget` | provavel-forte | CrewBannerWidgetModel | 5/5 | `res/scripts/client/gui/impl/lobby/crew/widget/crew_banner_widget.py` |
| `R.views.lobby.crew.widgets.CrewWidget` | provavel-forte | CrewWidgetModel | 15/15 | `res/scripts/client/gui/impl/lobby/crew/widget/crew_widget.py` |
| `R.views.lobby.crew.widgets.FilterPanelWidget` | provavel-forte | FilterPanelWidgetModel | 18/18 | `res/scripts/client/gui/impl/lobby/crew/filter/filter_panel_widget.py` |
| `R.views.lobby.crew.widgets.PriceList` | provavel-forte | PriceListModel | 3/3 | `res/scripts/client/gui/impl/auxiliary/tankman_operations.py` (+3) |
| `R.views.lobby.crew.widgets.TankmanInfo` | nao-encontrada | - | - | - |
| `R.views.lobby.crystalsPromo.CrystalsPromoView` | provavel | - | - | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+1) |
| `R.views.lobby.currency_reserves.CurrencyReserves` | provavel | - | - | `res/scripts/client/gui/impl/lobby/currency_reserves/states.py` |
| `R.views.lobby.currency_reserves.ReservesAwardView` | provavel | ReservesAwardViewModel | 0/7 | `res/scripts/client/gui/impl/lobby/currency_reserves/reserves_award_view.py` |
| `R.views.lobby.customization.CustomizationCart` | provavel | ProgressiveItemsViewModel | 3/8 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/main_view.py` (+2) |
| `R.views.lobby.customization.CustomizationRarityRewardScreen` | provavel-forte | CustomizationRarityRewardScreenModel | 7/7 | `res/scripts/client/gui/impl/lobby/customization/customization_rarity_reward_screen/customization_rarity_reward_screen.py` |
| `R.views.lobby.customization.progression_styles.OnboardingView` | provavel-forte | OnboardingViewModel | 3/3 | `res/scripts/client/gui/impl/lobby/customization/progression_styles/onboarding_view.py` (+1) |
| `R.views.lobby.customization.progression_styles.StageSwitcher` | provavel-forte | StageSwitcherModel | 7/7 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/progression_styles/stage_switcher.py` |
| `R.views.lobby.customization.progressive_items_reward.ProgressiveItemsUpgradeView` | provavel-forte | ProgressiveItemsRewardViewModel | 16/17 | `res/scripts/client/gui/impl/lobby/customization/progressive_items_reward/progressive_items_upgrade_view.py` |
| `R.views.lobby.customization.progressive_items_view.ProgressiveItemsView` | provavel-forte | ProgressiveItemsViewModel | 7/8 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/customization/main_view.py` (+1) |
| `R.views.lobby.customization.style_unlocked_view.StyleUnlockedView` | provavel-forte | StyleUnlockedViewModel | 8/8 | `res/scripts/client/gui/impl/lobby/customization/style_unlocked_view/style_unlocked_view.py` |
| `R.views.lobby.customization.vehicles_sidebar.VehiclesSidebar` | provavel-forte | VehiclesSidebarModel | 2/2 | `res/scripts/client/gui/shared/event_dispatcher.py` |
| `R.views.lobby.dedication.DedicationRewardView` | provavel | DedicationRewardViewModel | 0/2 | `res/scripts/client/gui/impl/lobby/dedication/dedication_reward_view.py` |
| `R.views.lobby.dog_tags.AnimatedDogTagGradeTooltip` | provavel-forte | AnimatedDogTagGradeTooltipModel | 4/4 | `res/scripts/client/gui/impl/lobby/achievements/summary/summary_view.py` (+1) |
| `R.views.lobby.dog_tags.AnimatedDogTagsView` | provavel-forte | AnimatedDogTagsViewModel | 10/10 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/LobbyView.py` (+3) |
| `R.views.lobby.dog_tags.CatalogAnimatedDogTagTooltip` | provavel | AnimatedDogTagsViewModel | 0/10 | `res/scripts/client/gui/impl/lobby/achievements/profile_utils.py` (+2) |
| `R.views.lobby.dog_tags.CustomizationConfirmDialog` | provavel-forte | CustomizationConfirmDialogModel | 4/4 | `res/scripts/client/gui/impl/lobby/dog_tags/customization_confirm_dialog.py` (+1) |
| `R.views.lobby.dog_tags.DedicationTooltip` | provavel | DogTagsViewModel | 0/21 | `res/scripts/client/gui/impl/lobby/dog_tags/dog_tags_view.py` |
| `R.views.lobby.dog_tags.DogTagsView` | provavel-forte | DogTagsViewModel | 20/21 | `res/scripts/client/gui/impl/lobby/dog_tags/dog_tags_view.py` (+2) |
| `R.views.lobby.dog_tags.RankedEfficiencyTooltip` | provavel | DogTagsViewModel | 0/21 | `res/scripts/client/gui/impl/lobby/dog_tags/dog_tags_view.py` (+1) |
| `R.views.lobby.dog_tags.ThreeMonthsTooltip` | provavel | DogTagsViewModel | 0/21 | `res/scripts/client/gui/impl/lobby/dog_tags/dog_tags_view.py` |
| `R.views.lobby.dog_tags.TriumphTooltip` | provavel | DogTagsViewModel | 0/21 | `res/scripts/client/gui/impl/lobby/dog_tags/dog_tags_view.py` |
| `R.views.lobby.excluded_maps.ExcludedMapsTooltip` | provavel-forte | ExcludedMapsTooltipModel | 2/2 | `res/scripts/client/gui/impl/lobby/maps_blacklist/maps_blacklist_view.py` |
| `R.views.lobby.excluded_maps.ExcludedMapsView` | provavel-forte | ExcludedMapsViewModel | 9/11 | `res/scripts/client/gui/impl/lobby/maps_blacklist/states.py` |
| `R.views.lobby.hangar.BuyVehicleView` | provavel-forte | BuyVehicleViewModel | 21/22 | `res/scripts/client/gui/game_control/AwardController.py` (+1) |
| `R.views.lobby.hangar.VehicleParamsWidget` | nao-encontrada | - | - | - |
| `R.views.lobby.hangar.notifications.PunishmentView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/hangar/notifications/punishment_notification_view.py` |
| `R.views.lobby.hangar.subViews.VehicleParams` | provavel | MemberChangeViewModel | 0/24 | `res/scripts/client/gui/impl/lobby/crew/container_vews/skills_training/skills_training_view.py` (+4) |
| `R.views.lobby.instructions.BuyWindow` | provavel-forte | BoosterBuyModel | 24/31 | `res/scripts/client/gui/impl/lobby/instructions/booster_buy_dialog.py` |
| `R.views.lobby.instructions.SellWindow` | provavel-forte | BuySellItemsDialogModel | 18/27 | `res/scripts/client/gui/impl/lobby/instructions/booster_sell_dialog.py` |
| `R.views.lobby.live_ops_web_events.EntryPoint` | provavel-forte | EntryPointViewModel | 7/7 | `res/scripts/client/gui/impl/lobby/live_ops_web_events/entry_point_view.py` |
| `R.views.lobby.live_ops_web_events.EntryPointTooltip` | provavel-forte | EntryPointTooltipViewModel | 3/4 | `res/scripts/client/gui/impl/lobby/live_ops_web_events/entry_point_tooltip_view.py` (+1) |
| `R.views.lobby.mapbox.MapBoxAwardsView` | provavel-forte | MapBoxAwardsViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/mapbox/map_box_awards_view.py` |
| `R.views.lobby.mapbox.MapBoxIntro` | provavel-forte | MapBoxIntroModel | 3/3 | `res/scripts/client/gui/impl/lobby/mapbox/map_box_intro.py` (+1) |
| `R.views.lobby.mapbox.MapBoxProgression` | provavel-forte | MapboxProgressionModel | 20/20 | `res/scripts/client/gui/impl/lobby/mapbox/mapbox_progression_view.py` |
| `R.views.lobby.mapbox.MapBoxSurveyView` | provavel-forte | MapBoxSurveyViewModel | 12/12 | `res/scripts/client/gui/impl/lobby/mapbox/mapbox_survey_view.py` |
| `R.views.lobby.marathon.RewardWindow` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/impl/lobby/marathon/marathon_reward_window_view.py` |
| `R.views.lobby.marathon.marathon_reward_view.MarathonRewardView` | provavel-forte | MarathonRewardViewModel | 11/11 | `res/scripts/client/gui/impl/lobby/marathon/marathon_reward_helper.py` (+1) |
| `R.views.lobby.marathon.tooltips.RestRewardTooltip` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/impl/lobby/marathon/marathon_reward_tooltip_content.py` (+1) |
| `R.views.lobby.matchmaker.ActiveTestConfirmView` | provavel | ActiveTestConfirmViewModel | 6/18 | `res/scripts/client/gui/impl/lobby/matchmaker/active_test_confirm_view.py` (+1) |
| `R.views.lobby.missions.missions_tab_bar_view.MissionsTabBarView` | provavel | - | - | `res/scripts/client/gui/Scaleform/daapi/view/lobby/missions/regular/missions_tab_bar.py` |
| `R.views.lobby.mode_selector.BattleSessionView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/mode_selector/battle_session_view.py` |
| `R.views.lobby.mode_selector.ModeSelectorView` | provavel | FunRandomSubSelectorModel | 4/10 | `res/fun_random/scripts/client/fun_random/gui/feature/sub_systems/fun_notifications.py` (+5) |
| `R.views.lobby.mode_selector.tooltips.AlertTooltip` | provavel-forte | SimpleTooltipContentModel | 3/4 | `res/scripts/client/gui/impl/lobby/mode_selector/tooltips/mode_selector_alert_tooltip.py` |
| `R.views.lobby.mode_selector.tooltips.SimplyFormatTooltip` | provavel-forte | SimpleTooltipContentModel | 2/4 | `res/scripts/client/gui/impl/lobby/mode_selector/mode_selector_view.py` (+1) |
| `R.views.lobby.mode_selector.tooltips.common.Divider` | nao-encontrada | - | - | - |
| `R.views.lobby.mode_selector.tooltips.common.GradientDecorator` | nao-encontrada | - | - | - |
| `R.views.lobby.mode_selector.widgets.EpicWidget` | nao-encontrada | - | - | - |
| `R.views.lobby.mode_selector.widgets.RankedWidget` | nao-encontrada | - | - | - |
| `R.views.lobby.nation_change.nation_change_screen.NationChangeScreen` | provavel | - | - | `res/scripts/client/gui/shared/event_dispatcher.py` |
| `R.views.lobby.offers.OfferBannerWindow` | provavel-forte | OfferBannerModel | 6/6 | `res/scripts/client/gui/impl/lobby/offers/offer_banner_window.py` (+1) |
| `R.views.lobby.offers.OfferGiftsWindow` | provavel-forte | OfferModel | 14/15 | `res/scripts/client/gui/impl/lobby/offers/offer_gifts_window.py` (+1) |
| `R.views.lobby.offers.OfferRewardWindow` | provavel | - | - | `res/scripts/client/gui/shared/event_dispatcher.py` |
| `R.views.lobby.personal_exchange_rates.AllPersonalExchangesView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/exchange/exchange_rates_helper.py` |
| `R.views.lobby.personal_exchange_rates.ExperienceExchangeView` | provavel | - | - | `res/scripts/client/gui/customization/constants.py` (+1) |
| `R.views.lobby.personal_exchange_rates.GoldExchangeView` | provavel | - | - | `res/scripts/client/gui/customization/constants.py` (+1) |
| `R.views.lobby.personal_exchange_rates.tooltips.ExchangeLimitTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/dialogs/buy_and_exchange.py` (+3) |
| `R.views.lobby.personal_exchange_rates.tooltips.ExchangeRateTooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/dialogs/buy_and_exchange.py` (+3) |
| `R.views.lobby.personal_reserves.BoosterTooltip` | provavel | ReservesActivationViewModel | 3/10 | `res/scripts/client/gui/impl/lobby/personal_reserves/booster_tooltip.py` (+1) |
| `R.views.lobby.personal_reserves.PersonalReservesTooltip` | provavel | ReservesEntryPointModel | 1/7 | `res/scripts/client/gui/impl/lobby/page/reserves_entry_point_presenter.py` (+1) |
| `R.views.lobby.personal_reserves.PersonalReservesWidget` | provavel | ReservesEntryPointModel | 3/7 | `res/scripts/client/gui/impl/lobby/personal_reserves/personal_reserves_widget.py` |
| `R.views.lobby.personal_reserves.QuestBoosterTooltip` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/impl/lobby/personal_reserves/quest_booster_tooltip.py` (+2) |
| `R.views.lobby.personal_reserves.ReserveCard` | nao-encontrada | - | - | - |
| `R.views.lobby.personal_reserves.ReserveCardTooltip` | nao-encontrada | - | - | - |
| `R.views.lobby.personal_reserves.ReserveGroup` | nao-encontrada | - | - | - |
| `R.views.lobby.personal_reserves.ReservesActivationView` | provavel-forte | ReservesActivationViewModel | 10/10 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+2) |
| `R.views.lobby.personal_reserves.ReservesIntroView` | provavel-forte | ReservesIntroViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/personal_reserves/personal_reserves_intro.py` |
| `R.views.lobby.platoon.AlertTooltip` | provavel-forte | AlertTooltipModel | 2/2 | `res/scripts/client/gui/impl/lobby/platoon/tooltip/platoon_alert_tooltip.py` (+3) |
| `R.views.lobby.platoon.MembersWindow` | provavel-forte | SlotLabelElementModel | 3/3 | `res/fun_random/scripts/client/FunRandomPersonality.py` (+2) |
| `R.views.lobby.platoon.PlatoonDropdown` | provavel-forte | PlatoonDropdownModel | 11/11 | `res/scripts/client/gui/impl/lobby/platoon/platoon_config.py` (+1) |
| `R.views.lobby.platoon.SearchingDropdown` | provavel-forte | SearchingDropdownModel | 8/8 | `res/scripts/client/gui/impl/lobby/platoon/platoon_config.py` (+1) |
| `R.views.lobby.platoon.SettingsPopover` | provavel | SettingsModel | 0/2 | `res/scripts/client/gui/impl/lobby/platoon/view/subview/platoon_tiers_filter_subview.py` |
| `R.views.lobby.platoon.WTRTooltip` | provavel-forte | CommonPlayerDataModel | 4/5 | `res/scripts/client/gui/impl/lobby/platoon/tooltip/platoon_wtr_tooltip.py` (+1) |
| `R.views.lobby.platoon.subViews.Chat` | provavel | ChatModel | 1/5 | `res/scripts/client/gui/impl/lobby/platoon/view/subview/platoon_chat_subview.py` |
| `R.views.lobby.platoon.subViews.SettingsContent` | provavel | SettingsModel | 0/2 | `res/scripts/client/gui/impl/lobby/platoon/view/subview/platoon_tiers_filter_subview.py` |
| `R.views.lobby.platoon.subViews.TiersLimit` | provavel-forte | TiersLimitModel | 7/9 | `res/scripts/client/gui/impl/lobby/platoon/view/subview/platoon_tiers_limit_subview.py` |
| `R.views.lobby.player_subscriptions.PlayerSubscriptions` | provavel | UserAccountModel | 0/3 | `res/scripts/client/gui/impl/lobby/page/user_account_presenter.py` (+2) |
| `R.views.lobby.player_subscriptions.SubscriptionItem` | nao-encontrada | - | - | - |
| `R.views.lobby.player_subscriptions.SubscriptionRewardView` | provavel | SubscriptionRewardViewModel | 2/7 | `res/scripts/client/gui/impl/lobby/reward_window.py` |
| `R.views.lobby.premacc.tooltips.SquadBonusTooltip` | provavel | SlotLabelElementModel | 1/3 | `res/comp7/scripts/client/comp7/gui/impl/lobby/platoon/view/comp7_platoon_welcome_view.py` (+7) |
| `R.views.lobby.prestige.sharedComponents.PrestigeProgressSymbol` | nao-encontrada | - | - | - |
| `R.views.lobby.prestige.sharedComponents.PrestigeProgressTab` | nao-encontrada | - | - | - |
| `R.views.lobby.prestige.tooltips.EliteLevelGradesTooltip` | provavel-forte | PrestigeProfileTechniqueEmblemModel | 1/1 | `res/scripts/client/gui/impl/lobby/prestige/prestige_level_grades_tooltip_view.py` (+1) |
| `R.views.lobby.prestige.views.GlobalOnboardingView` | provavel-forte | GlobalOnboardingViewModel | 4/4 | `res/scripts/client/gui/impl/lobby/prestige/global_onboarding_view.py` |
| `R.views.lobby.prestige.views.PrestigeHangarEntryPoint` | provavel-forte | PrestigeHangarEntryPointModel | 4/4 | `res/scripts/client/gui/impl/lobby/prestige/prestige_hangar_entry_point_view.py` |
| `R.views.lobby.prestige.views.PrestigeProfileTechniqueEmblemView` | provavel-forte | PrestigeProfileTechniqueEmblemModel | 1/1 | `res/scripts/client/gui/impl/lobby/prestige/prestige_profile_technique_views.py` |
| `R.views.lobby.prestige.views.PrestigeProfileTechniqueView` | provavel-forte | PrestigeProfileTechniqueEmblemModel | 1/1 | `res/scripts/client/gui/impl/lobby/prestige/prestige_profile_technique_views.py` |
| `R.views.lobby.prestige.views.PrestigeRewardView` | provavel-forte | PrestigeRewardViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/prestige/prestige_reward_view.py` |
| `R.views.lobby.progressive_reward.progressive_reward_award.ProgressiveRewardAward` | provavel-forte | ProgressiveRewardAwardModel | 9/11 | `res/scripts/client/gui/impl/lobby/progressive_reward/progressive_reward_award_view.py` |
| `R.views.lobby.progressive_reward.progressive_reward_view.ProgressiveRewardView` | provavel | - | - | `res/scripts/client/gui/shared/event_dispatcher.py` |
| `R.views.lobby.ranked.QualificationRewardsView` | provavel-forte | RankedQualificationRewardsViewModel | 3/3 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_qualification_rewards.py` |
| `R.views.lobby.ranked.RankedSelectableRewardView` | provavel-forte | RankedSelectableRewardViewModel | 1/2 | `res/scripts/client/gui/impl/lobby/ranked/ranked_selectable_reward_view.py` |
| `R.views.lobby.ranked.YearLeaderboardView` | provavel-forte | YearLeaderboardViewModel | 7/7 | `res/scripts/client/gui/impl/lobby/ranked/year_leaderboard_view.py` |
| `R.views.lobby.ranked.ranked_year_award.RankedYearAward` | provavel-forte | RankedYearAwardModel | 11/11 | `res/scripts/client/gui/impl/lobby/ranked/ranked_year_award_view.py` |
| `R.views.lobby.ranked.tooltips.RankedBattlesRolesTooltipView` | provavel | SeniorityAwardsVehiclesViewModel | 0/10 | `res/comp7/scripts/client/comp7/gui/impl/lobby/dialogs/purchase_dialog.py` (+7) |
| `R.views.lobby.research.BuyModuleDialogView` | provavel-forte | BuyModuleDialogViewModel | 17/20 | `res/scripts/client/gui/impl/lobby/research/buy_module_dialog_view.py` (+1) |
| `R.views.lobby.research.InsufficientCreditsTooltip` | provavel | BuyModuleDialogViewModel | 1/20 | `res/scripts/client/gui/impl/lobby/research/buy_module_dialog_view.py` |
| `R.views.lobby.research.SoldModuleInfoTooltip` | provavel | BuyModuleDialogViewModel | 0/20 | `res/scripts/client/gui/impl/lobby/research/buy_module_dialog_view.py` |
| `R.views.lobby.reward_window.clan_reward_window_content.ClanRewardWindowContent` | provavel | SubscriptionRewardViewModel | 1/7 | `res/scripts/client/gui/impl/lobby/reward_window.py` |
| `R.views.lobby.reward_window.piggy_bank_reward_window_content.PiggyBankRewardWindowContent` | provavel | SubscriptionRewardViewModel | 1/7 | `res/scripts/client/gui/impl/lobby/reward_window.py` |
| `R.views.lobby.reward_window.reward_window_content.RewardWindowContent` | provavel | SubscriptionRewardViewModel | 1/7 | `res/scripts/client/gui/impl/lobby/reward_window.py` |
| `R.views.lobby.reward_window.twitch_reward_window_content.TwitchRewardWindowContent` | provavel | SubscriptionRewardViewModel | 1/7 | `res/scripts/client/gui/impl/lobby/reward_window.py` |
| `R.views.lobby.tanksetup.AmmunitionPanel` | provavel | - | - | `res/scripts/client/gui/impl/lobby/tank_setup/ammunition_panel/base_view.py` |
| `R.views.lobby.tanksetup.DeconstructionDeviceView` | provavel-forte | DeconstructionDeviceViewModel | 11/11 | `res/scripts/client/gui/impl/lobby/tank_setup/deconstruction_device_view.py` (+1) |
| `R.views.lobby.tanksetup.HangarAmmunitionSetup` | provavel | - | - | `res/scripts/client/gui/Scaleform/daapi/view/lobby/hangar/Hangar.py` (+2) |
| `R.views.lobby.tanksetup.IntroScreen` | provavel | - | - | `res/scripts/client/gui/impl/lobby/tank_setup/intro_ammunition_setup_view.py` |
| `R.views.lobby.tanksetup.VehicleCompareAmmunitionPanel` | provavel-forte | AmmunitionPanelViewModel | 6/8 | `res/scripts/client/gui/impl/lobby/vehicle_compare/ammunition_panel.py` |
| `R.views.lobby.tanksetup.VehicleCompareAmmunitionSetup` | provavel | - | - | `res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_configurator_view.py` (+1) |
| `R.views.lobby.tanksetup.common.Action` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.CtaButtons` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.DealPanel` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.DemountKit` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.ExtraImage` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.FormatColorTagText` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.Location` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.MaybeWrapper` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.Price` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SetupApp` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.ShortenedText` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.Slider` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SlotParts.Bonus` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SlotParts.Container` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SlotParts.Count` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SlotParts.Inside` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SlotParts.Level` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.Specializations` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SwitchButton` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.SwitchEquipment` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.Transitions.SlotTransitions` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.common.WeaponOccupancy` | nao-encontrada | - | - | - |
| `R.views.lobby.tanksetup.dialogs.Confirm` | provavel-forte | AmmunitionBuyModel | 18/23 | `res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py` (+9) |
| `R.views.lobby.tanksetup.dialogs.ConfirmActionsWithEquipmentDialog` | provavel-forte | ConfirmActionsWithEquipmentDialogModel | 10/15 | `res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py` (+4) |
| `R.views.lobby.tanksetup.dialogs.DeconstructConfirm` | provavel | - | - | `res/scripts/client/gui/impl/lobby/tank_setup/dialogs/deconstruct_confirm.py` |
| `R.views.lobby.tanksetup.dialogs.DeviceUpgradeDialog` | provavel | - | - | `res/scripts/client/gui/impl/lobby/tank_setup/upgradable_device/UpgradeDeviceView.py` |
| `R.views.lobby.tanksetup.dialogs.ExchangeToApplyEasyTankEquip` | provavel-forte | DialogWithExchange | 13/18 | `res/scripts/client/gui/impl/lobby/easy_tank_equip/dialogs/easy_tank_equip_exchange_dialog.py` (+1) |
| `R.views.lobby.tanksetup.dialogs.ExchangeToBuyItems` | provavel-forte | ExchangeWithItemsModel | 14/19 | `res/halloween/scripts/client/halloween/gui/game_control/halloween_controller.py` (+3) |
| `R.views.lobby.tanksetup.dialogs.ExchangeToUpgradeItems` | provavel-forte | ExchangeWithItemsModel | 14/19 | `res/scripts/client/gui/impl/dialogs/dialogs.py` (+1) |
| `R.views.lobby.tanksetup.dialogs.NeedRepair` | provavel-forte | NeedRepairModel | 15/20 | `res/scripts/client/gui/impl/lobby/tank_setup/dialogs/need_repair.py` (+1) |
| `R.views.lobby.tanksetup.dialogs.RefillShells` | provavel-forte | RefillShellsModel | 16/21 | `res/scripts/client/gui/impl/lobby/tank_setup/dialogs/refill_shells.py` (+1) |
| `R.views.lobby.tanksetup.dialogs.Sell` | provavel-forte | SellViewModel | 9/14 | `res/scripts/client/gui/impl/lobby/tank_setup/dialogs/opt_device_sell_dialog.py` (+1) |
| `R.views.lobby.tanksetup.tooltips.DeconstructFromInventoryTooltip` | provavel-forte | DeconstructFromInventoryTooltipModel | 2/2 | `res/scripts/client/gui/impl/lobby/tank_setup/dialogs/deconstruct_confirm.py` (+1) |
| `R.views.lobby.tanksetup.tooltips.DeconstructFromVehicleTooltip` | provavel-forte | DeconstructFromVehicleTooltipModel | 2/2 | `res/scripts/client/gui/impl/lobby/tank_setup/dialogs/deconstruct_confirm.py` (+1) |
| `R.views.lobby.tanksetup.tooltips.PopularLoadoutsTooltip` | provavel | OptionalDevicesAssistantModel | 0/4 | `res/scripts/client/gui/impl/lobby/hangar/presenters/optional_devices_assistant_presenter.py` (+2) |
| `R.views.lobby.tanksetup.tooltips.SetupTabTooltipView` | provavel | EquipmentsModel | 0/10 | `res/scripts/client/gui/impl/lobby/hangar/presenters/equipments_presenter.py` (+3) |
| `R.views.lobby.tanksetup.tooltips.WarningTooltipView` | provavel-forte | WarningTooltipViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/tank_setup/ammunition_setup/base_hangar.py` (+2) |
| `R.views.lobby.tooltips.AdditionalBattlePassRewardsTooltip` | provavel | BattlePassProgressModel | 0/29 | `res/scripts/client/gui/impl/lobby/battle_results/missions_progress/battle_pass_progress.py` (+1) |
| `R.views.lobby.tooltips.AdditionalRewardsTooltip` | provavel | BattleMattersMainViewModel | 1/10 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/progression_view.py` (+20) |
| `R.views.lobby.tooltips.BattleResultsStatsTooltipView` | provavel-forte | CriticalDamageTooltipModel | 1/2 | `res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/battle_efficiency.py` (+7) |
| `R.views.lobby.tooltips.TankmanTooltipView` | provavel-forte | TankmanTooltipViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/tooltips/tankman_tooltip_view.py` |
| `R.views.lobby.tooltips.VehPostProgressionEntryPointTooltip` | provavel-forte | VehPostProgressionEntryPointTooltipModel | 5/6 | `res/scripts/client/gui/impl/lobby/tooltips/veh_post_progression_entry_point_tooltip.py` (+1) |
| `R.views.lobby.tooltips.clans.ClanShortInfoTooltipContent` | provavel | - | - | `res/scripts/client/gui/impl/lobby/account_dashboard/features/header_feature.py` (+1) |
| `R.views.lobby.veh_post_progression.PostProgressionInfo` | provavel | - | - | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_intro.py` |
| `R.views.lobby.veh_post_progression.PostProgressionIntro` | provavel | - | - | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_intro.py` |
| `R.views.lobby.veh_post_progression.PostProgressionResearchSteps` | provavel-forte | ResearchStepsDialog | 11/16 | `res/scripts/client/gui/impl/lobby/veh_post_progression/dialogs/research_confirm.py` (+1) |
| `R.views.lobby.veh_post_progression.VehiclePostProgressionCmpView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_cmp_component.py` |
| `R.views.lobby.veh_post_progression.VehiclePostProgressionView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_cfg_component.py` |
| `R.views.lobby.veh_post_progression.common.Bonus` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.common.Description` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.common.Grid` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.common.PersistentBonuses` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.common.Slide` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.common.SlideContent` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.common.Slider` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.common.TextSplit` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.tooltip.PairModificationTooltipView` | provavel-forte | PairModificationTooltipViewModel | 8/8 | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_base_component.py` (+4) |
| `R.views.lobby.veh_post_progression.tooltip.PostProgressionLevelTooltipView` | provavel-forte | PostProgressionLevelTooltipViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_cfg_component.py` (+3) |
| `R.views.lobby.veh_post_progression.tooltip.RoleSlotTooltipView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_base_component.py` (+2) |
| `R.views.lobby.veh_post_progression.tooltip.SetupTooltipView` | provavel | - | - | `res/scripts/client/gui/impl/lobby/veh_post_progression/post_progression_base_component.py` (+3) |
| `R.views.lobby.veh_post_progression.tooltip.common.DisabledBlock` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.tooltip.common.FeatureLevelSubtitle` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.tooltip.common.Lock` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.tooltip.common.NotEnoughCredits` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.tooltip.common.PriceBlock` | nao-encontrada | - | - | - |
| `R.views.lobby.veh_post_progression.tooltip.common.Separator` | nao-encontrada | - | - | - |
| `R.views.lobby.vehicle_compare.CompareModificationsPanelView` | provavel-forte | CompareModificationsPanelViewModel | 4/5 | `res/scripts/client/gui/impl/lobby/vehicle_compare/modifications_panel.py` |
| `R.views.lobby.vehicle_compare.CompareSkillsPanelView` | provavel-forte | CompareSkillsPanelViewModel | 3/3 | `res/scripts/client/gui/impl/lobby/vehicle_compare/skills_panel.py` |
| `R.views.lobby.vehicle_compare.SelectSlotSpecCompareDialog` | provavel-forte | SelectSlotSpecCompareDialogModel | 10/15 | `res/scripts/client/gui/impl/lobby/vehicle_compare/select_slot_spec_compare_dialog.py` |
| `R.views.lobby.vehicle_compare.SkillSelectView` | provavel-forte | CompareSkillsPanelViewModel | 2/3 | `res/scripts/client/gui/impl/lobby/vehicle_compare/skill_select_view.py` (+2) |
| `R.views.lobby.vehicle_compare.tooltips.CrewRolesTooltip` | provavel | SkillSelectViewModel | 1/9 | `res/scripts/client/gui/impl/lobby/vehicle_compare/crew_roles_tooltip_view.py` (+1) |
| `R.views.lobby.vehicle_preview.buying_panel.StyleBuyingPanel` | provavel-forte | StyleBuyingPanelModel | 6/6 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_style_buying.py` |
| `R.views.lobby.vehicle_preview.buying_panel.VPProgressionStylesBuyingPanel` | provavel-forte | ProgressionStylesBuyingPanelModel | 8/8 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_style_progression.py` |
| `R.views.lobby.vehicle_preview.tabs.CrewTabView` | provavel-forte | CrewTabModel | 5/5 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/crew_tab_view.py` |
| `R.views.lobby.vehicle_preview.top_panel.TopPanelTabs` | provavel-forte | TopPanelTabsModel | 4/4 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/top_panel_tabs.py` |
| `R.views.mono.attachments_preview.attachments_preview` | provavel-forte | AttachmentsPreviewModel | 3/3 | `res/scripts/client/gui/impl/lobby/customization/attachments_preview/attachments_preview.py` |
| `R.views.mono.battle_hud.main` | provavel-forte | HudViewModel | 1/1 | `res/scripts/client/gui/impl/battle/random/hud.py` |
| `R.views.mono.battle_pass.dialogs.chapter_confirm` | provavel | ChapterConfirmViewModel | 2/5 | `res/scripts/client/gui/impl/lobby/battle_pass/activate_chapter_confirm_dialog.py` (+1) |
| `R.views.mono.battle_pass.full_screen_video` | provavel | FullscreenVideoViewModel | 1/4 | `res/scripts/client/gui/impl/lobby/battle_pass/fullscreen_video_view.py` |
| `R.views.mono.battle_pass.how_to_earn_points` | provavel-forte | BattlePassHowToEarnPointsViewModel | 3/5 | `res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_how_to_earn_points_view.py` |
| `R.views.mono.battle_pass.intro` | provavel-forte | BattlePassIntroViewModel | 1/2 | `res/scripts/client/gui/impl/lobby/battle_pass/intro_view.py` |
| `R.views.mono.battle_pass.main` | provavel | MainViewModel | 0/1 | `res/scripts/client/gui/impl/lobby/battle_pass/main_view.py` (+1) |
| `R.views.mono.battle_pass.rewards_screen` | provavel | BattlePassAwardsViewModel | 10/22 | `res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_awards_view.py` (+1) |
| `R.views.mono.battle_pass.rewards_selection` | provavel | BattlePassProgressionsViewModel | 1/54 | `res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_progressions_view.py` (+1) |
| `R.views.mono.battle_pass.tankmen_screen` | nao-encontrada | - | - | - |
| `R.views.mono.battle_pass.tooltips.bp_points` | provavel-forte | BattlePassPointsViewModel | 1/2 | `res/scripts/client/gui/battle_pass/battle_pass_decorators.py` (+1) |
| `R.views.mono.battle_pass.tooltips.bpcoin` | provavel | BonusModel | 0/2 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/decorators.py` (+11) |
| `R.views.mono.battle_pass.tooltips.bptaler` | provavel | BonusModel | 0/2 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/decorators.py` (+8) |
| `R.views.mono.battle_pass.tooltips.completed` | provavel | BattlePassCompletedTooltipViewModel | 1/4 | `res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_entry_point_view.py` (+3) |
| `R.views.mono.battle_pass.tooltips.crew_member_skill` | provavel | TankmanModel | 0/9 | `res/scripts/client/gui/battle_pass/battle_pass_decorators.py` (+2) |
| `R.views.mono.battle_pass.tooltips.gold_mission` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/battle_pass/battle_pass_decorators.py` (+2) |
| `R.views.mono.battle_pass.tooltips.in_progress` | provavel | BattlePassInProgressTooltipViewModel | 7/16 | `res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_entry_point_view.py` (+2) |
| `R.views.mono.battle_pass.tooltips.lock_icon` | provavel | BattlePassLockIconTooltipViewModel | 0/1 | `res/scripts/client/gui/battle_pass/battle_pass_decorators.py` (+1) |
| `R.views.mono.battle_pass.tooltips.no_chapter` | provavel-forte | BattlePassNoChapterTooltipViewModel | 1/1 | `res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_entry_point_view.py` (+2) |
| `R.views.mono.battle_pass.tooltips.on_pause` | provavel | VehicleStatisticModel | 0/23 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/vehicles_data_providers/ls_vehicle_statistics_presenter.py` (+1) |
| `R.views.mono.battle_pass.tooltips.quest_chain` | provavel | TokenBonusModel | 0/3 | `res/scripts/client/gui/battle_pass/battle_pass_bonuses_packers.py` (+2) |
| `R.views.mono.battle_pass.tooltips.random_quest` | provavel | TokenBonusModel | 0/3 | `res/scripts/client/gui/battle_pass/battle_pass_bonuses_packers.py` (+2) |
| `R.views.mono.battle_pass.tooltips.reward_compensation` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/battle_pass/battle_pass_bonuses_packers.py` (+4) |
| `R.views.mono.battle_pass.tooltips.upgrade_style` | provavel | TokenBonusModel | 0/3 | `res/scripts/client/gui/battle_pass/battle_pass_bonuses_packers.py` (+2) |
| `R.views.mono.battle_pass.tooltips.vehicle_bp_points` | provavel | VehiclePointsTooltipViewModel | 1/11 | `res/last_stand/scripts/client/last_stand/gui/impl/lobby/vehicles_data_providers/ls_vehicle_statistics_presenter.py` (+2) |
| `R.views.mono.battle_pass.vehicle_cap_award` | provavel | BattlePassVehicleAwardViewModel | 1/7 | `res/scripts/client/gui/impl/lobby/battle_pass/battle_pass_vehicle_award_view.py` |
| `R.views.mono.challenges.awards_view` | provavel-forte | AwardsViewModel | 8/8 | `res/scripts/client/gui/impl/lobby/challenges/awards_view.py` |
| `R.views.mono.challenges.dialogs.challenge_dialog` | provavel-forte | PriceItemModel | 2/3 | `res/scripts/client/gui/impl/lobby/challenges/confirmation_view.py` (+1) |
| `R.views.mono.challenges.main` | nao-encontrada | - | - | - |
| `R.views.mono.crew.welcome_screen` | provavel-forte | WelcomeScreenViewModel | 1/1 | `res/scripts/client/gui/impl/lobby/crew/welcome_screen_view.py` |
| `R.views.mono.dialogs.default_dialog` | provavel | - | - | `res/scripts/client/gui/impl/dialogs/dialogs.py` (+2) |
| `R.views.mono.dialogs.pro_boost_switch_dialog` | provavel | - | - | `res/scripts/client/gui/impl/lobby/dialogs/wot_plus/pro_boost_switch_dialog.py` |
| `R.views.mono.dialogs.research_confirm_dialog` | provavel-forte | ResearchConfirmDialogViewModel | 3/5 | `res/scripts/client/gui/impl/lobby/dialogs/research_confirm.py` (+1) |
| `R.views.mono.dialogs.wot_plus_activated_dialog` | provavel | - | - | `res/scripts/client/gui/impl/lobby/dialogs/wot_plus/subscription_award_dialog.py` |
| `R.views.mono.hangar.footer` | provavel-forte | DefaultModel | 2/2 | `res/scripts/client/gui/impl/lobby/page/lobby_footer.py` |
| `R.views.mono.hangar.header` | provavel-forte | DefaultModel | 1/2 | `res/scripts/client/gui/impl/lobby/page/lobby_header.py` |
| `R.views.mono.hangar.main` | provavel-forte | RouterModel | 3/4 | `res/scripts/client/gui/impl/lobby/hangar/random/random_hangar.py` |
| `R.views.mono.hangar.overlays.playlist` | provavel | - | - | `res/scripts/client/gui/impl/lobby/hangar/dialogs/vehicle_playlists.py` |
| `R.views.mono.hangar.tooltips` | nao-encontrada | - | - | - |
| `R.views.mono.hangar.vehicle_tooltip` | provavel | VehiclesInventoryModel | 1/16 | `res/frontline/scripts/client/frontline/gui/impl/lobby/presenters/fl_vehicle_inventory_presenter.py` (+4) |
| `R.views.mono.integrated_auction.tooltips.auction_event_banner_tooltip` | provavel | AuctionEventBannerTooltipModel | 0/2 | `res/scripts/client/gui/integrated_auction/tooltips/event_banner_tooltip.py` |
| `R.views.mono.lobby.collector20_reward` | provavel | AwardsViewModel | 1/8 | `res/scripts/client/gui/impl/lobby/collector20_reward/collector20_reward_view.py` |
| `R.views.mono.lobby.elite_window` | provavel-forte | EliteViewModel | 6/6 | `res/scripts/client/gui/impl/lobby/elite_window/elite_view.py` |
| `R.views.mono.lobby.select_vehicle` | provavel-forte | SelectVehicleModel | 5/5 | `res/scripts/client/gui/impl/lobby/select_vehicle/select_vehicle.py` |
| `R.views.mono.lobby.veh_skill_tree.comparison` | provavel-forte | CompareUpgradesPanelViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/vehicle_compare/upgrades_panel.py` |
| `R.views.mono.lobby.veh_skill_tree.dialogs.alternate_configuration` | provavel | - | - | `res/scripts/client/gui/impl/lobby/veh_skill_tree/dialogs/alternate_configuration_dialog.py` (+1) |
| `R.views.mono.lobby.veh_skill_tree.intro_page` | provavel-forte | BaseIntroViewModel | 4/7 | `res/scripts/client/gui/impl/lobby/veh_skill_tree/dialogs/intro_page_view.py` |
| `R.views.mono.lobby.veh_skill_tree.notifications.perk_available` | provavel | - | - | `res/scripts/client/gui/impl/lobby/vehicle_hub/__init__.py` |
| `R.views.mono.lobby.veh_skill_tree.rarity_reward_screen` | provavel-forte | RarityRewardScreenModel | 2/4 | `res/scripts/client/gui/impl/lobby/veh_skill_tree/rarity_reward_screen/rarity_reward_screen.py` |
| `R.views.mono.lobby.veh_skill_tree.reward_screen` | provavel-forte | RewardScreenViewModel | 4/4 | `res/scripts/client/gui/impl/lobby/veh_skill_tree/rewards/prestige_milestone_achived_view.py` |
| `R.views.mono.lootbox.auto_open` | provavel-forte | AutoOpenViewModel | 5/5 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+1) |
| `R.views.mono.lootbox.dialogs.reroll_dialog` | provavel | ConfirmationModel | 3/9 | `res/scripts/client/gui/impl/lobby/lootbox_system/base/box_reroll_dialog.py` (+1) |
| `R.views.mono.lootbox.info_page` | provavel | - | - | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+2) |
| `R.views.mono.lootbox.main` | provavel | - | - | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+4) |
| `R.views.mono.lootbox.tooltips.box_compensation` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/box_tooltip.py` (+2) |
| `R.views.mono.lootbox.tooltips.box_tooltip` | provavel | BonusModel | 0/2 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/decorators.py` (+8) |
| `R.views.mono.lootbox.tooltips.entry_point` | provavel | EntryPointTooltipViewModel | 0/4 | `res/scripts/client/gui/impl/lobby/hangar/presenters/lootbox_entry_point_presenter.py` (+1) |
| `R.views.mono.lootbox.tooltips.guaranteed_reward_info` | provavel-forte | GuaranteedRewardInfoTooltipViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/guaranteed_reward_info_tooltip.py` (+1) |
| `R.views.mono.lootbox.tooltips.random_national_bonus` | provavel | BonusModel | 0/2 | `res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/random_national_bonus_tooltip_view.py` (+2) |
| `R.views.mono.lootbox.tooltips.reroll` | provavel | BoxRerollTooltipModel | 1/4 | `res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/box_reroll_tooltip.py` (+1) |
| `R.views.mono.lootbox.tooltips.statistics_category` | provavel-forte | StatisticsCategoryTooltipViewModel | 4/4 | `res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/statistics_category_tooltip.py` (+1) |
| `R.views.mono.maps_training.maps_training_page` | provavel | - | - | `res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/vehicle_preview.py` (+2) |
| `R.views.mono.maps_training.maps_training_queue` | provavel | - | - | `res/scripts/client/gui/impl/lobby/maps_training/maps_training_queue_view.py` (+1) |
| `R.views.mono.maps_training.maps_training_result` | provavel-forte | MapsTrainingResultModel | 13/14 | `res/scripts/client/gui/impl/lobby/maps_training/maps_training_result_view.py` |
| `R.views.mono.maps_training.scenario_tooltip` | provavel-forte | MapsTrainingScenarioTooltipModel | 8/8 | `res/scripts/client/gui/impl/lobby/maps_training/maps_training_view.py` (+1) |
| `R.views.mono.personal_missions_30.assembling_video` | provavel-forte | AssemblingVideoViewModel | 3/3 | `res/scripts/client/gui/impl/lobby/personal_missions_30/stage_view.py` |
| `R.views.mono.personal_missions_30.campaign_selector` | provavel-forte | CampaignSelectorModel | 7/7 | `res/scripts/client/gui/impl/lobby/personal_missions_30/campaign_selector_view.py` |
| `R.views.mono.personal_missions_30.intro_screen` | provavel-forte | IntroScreenModel | 1/1 | `res/scripts/client/gui/impl/lobby/personal_missions_30/intro_view.py` |
| `R.views.mono.personal_missions_30.main` | provavel | MainViewModel | 0/1 | `res/scripts/client/gui/impl/lobby/personal_missions_30/main_view.py` |
| `R.views.mono.personal_missions_30.rewards` | provavel-forte | RewardsViewModel | 3/5 | `res/scripts/client/gui/impl/lobby/personal_missions_30/rewards_view.py` |
| `R.views.mono.personal_missions_30.tooltips.mission_progress_tooltip` | provavel | MainViewModel | 0/1 | `res/scripts/client/gui/impl/lobby/battle_results/missions_progress/personal_missions_progress.py` (+2) |
| `R.views.mono.personal_missions_30.tooltips.missions_category_tooltip` | provavel | MainViewModel | 0/1 | `res/scripts/client/gui/impl/lobby/battle_results/missions_progress/personal_missions_progress.py` (+2) |
| `R.views.mono.personal_missions_30.tooltips.param_tooltip` | provavel | - | - | `res/scripts/client/gui/shared/tooltips/contexts.py` |
| `R.views.mono.personal_missions_30.tooltips.umg_tooltip` | provavel-forte | UmgTooltipModel | 13/16 | `res/scripts/client/gui/impl/lobby/personal_missions_30/tooltips/umg_tooltip.py` (+1) |
| `R.views.mono.pet_system.event_view` | provavel | - | - | `res/scripts/client/gui/impl/lobby/pet_system/event_view.py` |
| `R.views.mono.pet_system.fullscreen_event_view` | provavel | - | - | `res/scripts/client/gui/impl/lobby/pet_system/fullscreen_event_view.py` |
| `R.views.mono.pet_system.info_page` | nao-encontrada | - | - | - |
| `R.views.mono.pet_system.pet_house_marker` | provavel-forte | PetHouseMarkerModel | 3/3 | `res/scripts/client/gui/impl/lobby/pet_system/pet_house_marker_view.py` |
| `R.views.mono.pet_system.pet_storage` | provavel | - | - | `res/scripts/client/gui/impl/lobby/pet_system/pet_storage_view.py` |
| `R.views.mono.pet_system.tooltips.pet_storage_tooltip` | provavel | PetObjectTooltipModel | 0/2 | `res/scripts/client/gui/impl/lobby/hangar/presenters/pet_object_tooltip_presenter.py` (+1) |
| `R.views.mono.pet_system.tooltips.pet_tooltip` | provavel | PetTooltipModel | 1/5 | `res/scripts/client/gui/impl/lobby/pet_system/tooltips/pet_tooltip.py` |
| `R.views.mono.pet_system.tooltips.synergy_tooltip` | provavel | SynergyTooltipModel | 0/1 | `res/scripts/client/gui/impl/lobby/pet_system/pet_storage_view.py` (+1) |
| `R.views.mono.post_battle.flag` | provavel | - | - | `res/scripts/client/gui/impl/lobby/battle_results/flag_view.py` |
| `R.views.mono.post_battle.random` | provavel-forte | RandomBattleResultsViewModel | 11/12 | `res/scripts/client/gui/impl/lobby/battle_results/random_battle_results_view.py` |
| `R.views.mono.post_battle.tooltips.critical_damage` | provavel-forte | CriticalDamageTooltipModel | 1/2 | `res/comp7/scripts/client/comp7/gui/impl/lobby/battle_results/submodel_presenters/battle_efficiency.py` (+5) |
| `R.views.mono.prebattle_highlights.main` | provavel | - | - | `res/scripts/client/gui/impl/battle/prebattle_highlights/prebattle_highlights_view.py` |
| `R.views.mono.rest_bonus.tooltips.rest_bonus_tooltip` | provavel | VehicleStatisticModel | 0/23 | `res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_statistics_presenter.py` (+1) |
| `R.views.mono.seniority_awards.notifications.manual_claim` | provavel | - | - | `res/scripts/client/gui/impl/lobby/seniority_awards/__init__.py` |
| `R.views.mono.seniority_awards.notifications.tokens` | provavel | - | - | `res/scripts/client/gui/impl/lobby/seniority_awards/__init__.py` |
| `R.views.mono.seniority_awards.notifications.vehicles` | provavel | - | - | `res/scripts/client/gui/impl/lobby/seniority_awards/__init__.py` |
| `R.views.mono.seniority_awards.rewards` | provavel | - | - | `res/scripts/client/gui/shared/event_dispatcher.py` |
| `R.views.mono.seniority_awards.tooltips.seniority_tooltip` | provavel | SeniorityAwardsTooltipModel | 1/4 | `res/scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_vehicles_view.py` (+2) |
| `R.views.mono.seniority_awards.vehicle_rewards` | provavel | - | - | `res/scripts/client/gui/shared/event_dispatcher.py` |
| `R.views.mono.stronghold_event.tooltips.event_banner_tooltip` | provavel | StrongholdEventBannerTooltipViewModel | 0/3 | `res/scripts/client/gui/impl/lobby/stronghold_event/tooltips/stronghold_event_banner_tooltip.py` |
| `R.views.mono.tech_tree.main` | provavel-forte | TechTreeViewModel | 11/12 | `res/scripts/client/gui/graphics_optimization_controller/settings.py` (+1) |
| `R.views.mono.template.main` | nao-encontrada | - | - | - |
| `R.views.mono.tooltips.tooltips` | nao-encontrada | - | - | - |
| `R.views.mono.user_missions.hub` | provavel-forte | HubViewModel | 4/4 | `res/scripts/client/gui/Scaleform/daapi/view/lobby/user_missions/states.py` (+1) |
| `R.views.mono.user_missions.hub.mission_hub_intro_view` | provavel-forte | MissionHubIntroViewModel | 5/5 | `res/scripts/client/gui/impl/lobby/user_missions/hub/mission_hub_intro_view.py` |
| `R.views.mono.user_missions.info_page` | provavel | - | - | `res/scripts/client/gui/Scaleform/daapi/view/lobby/user_missions/states.py` |
| `R.views.mono.user_missions.notifications.complete_notification` | provavel | - | - | `res/scripts/client/gui/impl/lobby/challenges/__init__.py` |
| `R.views.mono.user_missions.notifications.fail_notification` | provavel | - | - | `res/scripts/client/gui/impl/lobby/challenges/__init__.py` |
| `R.views.mono.user_missions.notifications.mission_complete_notification` | provavel | - | - | `res/scripts/client/gui/impl/lobby/challenges/__init__.py` |
| `R.views.mono.user_missions.notifications.shield_notification` | provavel | - | - | `res/scripts/client/gui/impl/lobby/challenges/__init__.py` |
| `R.views.mono.user_missions.notifications.start_notification` | provavel | - | - | `res/scripts/client/gui/impl/lobby/challenges/__init__.py` |
| `R.views.mono.user_missions.tooltips.all_quests_done_tooltip` | provavel-forte | AllQuestsDoneTooltipModel | 1/1 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/quests_presenter.py` (+3) |
| `R.views.mono.user_missions.tooltips.challenges_banner_tooltip` | provavel-forte | ChallengesBannerTooltipModel | 5/6 | `res/scripts/client/gui/impl/lobby/user_missions/tooltips/challenges_banner_tooltip.py` |
| `R.views.mono.user_missions.tooltips.challenges_restart_tooltip` | provavel | ChallengeMissions | 0/9 | `res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/challenges/challenge_missions_tab.py` (+1) |
| `R.views.mono.user_missions.tooltips.challenges_shields_tooltip` | provavel | - | - | `res/scripts/client/gui/challenges/challenges_decorators.py` (+1) |
| `R.views.mono.user_missions.tooltips.daily_quest_tooltip` | provavel | QuestsListModel | 0/3 | `res/battle_royale/scripts/client/battle_royale/gui/impl/lobby/views/user_missions/hangar_widget/presenters/quests_presenter.py` (+4) |
| `R.views.mono.user_missions.tooltips.daily_reroll_tooltip` | provavel | DailyMissionsBlockModel | 0/6 | `res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/daily_missions_block_presenter.py` (+1) |
| `R.views.mono.user_missions.tooltips.param_tooltip` | nao-encontrada | - | - | - |
| `R.views.mono.user_missions.tooltips.pm4_banner_tooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/user_missions/tooltips/pm4_banner_tooltip.py` |
| `R.views.mono.user_missions.tooltips.weekly_quest_tooltip` | provavel | QuestsListModel | 0/3 | `res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/presenters/quests_presenter.py` (+1) |
| `R.views.mono.vehicle_hub.main` | provavel | - | - | `res/scripts/client/gui/impl/lobby/vehicle_hub/vehicle_hub_main_view.py` |
| `R.views.mono.vehicle_hub.tooltips.armor_tooltip` | provavel-forte | ArmorTooltipModel | 5/5 | `res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/armor_tooltip.py` |
| `R.views.mono.vehicle_hub.tooltips.back_to_main_progression_tooltip` | nao-encontrada | - | - | - |
| `R.views.mono.vehicle_hub.tooltips.minor_short_tooltip` | provavel-forte | MinorShortTooltipModel | 3/3 | `res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/armor_sub_presenter.py` (+1) |
| `R.views.mono.vehicle_hub.tooltips.minor_tooltip` | provavel | - | - | `res/scripts/client/gui/impl/lobby/vehicle_hub/sub_presenters/armor/armor_sub_presenter.py` (+1) |
| `R.views.mono.vehicle_hub.tooltips.perk_tooltip` | provavel-forte | BasePerkTooltipModel | 2/2 | `res/scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/common_perk_tooltip.py` (+4) |
| `R.views.mono.vehicle_hub.tooltips.prestige_reward_tooltip` | provavel-forte | PrestigeRewardTooltipModel | 1/1 | `res/scripts/client/gui/impl/lobby/veh_skill_tree/tooltips/prestige_reward_tooltip.py` (+1) |
| `R.views.mono.vehicle_hub.tooltips.vanity_entry_point_tooltip` | nao-encontrada | - | - | - |
| `R.views.mono.winback.popovers.winback_leave_mode_popover_view` | provavel-forte | WinbackLeaveModePopoverViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/mode_selector/items/winback_mode_selector_item.py` (+2) |
| `R.views.mono.winback.tooltips.main_reward_tooltip` | provavel | RewardProgressBlockModel | 0/3 | `res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/reward_progress_block_presenter.py` (+1) |
| `R.views.mono.winback.tooltips.mode_info_tooltip` | provavel | WinbackLeaveModePopoverViewModel | 0/2 | `res/scripts/client/gui/impl/lobby/winback/popovers/winback_leave_mode_popover_view.py` (+1) |
| `R.views.mono.winback.tooltips.selectable_reward_tooltip` | provavel | RewardProgressBlockModel | 0/3 | `res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/reward_progress_block_presenter.py` (+4) |
| `R.views.mono.winback.tooltips.selected_rewards_tooltip` | provavel-forte | SelectedRewardsTooltipModel | 1/1 | `res/scripts/client/gui/impl/lobby/winback/tooltips/selected_rewards_tooltip.py` (+1) |
| `R.views.mono.winback.winback_leave_mode_dialog_view` | provavel-forte | WinbackLeaveModeDialogViewModel | 2/2 | `res/scripts/client/gui/impl/lobby/winback/winback_leave_mode_dialog_view.py` (+1) |
| `R.views.mono.winback.winback_reward_view` | provavel-forte | WinbackRewardViewModel | 8/8 | `res/scripts/client/gui/impl/lobby/winback/winback_reward_view.py` |
| `R.views.mono.winback.winback_selectable_reward_view` | provavel-forte | WinbackSelectableRewardViewModel | 9/9 | `res/scripts/client/gui/impl/lobby/winback/winback_selectable_reward_view.py` |
| `R.views.mono.winback.winback_umg_intro_view` | provavel | WinbackUmgIntroViewModel | 1/4 | `res/scripts/client/gui/impl/lobby/winback/winback_umg_intro_view.py` (+1) |
| `R.views.open_bundle.mono.lobby.confirmation` | provavel-forte | ConfirmationModel | 6/6 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/confirmation_view.py` (+1) |
| `R.views.open_bundle.mono.lobby.intro` | provavel-forte | IntroViewModel | 2/4 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/intro_view.py` |
| `R.views.open_bundle.mono.lobby.main` | provavel-forte | MainViewModel | 8/11 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/main_view.py` (+2) |
| `R.views.open_bundle.mono.lobby.notifications.special_rewards_notification` | nao-encontrada | - | - | - |
| `R.views.open_bundle.mono.lobby.notifications.start_notification` | nao-encontrada | - | - | - |
| `R.views.open_bundle.mono.lobby.tooltips.event_banner` | provavel | EventBannerTooltipModel | 0/2 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/tooltips/event_banner_tooltip.py` |
| `R.views.open_bundle.mono.lobby.tooltips.fixed_rewards` | provavel | MainViewModel | 0/11 | `res/open_bundle/scripts/client/open_bundle/gui/impl/lobby/main_view.py` (+1) |
| `R.views.resource_well.mono.lobby.award_view` | provavel-forte | AwardViewModel | 3/5 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/award_view.py` (+1) |
| `R.views.resource_well.mono.lobby.completed_progression_view` | provavel-forte | CompletedProgressionViewModel | 5/7 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/completed_progression_view.py` |
| `R.views.resource_well.mono.lobby.no_serial_vehicles_confirm` | provavel-forte | NoSerialVehiclesConfirmModel | 4/5 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/no_serial_vehicles_confirm.py` (+1) |
| `R.views.resource_well.mono.lobby.no_vehicles_confirm` | provavel-forte | NoVehiclesConfirmModel | 2/2 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/no_vehicles_confirm.py` |
| `R.views.resource_well.mono.lobby.progression_view` | provavel-forte | ProgressionViewModel | 8/16 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/progression_view.py` |
| `R.views.resource_well.mono.lobby.resources_loading_confirm` | provavel-forte | ResourcesLoadingConfirmModel | 5/8 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/resources_loading_confirm.py` (+1) |
| `R.views.resource_well.mono.lobby.resources_loading_view` | provavel-forte | ResourcesLoadingViewModel | 6/10 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/resources_loading_view.py` |
| `R.views.resource_well.mono.lobby.tooltips.event_banner_tooltip` | provavel | EventBannerTooltipModel | 1/4 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/tooltips/event_banner_tooltip.py` |
| `R.views.resource_well.mono.lobby.tooltips.max_progress_tooltip` | provavel | ResourcesLoadingViewModel | 0/10 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/resources_loading_view.py` (+1) |
| `R.views.resource_well.mono.lobby.tooltips.progress_tooltip` | provavel | ProgressionViewModel | 0/16 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/progression_view.py` (+2) |
| `R.views.resource_well.mono.lobby.tooltips.serial_number_tooltip` | provavel | AwardViewModel | 0/5 | `res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/award_view.py` (+3) |
| `R.views.resource_well.mono.lobby.tooltips.simple_tooltip` | nao-encontrada | - | - | - |
| `R.views.resource_well.mono.lobby.vehicle_preview_bottom_panel` | provavel | WellPanelModel | 2/6 | `res/resource_well/scripts/client/resource_well/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/vehicle_preview_bottom_panel.py` |
| `R.views.server_side_replay.lobby.MetaReplaysView` | provavel | - | - | `res/server_side_replay/scripts/client/server_side_replay/gui/shared/event_dispatcher.py` |
| `R.views.server_side_replay.lobby.popovers.ReplaysFilterPopover` | provavel-forte | ReplaysFilterPopoverModel | 15/15 | `res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/pages/best_replays_page.py` (+2) |
| `R.views.story_mode.mono.battle.epilogue_window` | provavel-forte | EpilogueWindowViewModel | 2/2 | `res/story_mode/scripts/client/story_mode/gui/impl/battle/epilogue_window.py` (+1) |
| `R.views.story_mode.mono.battle.onboarding_battle_result_view` | provavel-forte | OnboardingBattleResultViewModel | 4/4 | `res/story_mode/scripts/client/story_mode/gui/impl/battle/onboarding_battle_result_view.py` (+1) |
| `R.views.story_mode.mono.battle.prebattle_window` | provavel-forte | PrebattleWindowViewModel | 4/4 | `res/story_mode/scripts/client/story_mode/gui/impl/battle/prebattle_window.py` (+1) |
| `R.views.story_mode.mono.lobby.battle_result_view` | provavel-forte | BattleResultViewModel | 16/16 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/battle_result_view.py` (+1) |
| `R.views.story_mode.mono.lobby.congratulations_window` | provavel-forte | CongratulationsWindowViewModel | 7/7 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/congratulations_window.py` (+2) |
| `R.views.story_mode.mono.lobby.event_welcome_view` | provavel | - | - | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/event_welcome_view.py` (+2) |
| `R.views.story_mode.mono.lobby.mission_selection_view` | provavel | - | - | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/mission_selection_view.py` (+1) |
| `R.views.story_mode.mono.lobby.newbie_advertising_view` | provavel | - | - | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/newbie_advertising_view.py` (+1) |
| `R.views.story_mode.mono.lobby.onboarding_queue_view` | provavel | PrebattleWindowViewModel | 1/4 | `res/story_mode/scripts/client/story_mode/gui/impl/battle/prebattle_window.py` (+1) |
| `R.views.story_mode.mono.lobby.tooltips.badge_tooltip` | provavel-forte | BadgeTooltipViewModel | 7/7 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/badge_tooltip.py` (+1) |
| `R.views.story_mode.mono.lobby.tooltips.battle_result_stat_tooltip` | provavel-forte | BattleResultStatTooltipModel | 3/3 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/battle_result_stat_tooltip.py` (+1) |
| `R.views.story_mode.mono.lobby.tooltips.difficulty_tooltip` | provavel | MissionDifficultyTooltipModel | 1/4 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/difficulty_tooltip.py` (+1) |
| `R.views.story_mode.mono.lobby.tooltips.event_banner_tooltip` | provavel | EventBannerTooltipModel | 0/1 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/event_banner_tooltip.py` |
| `R.views.story_mode.mono.lobby.tooltips.medal_tooltip` | provavel | CongratulationsWindowViewModel | 0/7 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/congratulations_window.py` |
| `R.views.story_mode.mono.lobby.tooltips.mission_tooltip` | provavel-forte | MissionSelectionTooltipModel | 3/3 | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/mission_selection_view.py` (+1) |
| `R.views.story_mode.mono.lobby.tooltips.newbie_banner_tooltip` | provavel | - | - | `res/story_mode/scripts/client/story_mode/gui/impl/lobby/newbie_banner_tooltip.py` |

Detalhes de cada view (ficheiros, dependências, eventos `engine.*`, comandos, propriedades do
ViewModel em falta no JS) em `manifests/views/<R.views>.json`.
