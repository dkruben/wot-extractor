package net.polarfox.SettingsApi.components.controls
{
   import flash.events.*;
   import net.polarfox.SettingsConstructor.events.ComponentEvent;
   import net.polarfox.SettingsConstructor.utils.Constants;
   import net.polarfox.SettingsConstructor.views.vxSettingsAPI;
   import net.wg.gui.components.controls.ButtonIconNormal;
   import net.wg.gui.components.controls.CheckBox;
   import net.wg.gui.components.controls.SoundButtonEx;
   import scaleform.clik.core.UIComponent;
   import scaleform.clik.events.ButtonEvent;
   
   public class CheckBoxEx extends UIComponent
   {
      
      private var cb:CheckBox;
      
      private var linkage:String;
      
      private var componentCFG:Object;
      
      public function CheckBoxEx(param1:Object, param2:String, param3:String, param4:Boolean, param5:String = "")
      {
         var button:*;
         var label:String;
         var selected:Boolean;
         var tooltipText:String;
         var tooltip_icon:String = null;
         super();
         this.name = "CheckboxUI";
         button = undefined;
         this.componentCFG = param1;
         this.linkage = param2;
         label = param3;
         selected = param4;
         tooltipText = param5;
         this.cb = App.utils.classFactory.getComponent("CheckBox",CheckBox);
         this.cb.label = label;
         this.cb.invalidateSize();
         this.cb.invalidateState();
         this.cb.invalidateData();
         this.cb.selected = selected;
         if(param1.hasOwnProperty("tooltip"))
         {
            tooltip_icon = param1.hasOwnProperty("tooltipIcon") ? param1.tooltipIcon : "info";
            this.cb.toolTip = param1.tooltip;
            if(tooltip_icon != "no_icon")
            {
               this.cb.infoIcoType = tooltip_icon;
            }
            this.addEventListener(MouseEvent.ROLL_OVER,function():void
            {
               App.toolTipMgr.showComplex(param1.tooltip);
            });
            this.addEventListener(MouseEvent.ROLL_OUT,function():void
            {
               App.toolTipMgr.hide();
            });
         }
         this.cb.width = 900;
         this.addChild(this.cb);
         this.cb.addEventListener(Event.SELECT,this.handleComponentEvent);
         if(this.componentCFG.hasOwnProperty("button"))
         {
            if(Boolean(this.componentCFG.button.hasOwnProperty("text")) && this.componentCFG.button.text != "")
            {
               button = SoundButtonEx(App.utils.classFactory.getComponent("ButtonNormal",SoundButtonEx));
               button.label = this.componentCFG.button.text;
            }
            if(Boolean(this.componentCFG.button.hasOwnProperty("iconSource")) && this.componentCFG.button.iconSource != "")
            {
               button = ButtonIconNormal(App.utils.classFactory.getComponent("ButtonIconNormalUI",ButtonIconNormal));
               button.iconSource = this.componentCFG.button.hasOwnProperty("iconSource") ? this.componentCFG.button.iconSource : "";
               button.iconOffsetTop = this.componentCFG.button.hasOwnProperty("iconOffsetTop") ? this.componentCFG.button.iconOffsetTop : 0;
               button.iconOffsetLeft = this.componentCFG.button.hasOwnProperty("iconOffsetLeft") ? this.componentCFG.button.iconOffsetLeft : 0;
            }
            button.y = this.cb.y + Constants.MOD_MARGIN_BOTTOM - 3;
            button.x = this.cb.x + this.cb.textField.textWidth + Constants.BUTTON_MARGIN_LEFT + 20;
            if(tooltipText)
            {
               button.x += 25;
            }
            if(this.componentCFG.button.hasOwnProperty("offsetLeft"))
            {
               button.x += this.componentCFG.button.offsetLeft;
            }
            if(this.componentCFG.button.hasOwnProperty("offsetTop"))
            {
               button.y += this.componentCFG.button.offsetTop;
            }
            button.width = this.componentCFG.button.hasOwnProperty("width") ? this.componentCFG.button.width : 30;
            button.height = this.componentCFG.button.hasOwnProperty("height") ? this.componentCFG.button.height : 25;
            button.validateNow();
            button.addEventListener(ButtonEvent.CLICK,function():void
            {
               vxSettingsAPI.manager.callButtonsS(linkage,componentCFG.varName,cb.selected);
            });
            this.addChild(button);
         }
      }
      
      public function get label() : String
      {
         return this.cb.label;
      }
      
      public function set label(param1:String) : void
      {
         this.cb.label = param1;
      }
      
      public function get selected() : Boolean
      {
         return this.cb.selected;
      }
      
      public function set selected(param1:Boolean) : void
      {
         this.cb.selected = param1;
      }
      
      private function handleComponentEvent(param1:Event) : void
      {
         vxSettingsAPI.manager.onDataChangedS(this.linkage,this.componentCFG.varName,this.selected);
         param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
      }
   }
}

