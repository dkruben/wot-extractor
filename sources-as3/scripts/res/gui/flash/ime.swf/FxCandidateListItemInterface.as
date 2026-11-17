package
{
   import flash.display.*;
   
   public class FxCandidateListItemInterface
   {
      
      public var ItemObj:Object;
      
      public var ItemDataMap:Array;
      
      public var ItemData:Array;
      
      public function FxCandidateListItemInterface(param1:MovieClip)
      {
         super();
         this.ItemObj = param1;
      }
      
      public function GetData(param1:String) : *
      {
         var _loc2_:* = 0;
         while(_loc2_ < this.ItemDataMap.length)
         {
            if(this.ItemDataMap[_loc2_] == param1)
            {
               return this.ItemData[_loc2_];
            }
            _loc2_++;
         }
      }
      
      public function DisplayInfo() : *
      {
         var _loc2_:* = undefined;
         var _loc1_:* = 0;
         while(_loc1_ < this.ItemDataMap.length)
         {
            _loc2_ = this.ItemObj[this.ItemDataMap[_loc1_]];
            if(_loc2_ != null && _loc2_ != undefined && this.ItemData != null)
            {
               _loc2_.replaceText(0,_loc2_.length,this.ItemData[_loc1_]);
            }
            _loc1_++;
         }
      }
   }
}

