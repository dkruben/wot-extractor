package net.polarfox.SettingsApi.components.controls
{
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextField;
   import net.polarfox.SettingsConstructor.events.ComponentEvent;
   import net.polarfox.SettingsConstructor.views.vxSettingsAPI;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.interfaces.ISoundButtonEx;
   
   public class KeyInputEx extends SoundButtonEx implements ISoundButtonEx
   {
      
      private static const BUTTON_STATES:Vector.<String> = new <String>["normal","accepting","alert"];
      
      private static const PY_CTX_KEYINPUT_MENU:String = "py_context_menu_settingsapi_keyinput";
      
      public var controlsTF:TextField = null;
      
      public var inputStates:MovieClip = null;
      
      public var keySet:Array = null;
      
      public var is_accepting:Boolean = false;
      
      public var is_setted:Boolean = false;
      
      public var latestData:Object;
      
      public var modLinkage:String;
      
      public var varName:String;
      
      public function KeyInputEx()
      {
         super();
      }
      
      override protected function configUI() : void
      {
         super.configUI();
         preventAutosizing = true;
         focusable = false;
         this.controlsTF.selectable = false;
      }
      
      public function updateSettings(param1:Boolean, param2:Object) : void
      {
         var _loc3_:Boolean = param1;
         var _loc4_:Object = param2;
         this.latestData = _loc4_;
         if(_loc3_)
         {
            this.keySet = _loc4_.value;
            this.is_setted = _loc4_.is_setted;
            this.is_accepting = false;
            this.controlsTF.text = _loc4_.button_text;
         }
         else if(this.is_setted != _loc4_.is_setted || this.keySet != _loc4_.value)
         {
            this.is_setted = _loc4_.is_setted;
            this.keySet = _loc4_.value;
            if(this.modLinkage + this.varName != _loc4_.accepting)
            {
               this.is_accepting = false;
               this.controlsTF.text = _loc4_.button_text;
               this.parent.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
               vxSettingsAPI.manager.onDataChangedS(this.modLinkage,this.varName,this.keySet);
            }
         }
         this.updateControls();
      }
      
      override protected function onMouseDownHandler(param1:MouseEvent) : void
      {
         super.onMouseDownHandler(param1);
         if(App.utils.commons.isLeftButton(param1))
         {
            this.is_accepting = true;
            vxSettingsAPI.manager.handleHotKeysS(this.modLinkage,this.varName,"accept");
         }
         if(App.utils.commons.isRightButton(param1))
         {
            this.is_accepting = false;
            App.contextMenuMgr.show(PY_CTX_KEYINPUT_MENU,this,{
               "linkage":this.modLinkage,
               "varName":this.varName
            });
         }
         this.updateControls();
      }
      
      private function updateControls() : void
      {
         var _loc1_:Boolean = this.is_accepting ? false : !this.is_setted;
         if(this.is_accepting)
         {
            this.inputStates.gotoAndPlay(BUTTON_STATES[1]);
            this.controlsTF.text = "";
         }
         if(_loc1_)
         {
            this.inputStates.gotoAndPlay(BUTTON_STATES[2]);
            this.controlsTF.text = "";
         }
         if(!this.is_accepting && !_loc1_)
         {
            this.inputStates.gotoAndStop(BUTTON_STATES[0]);
            this.controlsTF.text = this.latestData.button_text;
         }
      }
   }
}

