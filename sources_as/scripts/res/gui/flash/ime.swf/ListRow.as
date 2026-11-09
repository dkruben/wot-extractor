package
{
   import flash.display.*;
   import flash.events.MouseEvent;
   import flash.geom.*;
   import flash.text.*;
   
   [Embed(source="/_assets/assets.swf", symbol="symbol9")]
   public class ListRow extends MovieClip
   {
      
      public var bkGround_mc:MovieClip;
      
      public var RowNumberBackground_mc:MovieClip;
      
      public var currentState:String = "UnSelected";
      
      public var Value:TextField;
      
      public var ID:TextField;
      
      public var controller:Object;
      
      public function ListRow(param1:Object)
      {
         super();
         addFrameScript(0,this.frame1);
         this.controller = param1;
         addEventListener(MouseEvent.MOUSE_DOWN,this.pressHandler);
         addEventListener(MouseEvent.MOUSE_UP,this.releaseHandler);
      }
      
      internal function pressHandler(param1:MouseEvent) : *
      {
         MovieClip(parent).ClickedOnCandidateList = true;
         this.controller.SelectItem(this.name);
      }
      
      internal function releaseHandler(param1:MouseEvent) : *
      {
      }
      
      public function GotoOffState() : *
      {
         var _loc1_:MovieClip = null;
         var _loc2_:TextFormat = null;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         if(this.bkGround_mc != null)
         {
            this.controller.DisplayInfo(name);
            _loc1_ = MovieClip(parent.parent);
            _loc2_ = this.Value.getTextFormat();
            _loc2_.color = Number(_loc1_.candidateList.TextColor);
            _loc2_.size = _loc1_.candidateList.FontSize;
            _loc3_ = uint(_loc1_.candidateList.BackgroundColor);
            this.bkGround_mc.transform.colorTransform = new ColorTransform(0,0,0,1,(_loc3_ & 0xFF0000) >> 16,(_loc3_ & 0xFF00) >> 8,_loc3_ & 0xFF,0);
            _loc4_ = uint(_loc1_.candidateList.IndexBackgroundColor);
            this.RowNumberBackground_mc.transform.colorTransform = new ColorTransform(0,0,0,1,(_loc4_ & 0xFF0000) >> 16,(_loc4_ & 0xFF00) >> 8,_loc4_ & 0xFF,0);
            this.Value.setTextFormat(_loc2_);
            this.ID.setTextFormat(_loc2_);
         }
         this.currentState = "UnSelected";
      }
      
      public function GotoOnState() : *
      {
         var _loc1_:TextFormat = null;
         var _loc2_:MovieClip = null;
         var _loc3_:uint = 0;
         var _loc4_:uint = 0;
         if(this.bkGround_mc != null)
         {
            this.controller.DisplayInfo(name);
            _loc1_ = this.Value.getTextFormat();
            _loc2_ = MovieClip(parent.parent);
            _loc1_.color = Number(_loc2_.candidateList.SelectedTextColor);
            _loc1_.size = _loc2_.candidateList.FontSize;
            _loc3_ = uint(_loc2_.candidateList.SelectedBackgroundColor);
            this.bkGround_mc.transform.colorTransform = new ColorTransform(0,0,0,1,(_loc3_ & 0xFF0000) >> 16,(_loc3_ & 0xFF00) >> 8,_loc3_ & 0xFF,0);
            _loc4_ = uint(_loc2_.candidateList.SelectedIndexBackgroundColor);
            this.RowNumberBackground_mc.transform.colorTransform = new ColorTransform(0,0,0,1,(_loc4_ & 0xFF0000) >> 16,(_loc4_ & 0xFF00) >> 8,_loc4_ & 0xFF,0);
            this.Value.setTextFormat(_loc1_);
            this.ID.setTextFormat(_loc1_);
         }
         this.currentState = "Selected";
      }
      
      internal function frame1() : *
      {
      }
   }
}

