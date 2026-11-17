package net.polarfox.SettingsConstructor.components
{
   import flash.display.Bitmap;
   import flash.display.BitmapData;
   import flash.display.GradientType;
   import flash.display.InterpolationMethod;
   import flash.display.Shape;
   import flash.display.SpreadMethod;
   import flash.display.Sprite;
   import flash.events.Event;
   import flash.events.MouseEvent;
   import flash.geom.ColorTransform;
   import flash.geom.Matrix;
   import scaleform.clik.core.UIComponent;
   
   public class ColorPicker extends UIComponent
   {
      
      private static var paletteImage:Class = ColorPicker_paletteImage;
      
      private var _currentColor:String = "#000000";
      
      private var palette:Bitmap;
      
      private var spectrShow:Sprite = new Sprite();
      
      private var selectedColor:Sprite = new Sprite();
      
      private var background:Sprite = new Sprite();
      
      private var color:Sprite = new Sprite();
      
      private var paletteVisual:Sprite = new Sprite();
      
      private var paletteView:Sprite = new Sprite();
      
      private var spBg:Sprite = new Sprite();
      
      private var bitmapData:BitmapData = new BitmapData(202,132);
      
      private var colorTransform:ColorTransform = new ColorTransform();
      
      private var _hexColor:* = 0;
      
      private var _returnHexColor:String;
      
      private var _isRendered:Boolean = false;
      
      public function ColorPicker()
      {
         super();
         this.addEventListener(Event.ADDED_TO_STAGE,this.init);
      }
      
      private function init(param1:Event) : void
      {
         removeEventListener(Event.ADDED_TO_STAGE,this.init);
         this.interfaceInit();
      }
      
      private function interfaceInit() : void
      {
         var _loc1_:Shape = new Shape();
         _loc1_.graphics.beginFill(986633);
         _loc1_.graphics.drawRect(0,0,11.25,22.5);
         _loc1_.graphics.beginFill(5526337);
         _loc1_.graphics.drawRect(1,1,10.5,21);
         _loc1_.graphics.endFill();
         var _loc2_:Shape = new Shape();
         _loc2_.graphics.beginFill(0);
         _loc2_.graphics.drawRect(0,0,9,18);
         _loc2_.graphics.endFill();
         this.selectedColor.x = 2;
         this.selectedColor.y = 2;
         this.selectedColor.addChild(_loc2_);
         this.spectrShow.addChild(_loc1_);
         this.spectrShow.addChild(this.selectedColor);
         addChildAt(this.spectrShow,0);
         this.spBg.graphics.beginFill(0,0);
         this.spBg.graphics.drawRect(-1000,-1000,2000,2000);
         this.spBg.width = 0;
         this.spBg.height = 0;
         var _loc3_:Shape = new Shape();
         _loc3_.graphics.beginFill(2039063);
         _loc3_.graphics.drawRect(0,0,219,176);
         _loc3_.graphics.beginFill(2696992);
         _loc3_.graphics.drawRect(1,1,216,173);
         _loc3_.graphics.beginFill(1052940);
         _loc3_.graphics.drawRect(2,2,214,171);
         this.background.addChild(this.spBg);
         this.background.addChild(_loc3_);
         var _loc4_:Shape = new Shape();
         _loc4_.graphics.beginFill(uint(parseInt("0x" + this._currentColor.split("#").join(""),16)));
         _loc4_.graphics.drawRect(0,0,201,20);
         this.color.x = 7;
         this.color.y = 10;
         this.color.addChild(_loc4_);
         var _loc5_:Shape = new Shape();
         var _loc6_:Matrix = new Matrix();
         _loc6_.createGradientBox(202,132,Math.PI / 2,50,0);
         _loc5_.graphics.beginGradientFill(GradientType.LINEAR,[16777215,0],[1,1],[0,255],_loc6_,SpreadMethod.PAD,InterpolationMethod.LINEAR_RGB,0);
         _loc5_.graphics.drawRect(0,0,202,132);
         this.paletteVisual.x = 7;
         this.paletteVisual.y = 35;
         this.palette = new paletteImage() as Bitmap;
         this.palette.y = 2;
         this.palette.width = 198;
         this.palette.height = 130;
         this.paletteVisual.addChild(_loc5_);
         this.paletteVisual.addChild(this.palette);
         this.paletteView.addChild(this.background);
         this.paletteView.addChild(this.color);
         this.paletteView.addChild(this.paletteVisual);
         this.bitmapData.draw(this.paletteVisual);
         this.paletteView.x = this.spectrShow.width - 94;
         this.paletteView.y = 23;
         addChildAt(this.paletteView,0);
         this.paletteView.visible = false;
         this.paletteVisual.addEventListener(MouseEvent.MOUSE_MOVE,this.updateColorPicker);
         this.paletteVisual.addEventListener(MouseEvent.MOUSE_UP,this.setValue);
         this.spectrShow.addEventListener(MouseEvent.CLICK,this.spectrShow_click);
         this.spBg.addEventListener(MouseEvent.CLICK,this.hidePickerHandler);
      }
      
      private function updateColorPicker(param1:MouseEvent) : void
      {
         this._hexColor = "0x" + this.bitmapData.getPixel(this.paletteVisual.mouseX,this.paletteVisual.mouseY).toString(16);
         this.colorTransform.color = this._hexColor;
         this.color.transform.colorTransform = this.colorTransform;
         this._returnHexColor = this.bitmapData.getPixel(this.paletteVisual.mouseX,this.paletteVisual.mouseY).toString(16).toUpperCase();
         this._returnHexColor = "000000" + this._returnHexColor;
         this._returnHexColor = "#" + this._returnHexColor.substr(this._returnHexColor.length - 6);
         this._currentColor = this._returnHexColor;
      }
      
      public function set colorz(param1:String) : void
      {
         this._currentColor = param1;
         this.colorTransform.color = uint(parseInt("0x" + param1.split("#").join(""),16));
         this.color.transform.colorTransform = this.colorTransform;
         this.selectedColor.transform.colorTransform = this.colorTransform;
      }
      
      private function setValue(param1:MouseEvent) : void
      {
         this.selectedColor.transform.colorTransform = this.colorTransform;
         this.paletteView.visible = false;
         this.dispatchEvent(new Event(Event.CHANGE));
      }
      
      private function hidePickerHandler(param1:MouseEvent) : void
      {
         this.hidePicker();
      }
      
      private function spectrShow_click(param1:MouseEvent) : void
      {
         this.showPicker();
      }
      
      public function showPicker() : void
      {
         this._isRendered = true;
         this.colorz = this._currentColor;
         this.spBg.width = 2000;
         this.spBg.height = 2000;
         this.paletteView.visible = true;
      }
      
      public function hidePicker() : void
      {
         this._isRendered = false;
         this.paletteView.visible = false;
         this.spBg.width = 0;
         this.spBg.height = 0;
      }
      
      public function get hexColor() : *
      {
         return this._returnHexColor;
      }
      
      public function get isRendered() : Boolean
      {
         return this._isRendered;
      }
      
      public function set isRendered(param1:Boolean) : void
      {
         this._isRendered = param1;
      }
   }
}

