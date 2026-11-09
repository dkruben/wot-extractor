package net.polarfox.SettingsConstructor.components
{
   import flash.display.Bitmap;
   import flash.events.MouseEvent;
   import net.polarfox.SettingsConstructor.lang.STRINGS;
   import net.wg.gui.components.controls.SoundButton;
   
   public class ButtonModEnable extends SoundButton
   {
      
      private static var buttonNormalImage:Class = ButtonModEnable_buttonNormalImage;
      
      private static var buttonHoverImage:Class = ButtonModEnable_buttonHoverImage;
      
      private static var buttonPressedImage:Class = ButtonModEnable_buttonPressedImage;
      
      private static var buttonIconOnImage:Class = ButtonModEnable_buttonIconOnImage;
      
      private static var buttonIconOffImage:Class = ButtonModEnable_buttonIconOffImage;
      
      private static var buttonIconInactiveImage:Class = ButtonModEnable_buttonIconInactiveImage;
      
      private var button_normal:Bitmap;
      
      private var button_hover:Bitmap;
      
      private var button_pressed:Bitmap;
      
      private var button_icon_on:Bitmap;
      
      private var button_icon_off:Bitmap;
      
      private var button_icon_inactive:Bitmap;
      
      public var _tolltip:String;
      
      private var _enabled:Boolean = false;
      
      private var _inactive:Boolean = false;
      
      public function ButtonModEnable()
      {
         super();
         this.width = 25;
         this.height = 25;
         this.button_normal = new buttonNormalImage();
         this.addChild(this.button_normal);
         this.button_hover = new buttonHoverImage();
         this.button_hover.visible = false;
         this.addChild(this.button_hover);
         this.button_pressed = new buttonPressedImage();
         this.button_pressed.visible = false;
         this.addChild(this.button_pressed);
         this.button_icon_off = new buttonIconOffImage();
         this.button_icon_off.visible = false;
         this.addChild(this.button_icon_off);
         this.button_icon_inactive = new buttonIconInactiveImage();
         this.button_icon_inactive.visible = false;
         this.addChild(this.button_icon_inactive);
         this.button_icon_on = new buttonIconOnImage();
         this.button_icon_on.visible = false;
         this.addChild(this.button_icon_on);
         this.drawIcon();
         this.addEventListener(MouseEvent.MOUSE_DOWN,this.handleMouseDown);
         this.addEventListener(MouseEvent.MOUSE_UP,this.handleMouseUP);
      }
      
      public function set isEnabled(param1:Boolean) : void
      {
         this._enabled = param1;
         this.drawIcon();
      }
      
      public function get isEnabled() : Boolean
      {
         return this._enabled;
      }
      
      public function set isInactive(param1:Boolean) : void
      {
         this._inactive = param1;
         this.drawIcon();
      }
      
      public function get isInactive() : Boolean
      {
         return this._inactive;
      }
      
      override protected function handleMouseRollOver(param1:MouseEvent) : void
      {
         this.button_hover.visible = true;
         this.button_pressed.visible = false;
         this.drawIcon();
         App.toolTipMgr.showComplex(STRINGS.BUTTON_ENABLED_TOOLTIP);
         super.handleMouseRollOut(param1);
      }
      
      override protected function handleMouseRollOut(param1:MouseEvent) : void
      {
         this.button_hover.visible = false;
         this.button_pressed.visible = false;
         this.drawIcon();
         App.toolTipMgr.hide();
         super.handleMouseRollOut(param1);
      }
      
      private function handleMouseDown(param1:MouseEvent) : void
      {
         this.button_hover.visible = false;
         this.button_pressed.visible = true;
         this.button_icon_on.y = 1;
         this.button_icon_off.y = 1;
      }
      
      private function handleMouseUP(param1:MouseEvent) : void
      {
         this.button_hover.visible = true;
         this.button_pressed.visible = false;
         this.drawIcon();
      }
      
      private function drawIcon() : void
      {
         this.button_icon_on.y = 0;
         this.button_icon_off.y = 0;
         this.button_icon_inactive.y = 0;
         this.button_icon_on.visible = false;
         this.button_icon_off.visible = false;
         this.button_icon_inactive.visible = false;
         if(this.isEnabled && this.isInactive == false)
         {
            this.button_icon_on.visible = true;
         }
         else if(this.isInactive)
         {
            this.button_icon_inactive.visible = true;
         }
         else
         {
            this.button_icon_off.visible = true;
         }
      }
   }
}

