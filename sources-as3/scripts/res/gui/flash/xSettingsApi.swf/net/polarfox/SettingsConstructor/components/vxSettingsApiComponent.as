package net.polarfox.SettingsConstructor.components
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.events.MouseEvent;
   import flash.text.TextFormat;
   import net.polarfox.SettingsApi.components.controls.*;
   import net.polarfox.SettingsConstructor.events.ComponentEvent;
   import net.polarfox.SettingsConstructor.events.vxSettingsApiComponentEvent;
   import net.polarfox.SettingsConstructor.utils.ComponentsHelper;
   import net.polarfox.SettingsConstructor.utils.Constants;
   import net.polarfox.SettingsConstructor.utils.Utils;
   import net.polarfox.SettingsConstructor.utils.ValueProxy;
   import net.polarfox.SettingsConstructor.views.vxSettingsAPI;
   import net.wg.gui.components.advanced.FieldSet;
   import net.wg.infrastructure.base.UIComponentEx;
   import scaleform.clik.constants.InvalidationType;
   import scaleform.gfx.TextFieldEx;
   
   public class vxSettingsApiComponent extends UIComponentEx
   {
      
      public var modLinkage:String = "";
      
      public var modEnabled:Boolean = true;
      
      public var inBattle:Boolean = false;
      
      public var realm:String = "";
      
      public var numControls:Number = 0;
      
      public var componentsHolder:UIComponentEx;
      
      public var data:Object;
      
      public var components:Array;
      
      private var modEnabledButton:ButtonModEnable = null;
      
      private var __cached__:Boolean = false;
      
      public function vxSettingsApiComponent()
      {
         super();
         this.components = new Array();
         this.componentsHolder = new UIComponentEx();
         this.addChild(this.componentsHolder);
      }
      
      public function preInvoke(param1:String, param2:Boolean = false, param3:String = "") : void
      {
         this.modLinkage = this.name = param1;
         this.inBattle = param2;
         this.realm = param3;
      }
      
      public function setData(param1:Object) : void
      {
         if(param1 != null)
         {
            this.data = param1;
            invalidate(InvalidationType.DATA);
         }
      }
      
      public function getConfigData() : Object
      {
         var i:Number = NaN;
         var component:Object = null;
         var componentValue:* = undefined;
         var result:Object = new Object();
         try
         {
            i = 0;
            while(i < this.components.length)
            {
               component = this.components[i];
               if("varName" in component.data)
               {
                  componentValue = component.componentObject[Constants.COMPONENT_RETURN_VALUE_KEY].value;
                  result[component.data.varName] = component.componentObject[Constants.COMPONENT_RETURN_VALUE_KEY].value;
               }
               i++;
            }
            if(this.data.hasOwnProperty("enabled"))
            {
               result["enabled"] = this.modEnabled;
            }
            return result;
         }
         catch(err:Error)
         {
            Utils.ErrorLog(this.modLinkage + "-->getConfigData()",err.message);
         }
         return result;
      }
      
      override protected function configUI() : void
      {
         super.configUI();
      }
      
      override protected function draw() : void
      {
         if(isInvalid(InvalidationType.DATA))
         {
            this.setup();
         }
      }
      
      private function setup() : void
      {
         var column1:Array = null;
         var column2:Array = null;
         var paddingTop:Number = NaN;
         var lastPos:Number = NaN;
         var fieldSet:FieldSet = null;
         var tf:TextFormat = null;
         var lastPosTemp:Number = NaN;
         try
         {
            if(this.data)
            {
               column1 = this.data.column1;
               column2 = this.data.column2;
               this.numControls = column1.length + column2.length;
               paddingTop = Constants.MOD_PADDING_TOP;
               lastPos = 0;
               if(column1)
               {
                  lastPos = this.createComponents(this.componentsHolder,column1,Constants.MOD_PADDING_LEFT,paddingTop);
               }
               if(column2)
               {
                  lastPosTemp = this.createComponents(this.componentsHolder,column2,Constants.MOD_COMPONENT_WIDTH / 2,paddingTop);
                  if(lastPosTemp > lastPos)
                  {
                     lastPos = lastPosTemp;
                  }
               }
               if(this.data.hasOwnProperty("enabled"))
               {
                  this.modEnabled = this.data.enabled;
                  if(!this.data.hasOwnProperty("showToggleButton") || this.data.hasOwnProperty("showToggleButton") && this.data.showToggleButton == true)
                  {
                     this.modEnabledButton = new ButtonModEnable();
                     this.modEnabledButton.isInactive = this.inBattle;
                     this.modEnabledButton.isEnabled = this.modEnabled;
                     this.modEnabledButton.y = 11;
                     this.modEnabledButton.x = 909;
                     this.modEnabledButton.scaleX = this.modEnabledButton.scaleY = 0.81;
                     this.addChild(this.modEnabledButton);
                     this.modEnabledButton.addEventListener(MouseEvent.CLICK,this.handleButtonEnableClick);
                  }
               }
               fieldSet = FieldSet(App.utils.classFactory.getObject("FieldSet"));
               TextFieldEx.appendHtml(fieldSet.textField,this.data.modDisplayName);
               fieldSet.textField.autoSize = "left";
               fieldSet.width = Constants.MOD_COMPONENT_WIDTH;
               fieldSet.height = lastPos + Constants.MOD_PADDING_BOTTOM;
               fieldSet.textField.y -= 2;
               tf = fieldSet.textField.getTextFormat();
               tf.bold = true;
               tf.size = 15;
               fieldSet.textField.setTextFormat(tf);
               this.addChildAt(fieldSet,0);
               this.height = fieldSet.height;
               this.updateComponentsState();
            }
         }
         catch(err:Error)
         {
            Utils.ErrorLog(this.modLinkage + "setup",err.message);
         }
      }
      
      private function createComponents(param1:UIComponentEx, param2:Array, param3:Number, param4:Number) : Number
      {
         var _loc19_:Object = null;
         var _loc20_:int = 0;
         var _loc21_:int = 0;
         var _loc5_:DisplayObject = null;
         var _loc6_:Number = param4;
         var _loc7_:Vector.<String> = new <String>["Slider","Dropdown","TextInputField"];
         var _loc8_:Vector.<Number> = new <Number>[30,7,9,3,24];
         var _loc9_:int = 0;
         var _loc10_:int = 0;
         var _loc11_:int = 0;
         var _loc12_:int = 0;
         var _loc13_:* = 0;
         var _loc14_:int = 0;
         var _loc15_:Object = null;
         var _loc16_:Boolean = false;
         var _loc17_:Number = 0;
         var _loc18_:Array = new Array();
         while(_loc17_ < param2.length)
         {
            _loc19_ = param2[_loc17_];
            if(!_loc19_.showInBattle && this.inBattle)
            {
               _loc17_++;
            }
            else if(_loc19_.type == "FieldSet")
            {
               _loc9_ = param3 - 12;
               _loc10_ = _loc6_ + Constants.COMPONENT_MARGIN_BOTTOM;
               _loc14_ = _loc13_ = int(_loc19_.itemsCount);
               _loc15_ = new Object();
               _loc15_ = _loc19_;
               _loc6_ = _loc10_ + Constants.COMPONENT_MARGIN_BOTTOM;
               _loc17_++;
               _loc16_ = true;
            }
            else
            {
               _loc5_ = this.getComponentByType(_loc19_);
               _loc5_.addEventListener(ComponentEvent.VALUE_CHANGED,this.handleComponentEvent);
               this.components.push({
                  "componentObject":_loc5_,
                  "data":_loc19_
               });
               if(_loc16_ && _loc13_ >= 0)
               {
                  if(_loc15_.hasOwnProperty("compPadding"))
                  {
                     _loc5_.x = param3 + 9 + _loc15_.compPadding[2];
                  }
                  else
                  {
                     _loc5_.x = param3 + 9;
                  }
                  _loc20_ = _loc14_ == _loc13_ ? 9 : 0;
                  _loc5_.y = _loc6_ + Constants.COMPONENT_MARGIN_BOTTOM + _loc20_;
                  if(_loc19_.type == "RangeSlider")
                  {
                  }
                  if(_loc15_.hasOwnProperty("compMargin"))
                  {
                     _loc6_ = _loc5_.y + _loc5_.height + _loc15_.compMargin[1];
                     _loc12_ += _loc5_.height + Constants.COMPONENT_MARGIN_BOTTOM + _loc15_.compMargin[1];
                  }
                  else
                  {
                     _loc6_ = _loc5_.y + _loc5_.height;
                     _loc12_ += _loc5_.height + Constants.COMPONENT_MARGIN_BOTTOM;
                  }
                  param1.addChildAt(_loc5_,0);
                  _loc13_--;
               }
               else
               {
                  _loc5_.x = param3;
                  _loc5_.y = _loc6_ + Constants.COMPONENT_MARGIN_BOTTOM;
                  _loc6_ = _loc5_.y + _loc5_.height;
                  param1.addChildAt(_loc5_,0);
               }
               if(_loc13_ == 0 && _loc16_)
               {
                  _loc16_ = false;
                  _loc21_ = _loc5_.height;
                  if(_loc19_.type == "RangeSlider")
                  {
                     _loc21_ -= _loc8_[0] + _loc8_[1] + 7;
                  }
                  else if(_loc19_.type == "RadioButtonGroup")
                  {
                     _loc21_ -= _loc8_[4] + _loc8_[0] + _loc8_[3] + 4;
                  }
                  else if(_loc7_.indexOf(_loc19_.type) > -1)
                  {
                     _loc21_ -= _loc8_[4];
                  }
                  _loc5_ = ComponentsHelper.createFieldSet(_loc15_,_loc12_ + _loc21_ + 21);
                  _loc5_.x = _loc9_;
                  _loc5_.y = _loc10_;
                  param1.addChild(_loc5_);
                  _loc6_ += Constants.COMPONENT_MARGIN_BOTTOM + 9;
                  _loc13_ = 0;
                  _loc9_ = 0;
                  _loc10_ = 0;
                  _loc11_ = 0;
                  _loc12_ = 0;
                  _loc14_ = 0;
                  _loc15_ = null;
               }
               _loc17_++;
            }
         }
         return _loc6_;
      }
      
      private function handleComponentEvent(param1:ComponentEvent) : void
      {
         this.dispatchEvent(new vxSettingsApiComponentEvent(vxSettingsApiComponentEvent.MOD_SETTINGS_CHANGED,this.modLinkage,true));
      }
      
      private function _schedule() : void
      {
         vxSettingsAPI.manager.invalidateByLinkage(this.modLinkage);
      }
      
      private function handleButtonEnableClick(param1:MouseEvent) : void
      {
         App.utils.focusHandler.setFocus(this);
         var _loc2_:ButtonModEnable = ButtonModEnable(param1.target);
         _loc2_.isEnabled = !_loc2_.isEnabled;
         this.modEnabled = _loc2_.isEnabled;
         this.handleComponentEvent(null);
         App.utils.scheduler.scheduleTask(this._schedule,1000);
         this.updateComponentsState();
      }
      
      private function updateComponentsState() : void
      {
         this.componentsHolder.alpha = this.modEnabled ? 1 : 0.5;
         this.componentsHolder.mouseEnabled = this.modEnabled;
         this.componentsHolder.mouseChildren = this.modEnabled;
         this.componentsHolder.tabChildren = this.modEnabled;
         if(this.inBattle && this.modEnabledButton != null)
         {
            this.modEnabledButton.enabled = false;
         }
      }
      
      private function getComponentByType(param1:Object) : DisplayObject
      {
         var _loc3_:CheckBoxEx = null;
         var _loc2_:MovieClip = new MovieClip();
         switch(param1.type)
         {
            case "Label":
               return ComponentsHelper.createLabel(param1.text,param1.tooltip);
            case "Empty":
               return ComponentsHelper.createEmpty(450,Constants.EMPTY_COMPONENT_HEIGHT);
            case "CheckBox":
               _loc3_ = new CheckBoxEx(param1,this.modLinkage,param1.text,param1.value,param1.tooltip);
               _loc2_.addChild(_loc3_);
               _loc2_[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(_loc3_,"selected");
               return _loc2_;
            case "HotKey":
               return ComponentsHelper.createKeyInput(param1,this.modLinkage,param1.value,param1.text,param1.tooltip,this.realm);
            case "KeyInput":
               return ComponentsHelper.createKeyInput(param1,this.modLinkage,param1.value,param1.text,param1.tooltip,this.realm);
            case "RadioButtonGroup":
               return ComponentsHelper.createRadioButtonGroup(param1,this.modLinkage,param1.varName,param1.options,param1.text,param1.tooltip,param1.value);
            case "Slider":
               return ComponentsHelper.createSlider(param1,this.modLinkage,param1.minimum,param1.maximum,param1.snapInterval,param1.value,param1.format,param1.text,param1.tooltip);
            case "RangeSlider":
               return ComponentsHelper.createRangeSlider(param1,this.modLinkage);
            case "Button":
               return ComponentsHelper.createButton(param1,this.modLinkage);
            case "Dropdown":
               return ComponentsHelper.createDropdown(param1,this.modLinkage,param1.options,param1.text,param1.tooltip,param1.value,param1.width);
            case "TextInputField":
               return ComponentsHelper.createTextInput(param1,param1.text,this.modLinkage,param1.varName,param1.tooltip,param1.value,param1.width);
            case "TextInputColor":
               return ComponentsHelper.createTextInputColor(param1.text,this.modLinkage,param1.varName,param1.tooltip,param1.value,param1.width);
            case "TextInputArea":
               return ComponentsHelper.createTextInputArea(param1,param1.text,this.modLinkage,param1.varName,param1.tooltip,param1.value,param1.width);
            case "NumericStepper":
               return ComponentsHelper.createNumericStepper(param1,this.modLinkage);
            case "DashLineText":
               return ComponentsHelper.createDashLineText(param1);
            case "FieldSet":
               return ComponentsHelper.createFieldSet(param1,10);
            default:
               return _loc2_;
         }
      }
   }
}

