package net.polarfox.SettingsConstructor.utils
{
   import flash.display.DisplayObject;
   import flash.display.MovieClip;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.ColorTransform;
   import net.polarfox.SettingsApi.components.controls.*;
   import net.polarfox.SettingsConstructor.components.ColorPicker;
   import net.polarfox.SettingsConstructor.events.ComponentEvent;
   import net.polarfox.SettingsConstructor.views.vxSettingsAPI;
   import net.wg.gui.components.advanced.DashLineTextItem;
   import net.wg.gui.components.advanced.FieldSet;
   import net.wg.gui.components.advanced.TextAreaSimple;
   import net.wg.gui.components.controls.ButtonIconNormal;
   import net.wg.gui.components.controls.DropdownMenu;
   import net.wg.gui.components.controls.LabelControl;
   import net.wg.gui.components.controls.RadioButton;
   import net.wg.gui.components.controls.RangeSlider;
   import net.wg.gui.components.controls.Slider;
   import net.wg.gui.components.controls.SoundButtonEx;
   import net.wg.gui.components.controls.events.RangeSliderEvent;
   import scaleform.clik.controls.ButtonGroup;
   import scaleform.clik.core.UIComponent;
   import scaleform.clik.data.DataProvider;
   import scaleform.clik.events.ButtonEvent;
   import scaleform.clik.events.IndexEvent;
   import scaleform.clik.events.InputEvent;
   import scaleform.clik.events.ListEvent;
   import scaleform.clik.events.SliderEvent;
   import scaleform.gfx.TextFieldEx;
   
   public class ComponentsHelper extends UIComponent
   {
      
      public function ComponentsHelper()
      {
         super();
      }
      
      public static function handleComponentEvent(param1:Event) : void
      {
         param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
      }
      
      public static function createEmpty(param1:Number, param2:Number) : MovieClip
      {
         var _loc3_:MovieClip = new MovieClip();
         _loc3_.width = param1;
         _loc3_.height = param2;
         return _loc3_;
      }
      
      public static function createTooltipPopover(param1:*, param2:String) : void
      {
         var holder:* = param1;
         var tooltip_text:String = param2;
         holder.addEventListener(MouseEvent.ROLL_OVER,function():void
         {
            App.toolTipMgr.showComplex(tooltip_text);
         });
         holder.addEventListener(MouseEvent.ROLL_OUT,function():void
         {
            App.toolTipMgr.hide();
         });
      }
      
      public static function createDashLineText(param1:Object) : DisplayObject
      {
         var _loc2_:UIComponent = new UIComponent();
         _loc2_.name = "DashLineTextUI";
         var _loc3_:DashLineTextItem = DashLineTextItem(App.utils.classFactory.getComponent("DashLineTextItem_UI",DashLineTextItem));
         _loc3_.name = "DashLineTextItem";
         if(param1.hasOwnProperty("width"))
         {
            _loc3_.width = param1.width;
         }
         else
         {
            _loc3_.width = 425;
         }
         if(param1.hasOwnProperty("useHtml") && Boolean(param1.useHtml))
         {
            TextFieldEx.appendHtml(_loc3_.labelTextField,param1.text);
            if(param1.hasOwnProperty("textValue"))
            {
               TextFieldEx.appendHtml(_loc3_.valueTextField,param1.textValue);
            }
         }
         else
         {
            _loc3_.label = param1.text;
            if(param1.hasOwnProperty("textValue"))
            {
               _loc3_.value = param1.textValue;
            }
         }
         if(param1.hasOwnProperty("tooltip"))
         {
            _loc3_.tooltip = param1.tooltip;
         }
         _loc2_.addChild(_loc3_);
         _loc3_.validateNow();
         var _loc4_:MovieClip = new MovieClip();
         _loc4_.addChild(_loc2_);
         _loc4_[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(_loc3_,"labelTextField");
         _loc4_["dashLabel"] = _loc3_;
         return _loc4_;
      }
      
      public static function createFieldSet(param1:Object, param2:int) : DisplayObject
      {
         var _loc6_:ColorTransform = null;
         var _loc3_:UIComponent = new UIComponent();
         _loc3_.name = "FieldSetUI";
         var _loc4_:FieldSet = FieldSet(App.utils.classFactory.getObject("FieldSet"));
         _loc4_.name = "FieldSet";
         if(param1.hasOwnProperty("width"))
         {
            _loc4_.width = param1.width;
         }
         else
         {
            _loc4_.width = 455;
         }
         _loc4_.height = param2;
         if(param1.hasOwnProperty("useHtml") && Boolean(param1.useHtml))
         {
            TextFieldEx.appendHtml(_loc4_.textField,param1.text);
         }
         else
         {
            _loc4_.label = param1.text;
         }
         if(param1.hasOwnProperty("borderColor"))
         {
            _loc6_ = new ColorTransform();
            _loc6_.color = uint("0x" + param1.borderColor.substr(1));
            _loc4_.line.transform.colorTransform = _loc6_;
            _loc4_.bg.transform.colorTransform = _loc6_;
         }
         if(param1.hasOwnProperty("scale"))
         {
            _loc4_.line.scaleX = _loc4_.line.scaleY = param1.scale;
         }
         _loc3_.addChild(_loc4_);
         _loc4_.validateNow();
         var _loc5_:MovieClip = new MovieClip();
         _loc5_.mouseEnabled = false;
         _loc5_.mouseChildren = false;
         _loc5_.addChild(_loc3_);
         _loc5_[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(_loc4_.textField,"text");
         _loc5_["fieldSet"] = _loc4_;
         _loc5_["fieldHolder"] = _loc3_;
         return _loc5_;
      }
      
      public static function createLabel(param1:String, param2:String = "", param3:String = "info") : DisplayObject
      {
         var _loc4_:UIComponent = new UIComponent();
         _loc4_.name = "LabelUI";
         var _loc5_:LabelControl = LabelControl(App.utils.classFactory.getComponent("LabelControl",LabelControl));
         _loc5_.name = "LabelControl";
         TextFieldEx.setNoTranslate(_loc5_.textField,true);
         _loc5_.width = 900;
         TextFieldEx.appendHtml(_loc5_.textField,param1);
         if(param2)
         {
            _loc5_.toolTip = param2;
            if(param3 != "no_icon")
            {
               _loc5_.infoIcoType = param3;
            }
         }
         _loc4_.addChild(_loc5_);
         _loc5_.validateNow();
         var _loc6_:MovieClip = new MovieClip();
         _loc6_.addChild(_loc4_);
         _loc6_[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(_loc5_,"text");
         _loc6_["label"] = _loc5_;
         return _loc6_;
      }
      
      public static function createRadioButtonGroup(param1:Object, param2:String, param3:String, param4:Array, param5:String = "", param6:String = "", param7:Number = 0) : DisplayObject
      {
         var i:Number;
         var result:MovieClip;
         var buttonGroup:ButtonGroup = null;
         var componentCFG:Object = null;
         var modLinkage:String = null;
         var tooltip_icon:String = null;
         buttonGroup = null;
         var lb:DisplayObject = null;
         var radioButton:RadioButton = null;
         var button:* = undefined;
         var rb:* = undefined;
         componentCFG = param1;
         modLinkage = param2;
         var groupName:String = param3;
         var options:Array = param4;
         var headerText:String = param5;
         var tooltipText:String = param6;
         var selectedIndex:Number = param7;
         var radioButtonsUI:UIComponent = new UIComponent();
         var headerMargin:Number = headerText ? Number(Constants.COMPONENT_HEADER_MARGIN) : Number(0);
         if(headerText)
         {
            tooltip_icon = param1.hasOwnProperty("tooltipIcon") ? param1.tooltipIcon : "info";
            lb = ComponentsHelper.createLabel(headerText,tooltipText,tooltip_icon);
            lb.y = 0;
            lb.x = 0;
            radioButtonsUI.addChild(lb);
            ComponentsHelper.createTooltipPopover(radioButtonsUI,tooltipText);
         }
         buttonGroup = ButtonGroup.getGroup(groupName,radioButtonsUI);
         i = 0;
         while(i < options.length)
         {
            radioButton = RadioButton(App.utils.classFactory.getComponent("RadioButton",RadioButton));
            radioButton.y = i * Constants.RADIO_BUTTONS_MARGIN + headerMargin;
            radioButton.label = options[i].label;
            radioButtonsUI.addChild(radioButton);
            buttonGroup.addButton(radioButton);
            radioButton.addEventListener(MouseEvent.CLICK,handleComponentEvent);
            i++;
         }
         buttonGroup.setSelectedButtonByIndex(selectedIndex);
         if(componentCFG.hasOwnProperty("button"))
         {
            if(Boolean(componentCFG.button.hasOwnProperty("text")) && componentCFG.button.text != "")
            {
               button = SoundButtonEx(App.utils.classFactory.getComponent("ButtonNormal",SoundButtonEx));
               button.label = componentCFG.button.text;
            }
            if(Boolean(componentCFG.button.hasOwnProperty("iconSource")) && componentCFG.button.iconSource != "")
            {
               button = ButtonIconNormal(App.utils.classFactory.getComponent("ButtonIconNormalUI",ButtonIconNormal));
               button.iconSource = componentCFG.button.hasOwnProperty("iconSource") ? componentCFG.button.iconSource : "";
               button.iconOffsetTop = componentCFG.button.hasOwnProperty("iconOffsetTop") ? componentCFG.button.iconOffsetTop : 0;
               button.iconOffsetLeft = componentCFG.button.hasOwnProperty("iconOffsetLeft") ? componentCFG.button.iconOffsetLeft : 0;
            }
            rb = buttonGroup.getButtonAt(0);
            button.y = 0;
            if(headerText)
            {
               button.x = lb.x + lb["label"].textField.textWidth + Constants.BUTTON_MARGIN_LEFT;
               if(tooltipText)
               {
                  button.x += 25;
               }
            }
            else
            {
               button.x = rb.x + rb.width + Constants.BUTTON_MARGIN_LEFT;
            }
            if(componentCFG.button.hasOwnProperty("offsetLeft"))
            {
               button.x += componentCFG.button.offsetLeft;
            }
            if(componentCFG.button.hasOwnProperty("offsetTop"))
            {
               button.y += componentCFG.button.offsetTop;
            }
            button.width = componentCFG.button.hasOwnProperty("width") ? componentCFG.button.width : 30;
            button.height = componentCFG.button.hasOwnProperty("height") ? componentCFG.button.height : 25;
            button.validateNow();
            button.addEventListener(ButtonEvent.CLICK,function():void
            {
               vxSettingsAPI.manager.callButtonsS(modLinkage,componentCFG.varName,buttonGroup.selectedIndex);
            });
            radioButtonsUI.addChild(button);
         }
         result = new MovieClip();
         result.addChild(radioButtonsUI);
         result[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(buttonGroup,"selectedIndex");
         return result;
      }
      
      public static function createDropdown(param1:Object, param2:String, param3:Array, param4:String = "", param5:String = "", param6:Number = 0, param7:Number = 200) : DisplayObject
      {
         var headerMargin:Number;
         var result:MovieClip;
         var componentCFG:Object = null;
         var modLinkage:String = null;
         var dropdown:DropdownMenu = null;
         var tooltip_icon:String = null;
         var lb:DisplayObject = null;
         var button:* = undefined;
         componentCFG = param1;
         modLinkage = param2;
         var options:Array = param3;
         var headerText:String = param4;
         var tooltipText:String = param5;
         var selectedIndex:Number = param6;
         var width:Number = param7;
         var dropdownUI:UIComponent = new UIComponent();
         var inline:Boolean = param1.hasOwnProperty("inline") && Boolean(param1.inline);
         dropdownUI.name = "DropdownUI";
         headerMargin = headerText ? Number(Constants.COMPONENT_HEADER_MARGIN) : Number(0);
         dropdown = DropdownMenu(App.utils.classFactory.getComponent("DropdownMenuUI",DropdownMenu));
         if(headerText)
         {
            tooltip_icon = param1.hasOwnProperty("tooltipIcon") ? param1.tooltipIcon : "info";
            lb = ComponentsHelper.createLabel(headerText,tooltipText,tooltip_icon);
            lb.name = "Label";
            if(inline)
            {
               lb.x = width + Constants.NUMERIC_STEPPER_LABEL_MARGIN;
               lb.y = 2.5;
            }
            else
            {
               lb.y = 0;
               lb.x = 0;
            }
            dropdownUI.addChild(lb);
            ComponentsHelper.createTooltipPopover(dropdownUI,tooltipText);
         }
         dropdown.name = "Dropdown";
         if(inline)
         {
            dropdown.y = 0;
         }
         else
         {
            dropdown.y = headerMargin;
         }
         dropdown.selectedIndex = selectedIndex;
         dropdown.width = width;
         dropdown.dataProvider = new DataProvider(options);
         dropdownUI.addChild(dropdown);
         dropdown.addEventListener(ListEvent.INDEX_CHANGE,function(param1:ListEvent):*
         {
            param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
            vxSettingsAPI.manager.onDataChangedS(modLinkage,componentCFG.varName,dropdown.selectedIndex);
         });
         dropdown["componentInspectorSetting"] = true;
         dropdown.dropdown = "DropdownMenu_ScrollingList";
         dropdown.itemRenderer = App.utils.classFactory.getClass("DropDownListItemRendererSound");
         dropdown.inspectableMenuOffset = {
            "top":-5,
            "right":-6,
            "bottom":0,
            "left":3
         };
         if(options.length > 10)
         {
            dropdown.rowCount = 10;
            dropdown.scrollBar = "ScrollBar";
            dropdown.inspectableThumbOffset = {
               "top":0,
               "bottom":0
            };
         }
         else
         {
            dropdown.rowCount = options.length;
         }
         dropdown["componentInspectorSetting"] = false;
         dropdown.validateNow();
         if(componentCFG.hasOwnProperty("button"))
         {
            if(Boolean(componentCFG.button.hasOwnProperty("text")) && componentCFG.button.text != "")
            {
               button = SoundButtonEx(App.utils.classFactory.getComponent("ButtonNormal",SoundButtonEx));
               button.label = componentCFG.button.text;
            }
            if(Boolean(componentCFG.button.hasOwnProperty("iconSource")) && componentCFG.button.iconSource != "")
            {
               button = ButtonIconNormal(App.utils.classFactory.getComponent("ButtonIconNormalUI",ButtonIconNormal));
               button.iconSource = componentCFG.button.hasOwnProperty("iconSource") ? componentCFG.button.iconSource : "";
               button.iconOffsetTop = componentCFG.button.hasOwnProperty("iconOffsetTop") ? componentCFG.button.iconOffsetTop : 0;
               button.iconOffsetLeft = componentCFG.button.hasOwnProperty("iconOffsetLeft") ? componentCFG.button.iconOffsetLeft : 0;
            }
            button.y = dropdown.y + Constants.MOD_MARGIN_BOTTOM - 3;
            button.x = dropdown.x + dropdown.width + Constants.BUTTON_MARGIN_LEFT - 3;
            if(componentCFG.button.hasOwnProperty("offsetLeft"))
            {
               button.x += componentCFG.button.offsetLeft;
            }
            if(componentCFG.button.hasOwnProperty("offsetTop"))
            {
               button.y += componentCFG.button.offsetTop;
            }
            button.width = componentCFG.button.hasOwnProperty("width") ? componentCFG.button.width : 30;
            button.height = componentCFG.button.hasOwnProperty("height") ? componentCFG.button.height : 25;
            button.name = "Button";
            button.validateNow();
            button.addEventListener(ButtonEvent.CLICK,function():void
            {
               vxSettingsAPI.manager.callButtonsS(modLinkage,componentCFG.varName,dropdown.selectedIndex);
            });
            dropdownUI.addChild(button);
         }
         result = new MovieClip();
         result.addChild(dropdownUI);
         result[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(dropdown,"selectedIndex");
         return result;
      }
      
      public static function createSlider(param1:Object, param2:String, param3:Number, param4:Number, param5:Number, param6:Number, param7:String, param8:String = "", param9:String = "", param10:Number = 200, param11:int = 2) : DisplayObject
      {
         var headerMargin:Number;
         var result:MovieClip;
         var slider:Slider = null;
         var valueLabel:DisplayObject = null;
         var componentCFG:Object = null;
         var modLinkage:String = null;
         var format:String = null;
         var precision:int = param11;
         slider = null;
         var lb:DisplayObject = null;
         var formattedString:String = null;
         valueLabel = null;
         var button:* = undefined;
         componentCFG = param1;
         modLinkage = param2;
         var min:Number = param3;
         var max:Number = param4;
         var interval:Number = param5;
         var value:Number = param6;
         format = param7;
         var headerText:String = param8;
         var tooltipText:String = param9;
         var width:Number = param10;
         var tooltip_icon:String = param1.hasOwnProperty("tooltipIcon") ? param1.tooltipIcon : "info";
         var getFormattedString:Function = function(param1:String, param2:*):String
         {
            return param1.split(Constants.SLIDER_VALUE_KEY).join(param2);
         };
         var sliderUI:UIComponent = new UIComponent();
         sliderUI.name = "SliderUI";
         headerMargin = headerText ? Number(Constants.COMPONENT_HEADER_MARGIN) : Number(0);
         if(headerText)
         {
            lb = ComponentsHelper.createLabel(headerText,tooltipText,tooltip_icon);
            lb.name = "Label";
            lb.y = 0;
            lb.x = 0;
            sliderUI.addChild(lb);
            ComponentsHelper.createTooltipPopover(sliderUI,tooltipText);
         }
         slider = Slider(App.utils.classFactory.getComponent("Slider",Slider));
         slider.name = "Slider";
         slider.y = headerMargin;
         slider.width = width;
         slider.minimum = min;
         slider.maximum = max;
         slider.snapInterval = interval;
         slider.snapping = true;
         slider.liveDragging = true;
         slider.value = value;
         sliderUI.addChild(slider);
         slider.addEventListener(SliderEvent.VALUE_CHANGE,function(param1:SliderEvent):*
         {
            if(format)
            {
               valueLabel["label"].text = getFormattedString(format,Utils.setPrecision(param1.value,precision));
            }
            param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
            vxSettingsAPI.manager.onDataChangedS(modLinkage,componentCFG.varName,param1.value);
         });
         if(format)
         {
            formattedString = getFormattedString(format,slider.value);
            valueLabel = ComponentsHelper.createLabel(formattedString);
            valueLabel.name = "valueLabel";
            valueLabel.y = slider.y + 2;
            valueLabel.x = slider.x + slider.width + Constants.SLIDER_VALUE_MARGIN;
            sliderUI.addChild(valueLabel);
         }
         if(componentCFG.hasOwnProperty("button"))
         {
            if(Boolean(componentCFG.button.hasOwnProperty("text")) && componentCFG.button.text != "")
            {
               button = SoundButtonEx(App.utils.classFactory.getComponent("ButtonNormal",SoundButtonEx));
               button.label = componentCFG.button.text;
            }
            if(Boolean(componentCFG.button.hasOwnProperty("iconSource")) && componentCFG.button.iconSource != "")
            {
               button = ButtonIconNormal(App.utils.classFactory.getComponent("ButtonIconNormalUI",ButtonIconNormal));
               button.iconSource = componentCFG.button.hasOwnProperty("iconSource") ? componentCFG.button.iconSource : "";
               button.iconOffsetTop = componentCFG.button.hasOwnProperty("iconOffsetTop") ? componentCFG.button.iconOffsetTop : 0;
               button.iconOffsetLeft = componentCFG.button.hasOwnProperty("iconOffsetLeft") ? componentCFG.button.iconOffsetLeft : 0;
            }
            button.y = headerMargin;
            button.x = slider.x + slider.width + Constants.SLIDER_VALUE_MARGIN + 15;
            if(format)
            {
               button.x += 15;
            }
            if(componentCFG.button.hasOwnProperty("offsetLeft"))
            {
               button.x += componentCFG.button.offsetLeft;
            }
            if(componentCFG.button.hasOwnProperty("offsetTop"))
            {
               button.y += componentCFG.button.offsetTop;
            }
            button.width = componentCFG.button.hasOwnProperty("width") ? componentCFG.button.width : 30;
            button.height = componentCFG.button.hasOwnProperty("height") ? componentCFG.button.height : 25;
            button.validateNow();
            button.addEventListener(ButtonEvent.CLICK,function():void
            {
               vxSettingsAPI.manager.callButtonsS(modLinkage,componentCFG.varName,slider.value);
            });
            sliderUI.addChild(button);
         }
         result = new MovieClip();
         result.addChild(sliderUI);
         result[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(slider,"value");
         return result;
      }
      
      public static function createButton(param1:Object, param2:String) : DisplayObject
      {
         var result:MovieClip;
         var returnValue:* = undefined;
         var settings:Object = param1;
         var linkage:String = param2;
         var buttonUI:UIComponent = new UIComponent();
         var button:SoundButtonEx = SoundButtonEx(App.utils.classFactory.getComponent("ButtonNormal",SoundButtonEx));
         TextFieldEx.setNoTranslate(button.textField,true);
         button.label = settings.text;
         button.x = settings.hasOwnProperty("x") ? Number(settings.x) : 0;
         button.y = settings.hasOwnProperty("y") ? Number(settings.y) : 0;
         button.focusable = false;
         returnValue = -1;
         if(settings.hasOwnProperty("value"))
         {
            returnValue = settings.value;
         }
         button["returnValue"] = returnValue;
         if(settings.hasOwnProperty("autoSize"))
         {
            button.autoSize = settings.autoSize;
         }
         if(settings.hasOwnProperty("size"))
         {
            button.setActualSize(settings.size[0],settings.size[1]);
         }
         button.addEventListener(ButtonEvent.CLICK,function():void
         {
            vxSettingsAPI.manager.callButtonsS(linkage,settings.varName,returnValue);
         });
         button.validateNow();
         buttonUI.addChild(button);
         result = new MovieClip();
         result.addChild(buttonUI);
         result[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(button,"returnValue");
         return result;
      }
      
      public static function createTextInput(param1:Object, param2:String = "", param3:String = "", param4:String = "", param5:String = "", param6:String = "", param7:Number = 200) : DisplayObject
      {
         var _loc6_:Number;
         var _loc8_:MovieClip;
         var textInput:TextInput = null;
         var tooltip_icon:String = null;
         var params:Object = param1;
         param1 = param2;
         var linkage:String = param3;
         var varName:String = param4;
         param2 = param5;
         param3 = param6;
         param4 = param7;
         var lb:DisplayObject = null;
         var _loc5_:UIComponent = new UIComponent();
         _loc5_.name = "TextInputUI";
         _loc6_ = param1 ? Number(Constants.COMPONENT_HEADER_MARGIN) : Number(0);
         if(param1)
         {
            tooltip_icon = params.hasOwnProperty("tooltipIcon") ? params.tooltipIcon : "info";
            lb = ComponentsHelper.createLabel(param1,param2,tooltip_icon);
            lb.y = 0;
            lb.x = 0;
            lb.name = "Label";
            _loc5_.addChild(lb);
            ComponentsHelper.createTooltipPopover(_loc5_,param2);
         }
         textInput = TextInput(App.utils.classFactory.getComponent("TextInput",TextInput));
         textInput.name = "TextInput";
         TextFieldEx.setNoTranslate(textInput.textField,true);
         textInput.y = _loc6_;
         textInput.width = param4;
         textInput.text = param3;
         textInput.focusable = params.hasOwnProperty("defaultSelection") ? Boolean(params.defaultSelection) : true;
         _loc5_.addChild(textInput);
         textInput.addEventListener(InputEvent.INPUT,function(param1:InputEvent):*
         {
            vxSettingsAPI.manager.onDataChangedS(linkage,varName,textInput.text);
            handleComponentEvent(param1);
         });
         _loc8_ = new MovieClip();
         _loc8_.addChild(_loc5_);
         _loc8_[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(textInput.textField,"text");
         return _loc8_;
      }
      
      public static function createTextInputArea(param1:Object, param2:String = "", param3:String = "", param4:String = "", param5:String = "", param6:String = "", param7:Number = 200) : DisplayObject
      {
         var _loc6_:Number;
         var _loc8_:MovieClip;
         var textArea:TextAreaSimple = null;
         var params:Object = param1;
         param1 = param2;
         var linkage:String = param3;
         var varName:String = param4;
         param2 = param5;
         param3 = param6;
         param4 = param7;
         var lb:DisplayObject = null;
         var _loc5_:UIComponent = new UIComponent();
         _loc5_.name = "TextInputAreaUI";
         _loc6_ = param1 ? Number(Constants.COMPONENT_HEADER_MARGIN) : Number(0);
         if(param1)
         {
            lb = ComponentsHelper.createLabel(param1,param2);
            lb.y = 0;
            lb.x = 0;
            lb.name = "Label";
            _loc5_.addChild(lb);
            ComponentsHelper.createTooltipPopover(_loc5_,param2);
         }
         textArea = TextAreaSimple(App.utils.classFactory.getComponent("TextAreaSimple",TextAreaSimple));
         textArea.name = "TextArea";
         TextFieldEx.setNoTranslate(textArea.textField,true);
         textArea.scrollBar = "ScrollBar";
         textArea.y = _loc6_;
         textArea.width = param4;
         textArea.height = params.hasOwnProperty("height") ? Number(params.height) : 120;
         textArea.text = param3;
         textArea.focusable = params.hasOwnProperty("defaultSelection") ? Boolean(params.defaultSelection) : true;
         textArea.showBgForm = params.hasOwnProperty("showBgForm") ? Boolean(params.showBgForm) : true;
         textArea.bgForm.alpha = 0.63;
         textArea.validateNow();
         _loc5_.addChild(textArea);
         textArea.addEventListener(InputEvent.INPUT,function(param1:InputEvent):*
         {
            param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
            vxSettingsAPI.manager.onDataChangedS(linkage,varName,textArea.text);
         });
         _loc8_ = new MovieClip();
         _loc8_.addChild(_loc5_);
         _loc8_[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(textArea.textField,"text");
         return _loc8_;
      }
      
      public static function createTextInputColor(param1:String = "", param2:String = "", param3:String = "", param4:String = "", param5:String = "", param6:Number = 200) : DisplayObject
      {
         var result:MovieClip;
         var colorPicker:ColorPicker = null;
         var textInput:TextInput = null;
         var linkage:String = param3;
         var varName:String = param4;
         param3 = param5;
         param4 = param6;
         var lb:DisplayObject = null;
         var colorPickerUI:UIComponent = new UIComponent();
         colorPickerUI.name = "ColorPickerUI";
         colorPicker = new ColorPicker();
         colorPicker.name = "ColorPicker";
         textInput = TextInput(App.utils.classFactory.getComponent("TextInput",TextInput));
         textInput.name = "TextInput";
         TextFieldEx.setNoTranslate(textInput.textField,true);
         if(param1)
         {
            lb = ComponentsHelper.createLabel(param1);
            lb.y = 8;
            lb.x = 90;
            lb.name = "Label";
            colorPickerUI.addChild(lb);
         }
         textInput.width = 73;
         textInput.maxChars = 7;
         textInput.x = 0;
         textInput.y = 5;
         textInput.text = param3;
         textInput.textField.restrict = "#0123456789ABCDEFabcdef";
         colorPicker.x = 70;
         colorPicker.y = 7.3;
         colorPicker.colorz = param3;
         colorPicker.buttonMode = true;
         colorPicker.useHandCursor = true;
         colorPickerUI.addChild(textInput);
         colorPickerUI.addChildAt(colorPicker,0);
         colorPickerUI.y = -4;
         textInput.addEventListener(InputEvent.INPUT,function(param1:Event):void
         {
            colorPicker.colorz = param1.target.text;
            param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
            vxSettingsAPI.manager.onDataChangedS(linkage,varName,param1.target.text);
         });
         textInput.addEventListener(MouseEvent.CLICK,function():void
         {
            colorPicker.colorz = textInput.text;
            if(colorPicker.isRendered)
            {
               colorPicker.hidePicker();
            }
            else
            {
               colorPicker.showPicker();
            }
         });
         if(lb)
         {
            lb.addEventListener(MouseEvent.CLICK,function():void
            {
               colorPicker.hidePicker();
            });
         }
         colorPicker.addEventListener(Event.CHANGE,function(param1:Event):void
         {
            textInput.text = param1.target.hexColor;
            param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
            vxSettingsAPI.manager.onDataChangedS(linkage,varName,textInput.text);
         });
         result = new MovieClip();
         result.addChildAt(colorPickerUI,0);
         result[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(textInput,"text");
         return result;
      }
      
      public static function createNumericStepper(param1:Object, param2:String = "") : DisplayObject
      {
         var text_label:String;
         var canManualInput:*;
         var result:MovieClip;
         var label:DisplayObject = null;
         var _numericStepper:NumericStepper = null;
         var tooltip_icon:String = null;
         var settings:Object = param1;
         var linkage:String = param2;
         var numericStepperUI:UIComponent = new UIComponent();
         numericStepperUI.name = "NumericStepperUI";
         text_label = settings.hasOwnProperty("label") ? settings.label : settings.text;
         _numericStepper = NumericStepper(App.utils.classFactory.getComponent("NumericStepperEx",NumericStepper));
         canManualInput = settings.hasOwnProperty("canManualInput") ? settings.canManualInput : false;
         _numericStepper.name = "NumericStepper";
         _numericStepper.stepSize = settings.hasOwnProperty("stepSize") ? Number(settings.stepSize) : 1;
         _numericStepper.minimum = settings.hasOwnProperty("minimum") ? Number(settings.minimum) : 0;
         _numericStepper.maximum = settings.hasOwnProperty("maximum") ? Number(settings.maximum) : 100;
         _numericStepper.canManualInput = canManualInput;
         _numericStepper.value = settings.hasOwnProperty("value") ? Number(settings.value) : 1;
         _numericStepper.focusable = canManualInput;
         if(settings.hasOwnProperty("tooltip") || Boolean(text_label))
         {
            tooltip_icon = settings.hasOwnProperty("tooltipIcon") ? settings.tooltipIcon : "info";
            label = ComponentsHelper.createLabel(text_label,settings.tooltip,tooltip_icon);
            label.y = 2.5;
            label.x = _numericStepper.width + Constants.NUMERIC_STEPPER_LABEL_MARGIN;
            label.name = "Label";
            numericStepperUI.addChild(label);
            ComponentsHelper.createTooltipPopover(numericStepperUI,settings.tooltip);
         }
         _numericStepper.addEventListener(IndexEvent.INDEX_CHANGE,function(param1:IndexEvent):*
         {
            param1.target.dispatchEvent(new ComponentEvent(ComponentEvent.VALUE_CHANGED,true));
            vxSettingsAPI.manager.onDataChangedS(linkage,settings.varName,_numericStepper.value);
         });
         numericStepperUI.addChild(_numericStepper);
         result = new MovieClip();
         result.addChild(numericStepperUI);
         result[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(_numericStepper,"value");
         return result;
      }
      
      public static function createRangeSlider(param1:Object, param2:String) : DisplayObject
      {
         var lb:DisplayObject;
         var tooltip_text:String;
         var tooltip_icon:String;
         var result:MovieClip;
         var valueLabel:DisplayObject = null;
         var rangeSlider:RangeSlider = null;
         var linkage:String = param2;
         valueLabel = null;
         var rangeSliderUI:UIComponent = new UIComponent();
         rangeSliderUI.name = "RangeSliderUI";
         rangeSlider = RangeSlider(App.utils.classFactory.getComponent("RangeSliderUI",RangeSlider));
         rangeSlider.name = "RangeSlider";
         lb = null;
         rangeSliderUI.y += 7;
         lb = ComponentsHelper.createLabel(param1.text,"");
         lb.y = -7;
         lb.x = 0;
         lb.name = "Label";
         rangeSliderUI.addChild(lb);
         rangeSlider.y += 33;
         rangeSlider.x += 5;
         rangeSlider.divisionLabelPostfix = "";
         rangeSlider.divisionLabelStep = param1.divisionLabelStep;
         rangeSlider.divisionStep = param1.divisionStep;
         rangeSlider.focusable = true;
         rangeSlider.snapping = true;
         rangeSlider.liveDragging = param1.hasOwnProperty("liveDragging") ? Boolean(param1.liveDragging) : true;
         rangeSlider.maximum = param1.hasOwnProperty("maximum") ? Number(param1.maximum) : 500;
         rangeSlider.minimum = param1.hasOwnProperty("minimum") ? Number(param1.minimum) : 0;
         rangeSlider.minRangeDistance = param1.minRangeDistance;
         rangeSlider.rangeMode = true;
         rangeSlider.snapInterval = param1.snapInterval;
         rangeSlider.leftValue = param1.value[0];
         rangeSlider.rightValue = param1.value[1];
         rangeSlider["args"] = [rangeSlider.leftValue,rangeSlider.rightValue];
         if(param1.hasOwnProperty("width"))
         {
            rangeSlider.width = param1.width;
         }
         else
         {
            rangeSlider.width = 240;
         }
         tooltip_text = param1.hasOwnProperty("tooltip") ? param1.tooltip : "";
         tooltip_icon = param1.hasOwnProperty("tooltipIcon") ? param1.tooltipIcon : "info";
         valueLabel = ComponentsHelper.createLabel("",tooltip_text,tooltip_icon);
         ComponentsHelper.createTooltipPopover(rangeSliderUI,tooltip_text);
         valueLabel.y = rangeSlider.y + 2;
         valueLabel.x = rangeSlider.x + rangeSlider.width + Constants.SLIDER_VALUE_MARGIN + 5;
         rangeSliderUI.addChild(valueLabel);
         rangeSlider.addEventListener(SliderEvent.VALUE_CHANGE,function(param1:RangeSliderEvent):*
         {
            valueLabel["label"].text = param1.leftValue + " / " + param1.rightValue;
            rangeSlider["args"] = [rangeSlider.leftValue,rangeSlider.rightValue];
            vxSettingsAPI.manager.onDataChangedS(linkage,param1.varName,[rangeSlider.leftValue,rangeSlider.rightValue]);
            handleComponentEvent(param1);
         });
         valueLabel["label"].text = rangeSlider.leftValue + " / " + rangeSlider.rightValue;
         rangeSlider.validateNow();
         rangeSliderUI.addChild(rangeSlider);
         result = new MovieClip();
         result.addChild(rangeSliderUI);
         result[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(rangeSlider,"args");
         return result;
      }
      
      public static function createKeyInput(param1:Object, param2:String, param3:Array, param4:String = "", param5:String = "", param6:String = "") : DisplayObject
      {
         var _loc7_:UIComponent = new UIComponent();
         var _loc8_:String = param1.hasOwnProperty("tooltipIcon") ? param1.tooltipIcon : "info";
         var _loc9_:DisplayObject = ComponentsHelper.createLabel(param1.text,param1.tooltip,_loc8_);
         _loc9_.x = 140;
         _loc9_.y = 3;
         _loc7_.addChild(_loc9_);
         ComponentsHelper.createTooltipPopover(_loc7_,param1.tooltip);
         var _loc10_:KeyInputEx = App.utils.classFactory.getComponent("KeyInputExUI",KeyInputEx);
         _loc10_.modLinkage = param2;
         _loc10_.varName = param1.varName;
         _loc10_.x = -4;
         _loc10_.y = 0;
         _loc9_.x = _loc10_.width;
         _loc7_.addChild(_loc10_);
         var _loc11_:MovieClip = new MovieClip();
         _loc11_.addChild(_loc7_);
         _loc11_[Constants.COMPONENT_RETURN_VALUE_KEY] = new ValueProxy(_loc10_,"keySet");
         _loc11_["control"] = _loc10_;
         return _loc11_;
      }
   }
}

