package net.polarfox.SettingsConstructor.views
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import net.polarfox.SettingsConstructor.components.vxSettingsApiComponent;
   import net.polarfox.SettingsConstructor.events.LoggerEvent;
   import net.polarfox.SettingsConstructor.events.vxSettingsApiComponentEvent;
   import net.polarfox.SettingsConstructor.lang.LANGUAGES;
   import net.polarfox.SettingsConstructor.lang.STRINGS;
   import net.polarfox.SettingsConstructor.utils.Constants;
   import net.wg.gui.components.controls.ScrollBar;
   import net.wg.gui.components.controls.ScrollPane;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.infrastructure.base.AbstractWindowView;
   
   public class vxSettingsAPI extends AbstractWindowView
   {
      
      public static var manager:vxSettingsAPI = null;
      
      public var realm:String = "";
      
      public var scrollPane:ScrollPane;
      
      public var scrollBar:ScrollBar;
      
      public var modsContainer:MovieClip;
      
      public var modsArray:Array;
      
      public var modsData:Object;
      
      public var getModsDataS:Function;
      
      public var sendDataS:Function;
      
      public var callButtonsS:Function;
      
      public var handleHotKeysS:Function;
      
      public var flashLogS:Function;
      
      public var sendCallbackS:Function;
      
      public var currentLang:Object;
      
      public var onDataChangedS:Function;
      
      public var btnOk:SoundButtonEx;
      
      public var btnCancel:SoundButtonEx;
      
      public var btnApply:SoundButtonEx;
      
      public var btnReset:SoundButtonEx;
      
      private var isDestroying:Boolean = false;
      
      private var configChanged:Boolean = false;
      
      private var configChangedLinkages:Array;
      
      public function vxSettingsAPI()
      {
         super();
         this.currentLang = LANGUAGES.RU;
         this.configChanged = false;
         this.configChangedLinkages = new Array();
         this.modsArray = new Array();
         this.width = 960;
         this.height = 700;
         this.canResize = false;
         this.isCentered = true;
         manager = this;
      }
      
      public function handleLoggerEvent(param1:LoggerEvent) : void
      {
         this.flashLogS(param1.data);
      }
      
      override protected function onPopulate() : void
      {
         super.onPopulate();
         this.processLoad();
      }
      
      private function processLoad() : void
      {
         if(Boolean(this.initialized) && !this.isDestroying)
         {
            App.utils.scheduler.cancelTask(this.processLoad);
            manager = this;
            STRINGS.setLang(this.currentLang);
            this.window.useBottomBtns = true;
            this.btnApply.enabled = this.configChanged;
            this.btnOk.addEventListener(MouseEvent.CLICK,this.handleBtnOkClick);
            this.btnCancel.addEventListener(MouseEvent.CLICK,this.handleWindowClose);
            this.btnApply.addEventListener(MouseEvent.CLICK,this.handleBtnApplyClick);
            this.btnApply.width = this.btnCancel.width = this.btnOk.width = 100;
            this.btnApply.x = 960 - this.btnApply.width - 5;
            this.btnCancel.x = this.btnApply.x - 105;
            this.btnOk.x = this.btnCancel.x - 105;
            this.btnApply.y = this.btnCancel.y = this.btnOk.y = 680;
            this.refreshStrings();
            this.getModsDataS();
            this.sendCallbackS("pageLoaded");
         }
         else
         {
            App.utils.scheduler.scheduleOnNextFrame(this.processLoad);
         }
      }
      
      override protected function onDispose() : void
      {
         App.toolTipMgr.hide();
         App.utils.popupMgr.removeAll();
         this.btnOk.removeEventListener(MouseEvent.CLICK,this.handleBtnOkClick);
         this.btnCancel.removeEventListener(MouseEvent.CLICK,this.handleWindowClose);
         this.btnApply.removeEventListener(MouseEvent.CLICK,this.handleBtnApplyClick);
         this.isDestroying = true;
         super.onDispose();
         this.sendCallbackS(Constants.AS_RETURN_VIEW_DISPOSED);
      }
      
      public function as_setSettings(param1:Object, param2:Boolean = false) : void
      {
         var _loc3_:Object = param1;
         if(!param2)
         {
            this.handleWindowClose();
         }
         if(_loc3_.windowTitle)
         {
            this.window.title = _loc3_.windowTitle;
         }
         if(_loc3_.buttonOK)
         {
            this.btnOk.label = _loc3_.buttonOK;
         }
         if(_loc3_.buttonCancel)
         {
            this.btnCancel.label = _loc3_.buttonCancel;
         }
         if(_loc3_.buttonApply)
         {
            this.btnApply.label = _loc3_.buttonApply;
         }
         if(_loc3_.enableButtonTooltip)
         {
            STRINGS.BUTTON_ENABLED_TOOLTIP = _loc3_.enableButtonTooltip;
         }
      }
      
      public function as_processEvent(param1:String) : void
      {
         if(param1 == Constants.AS_CALL_CLOSE_WINDOW && Boolean(this.initialized) && !this.isDestroying)
         {
            this.isDestroying = true;
            App.utils.scheduler.scheduleTask(this.handleWindowClose,0.3);
         }
      }
      
      public function as_setModsData(param1:Object, param2:Boolean = false, param3:Boolean = false, param4:String = "") : void
      {
         var _loc11_:* = undefined;
         if(!param2)
         {
            return;
         }
         var _loc5_:int = 0;
         this.realm = param4;
         var _loc6_:String = null;
         var _loc7_:vxSettingsApiComponent = null;
         var _loc8_:Object = param1;
         var _loc9_:Array = new Array();
         var _loc10_:int = 9000;
         this.initScrollArea();
         this.modsData = _loc8_;
         _loc5_ = 0;
         for(_loc6_ in this.modsData)
         {
            if(this.modsData[_loc6_].hasOwnProperty("position"))
            {
               if(this.modsData[_loc6_].position == _loc10_)
               {
                  _loc10_ += 1;
               }
               _loc9_.push({
                  "name":_loc6_,
                  "sid":this.modsData[_loc6_].position
               });
               _loc10_ += 1;
            }
            else
            {
               _loc9_.push({
                  "name":_loc6_,
                  "sid":_loc10_
               });
               _loc10_ += 1;
            }
         }
         _loc9_.sortOn("sid",Array.NUMERIC);
         for each(_loc11_ in _loc9_)
         {
            if(!(!this.modsData[_loc11_.name].inBattle && param3))
            {
               _loc7_ = new vxSettingsApiComponent();
               _loc7_.name = _loc11_.name;
               _loc7_.preInvoke(_loc11_.name,param3,param4);
               _loc7_.setData(this.modsData[_loc11_.name]);
               _loc7_.validateNow();
               _loc7_.y = _loc5_;
               _loc5_ = _loc7_.y + _loc7_.height + Constants.MOD_MARGIN_BOTTOM;
               this.modsContainer.addChildAt(_loc7_,0);
               this.modsArray.push(_loc7_);
               if(this.modsArray.length == this.sendCallbackS("getRefCount") && !this.isDestroying)
               {
                  App.utils.scheduler.scheduleOnNextFrame(this.invalidateDCS);
               }
            }
         }
      }
      
      public function invalidateDCS() : void
      {
         var mod:vxSettingsApiComponent = null;
         var component:Object = null;
         var j:int = 0;
         var i:int = 0;
         try
         {
            j = 0;
            while(j < this.modsArray.length)
            {
               mod = this.modsArray[j];
               i = 0;
               while(i < mod.components.length)
               {
                  component = mod.components[i];
                  if(!("type" in component.data && (component.data.type == "Label" || component.data.type == "Empty")))
                  {
                     if("varName" in component.data)
                     {
                        this.onDataChangedS(mod.modLinkage,component.data.varName,component.componentObject[Constants.COMPONENT_RETURN_VALUE_KEY].value);
                     }
                  }
                  i++;
               }
               j++;
            }
         }
         catch(err:Error)
         {
            return;
         }
      }
      
      public function invalidateByLinkage(param1:String) : void
      {
         var mod:vxSettingsApiComponent = null;
         var component:Object = null;
         var j:int = 0;
         var i:int = 0;
         var linkage:String = param1;
         try
         {
            j = 0;
            while(j < this.modsArray.length)
            {
               mod = this.modsArray[j];
               if(mod.modLinkage == linkage)
               {
                  i = 0;
                  while(i < mod.components.length)
                  {
                     component = mod.components[i];
                     if(!("type" in component.data && (component.data.type == "Label" || component.data.type == "Empty")))
                     {
                        if("varName" in component.data)
                        {
                           this.onDataChangedS(mod.modLinkage,component.data.varName,component.componentObject[Constants.COMPONENT_RETURN_VALUE_KEY].value);
                        }
                     }
                     i++;
                  }
               }
               j++;
            }
         }
         catch(err:Error)
         {
            return;
         }
      }
      
      public function as_getDAAPIObject(param1:String, param2:String) : *
      {
         var mod:vxSettingsApiComponent = null;
         var component:Object = null;
         var j:int = 0;
         var i:int = 0;
         var name:String = param1;
         var arg2:String = param2;
         try
         {
            j = 0;
            while(j < this.modsArray.length)
            {
               mod = this.modsArray[j];
               if(mod.modLinkage == name)
               {
                  i = 0;
                  while(i < mod.components.length)
                  {
                     component = mod.components[i];
                     if("varName" in component.data && component.data.varName == arg2)
                     {
                        return MovieClip(component.componentObject);
                     }
                     i++;
                  }
               }
               j++;
            }
         }
         catch(err:Error)
         {
            return new MovieClip();
         }
      }
      
      public function as_updateData(param1:String, param2:Boolean) : void
      {
         var _loc3_:int = 0;
         var _loc4_:vxSettingsApiComponent = null;
         _loc3_ = 0;
         while(_loc3_ < this.modsArray.length)
         {
            _loc4_ = this.modsArray[_loc3_];
            _loc4_.validateNow();
            _loc3_++;
         }
      }
      
      public function as_updateHotKeysCtrl(param1:Object, param2:Boolean) : void
      {
         var mod_iter:Number = 0;
         var component_iter:Number = 0;
         var mod:vxSettingsApiComponent = null;
         var component:Object = null;
         var hotkeys_data:Object = param1;
         var isFirst:Boolean = param2;
         try
         {
            mod_iter = 0;
            while(mod_iter < this.modsArray.length)
            {
               mod = this.modsArray[mod_iter];
               if(mod.modLinkage in hotkeys_data)
               {
                  component_iter = 0;
                  while(component_iter < mod.components.length)
                  {
                     component = mod.components[component_iter];
                     if("varName" in component.data && component.data.varName in hotkeys_data[mod.modLinkage] && (component.data.type == "HotKey" || component.data.type == "KeyInput"))
                     {
                        component.componentObject["control"].updateSettings(isFirst,hotkeys_data[mod.modLinkage][component.data.varName]);
                     }
                     component_iter++;
                  }
               }
               mod_iter++;
            }
            return;
         }
         catch(err:Error)
         {
            return;
         }
      }
      
      private function handleModSettingsChanged(param1:vxSettingsApiComponentEvent) : void
      {
         this.configChanged = true;
         this.btnApply.enabled = true;
         this.btnOk.enabled = true;
         if(this.configChangedLinkages.indexOf(param1.modLinkage) == -1)
         {
            this.configChangedLinkages.push(param1.modLinkage);
         }
      }
      
      private function handleBtnOkClick(param1:MouseEvent) : void
      {
         var _loc2_:Object = null;
         if(this.configChanged)
         {
            _loc2_ = this.collectModsData();
            this.sendDataS(App.utils.JSON.encode(_loc2_));
         }
         this.handleWindowClose();
      }
      
      private function handleBtnApplyClick(param1:MouseEvent) : void
      {
         var _loc2_:Object = this.collectModsData();
         this.sendDataS(App.utils.JSON.encode(_loc2_));
         this.configChanged = false;
         this.btnApply.enabled = this.configChanged;
      }
      
      private function handleBtnCancelClick(param1:MouseEvent) : void
      {
         var _loc2_:Object = this.collectModsData();
         this.sendDataS(App.utils.JSON.encode(_loc2_));
         this.configChanged = false;
         this.btnApply.enabled = this.configChanged;
      }
      
      public function collectModsData() : Object
      {
         var _loc1_:Number = NaN;
         var _loc2_:vxSettingsApiComponent = null;
         var _loc3_:Object = new Object();
         _loc1_ = 0;
         while(_loc1_ < this.modsArray.length)
         {
            _loc2_ = this.modsArray[_loc1_];
            if(this.configChangedLinkages.indexOf(_loc2_.modLinkage) != -1)
            {
               _loc3_[_loc2_.modLinkage] = _loc2_.getConfigData();
            }
            _loc1_++;
         }
         return _loc3_;
      }
      
      private function initScrollArea() : void
      {
         this.scrollPane = new ScrollPane();
         this.modsContainer = new MovieClip();
         this.modsContainer.addEventListener(vxSettingsApiComponentEvent.MOD_SETTINGS_CHANGED,this.handleModSettingsChanged);
         this.scrollBar = App.utils.classFactory.getComponent("ScrollBar",ScrollBar);
         this.scrollBar.y = 7;
         this.scrollBar.x = 940;
         this.scrollBar.height = 663;
         this.scrollPane.scrollStepFactor = 20;
         this.scrollPane.y = 0;
         this.scrollPane.x = 0;
         this.scrollPane.scrollBar = this.scrollBar;
         this.scrollPane.isScrollBarHaveToBeShown = true;
         this.scrollPane.setSize(950,670);
         this.scrollPane.target = this.modsContainer;
         this.addChild(this.scrollPane);
         this.addChild(this.scrollBar);
      }
      
      private function refreshStrings() : void
      {
         this.window.title = STRINGS.WINDOW_TITLE;
         this.btnApply.label = STRINGS.BUTTON_APPLY;
         this.btnOk.label = STRINGS.BUTTON_OK;
         this.btnCancel.label = STRINGS.BUTTON_CANCEL;
      }
   }
}

