package
{
   import flash.display.*;
   
   public class FxCandidateListBox
   {
      
      private var ListObj:MovieClip;
      
      private var ItemName:String;
      
      private var SelectedItemIndex:Number;
      
      private var DisplayItems:Array;
      
      private var DisplayItemIndex:Number;
      
      private var Items:Array;
      
      private var ItemDataMap:Array;
      
      private var TextColor:Number;
      
      private var SelectedTextColor:Number;
      
      private var SelectedBackgroundColor:Number;
      
      private var BackgroundColor:Number;
      
      private var IndexBackgroundColor:Number;
      
      private var SelectedIndexBackgroundColor:Number;
      
      private var FontSize:Number;
      
      private var VisibleCount:Number;
      
      private var DisplayCallback:Function;
      
      public function FxCandidateListBox()
      {
         super();
         this.ListObj = null;
         this.ItemName = null;
         this.SelectedItemIndex = -1;
         this.DisplayItems = new Array();
         this.DisplayItemIndex = 0;
         this.Items = new Array();
         this.VisibleCount = 0;
         this.DisplayCallback = null;
      }
      
      public function InitCandidateListDefaults(param1:Object) : void
      {
         this.SelectedBackgroundColor = param1.selectedBackgroundColor == undefined ? 9755539 : Number(param1.selectedBackgroundColor);
         this.IndexBackgroundColor = param1.indexBackgroundColor == undefined ? 12503505 : Number(param1.indexBackgroundColor);
         this.SelectedIndexBackgroundColor = param1.selectedIndexBackgroundColor == undefined ? 6994017 : Number(param1.selectedIndexBackgroundColor);
         this.SelectedTextColor = param1.selectedTextColor == undefined ? 16777215 : Number(param1.selectedTextColor);
         this.TextColor = param1.textColor == undefined ? 0 : Number(param1.textColor);
         this.BackgroundColor = param1.backgroundColor == undefined ? 15725300 : Number(param1.backgroundColor);
         this.FontSize = param1.fontSize == undefined ? 26 : Number(param1.fontSize);
      }
      
      public function SetCandidateListProps(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number) : *
      {
         this.SelectedBackgroundColor = param4 >= 0 ? param4 : this.SelectedBackgroundColor;
         this.SelectedIndexBackgroundColor = param7 >= 0 ? param7 : this.SelectedIndexBackgroundColor;
         this.BackgroundColor = param3 >= 0 ? param3 : this.BackgroundColor;
         this.IndexBackgroundColor = param6 >= 0 ? param6 : this.IndexBackgroundColor;
         this.FontSize = param5 >= 0 ? param5 : this.FontSize;
         this.SelectedTextColor = param2 >= 0 ? param2 : this.SelectedTextColor;
         this.TextColor = param1 >= 0 ? param1 : this.TextColor;
      }
      
      public function CreateCandidateList(param1:MovieClip, param2:Number, param3:String, param4:Number, param5:Number, param6:String, param7:Array, param8:Object) : *
      {
         var _loc10_:MovieClip = null;
         this.InitCandidateListDefaults(param8);
         var _loc9_:* = 0;
         while(_loc9_ < param2)
         {
            _loc10_ = new ListRow(this);
            param1.addChild(_loc10_);
            _loc10_.name = param3 + _loc9_;
            _loc10_.x = param4;
            _loc10_.y = param5;
            _loc10_.ID.autoSize = true;
            _loc10_.Value.autoSize = true;
            param5 += _loc10_.height - 3;
            _loc9_++;
         }
         this.SetListObject(param1);
         this.SetItemDataMap(param7);
         this.SetItemName(param3);
         this.SetVisibleCount(param2);
      }
      
      public function DestroyList() : void
      {
         var _loc1_:* = 0;
         while(_loc1_ < this.VisibleCount)
         {
            this.DisplayItems[_loc1_] = null;
            _loc1_++;
         }
      }
      
      public function ClearList() : void
      {
         this.DisplayItemIndex = 0;
         this.SelectedItemIndex = -1;
      }
      
      public function Add() : void
      {
         if(arguments.length < this.ItemDataMap.length)
         {
            trace("Not enough arguements passed to Add.");
            return;
         }
         if(this.DisplayItemIndex < this.DisplayItems.length)
         {
            this.DisplayItems[this.DisplayItemIndex].ItemData = arguments;
            ++this.DisplayItemIndex;
         }
      }
      
      public function SetVisibleCount(param1:Number) : void
      {
         var _loc3_:* = undefined;
         this.VisibleCount = param1;
         this.DisplayItems.splice(0);
         var _loc2_:* = 0;
         while(_loc2_ < param1)
         {
            _loc3_ = new FxCandidateListItemInterface(MovieClip(this.ListObj.getChildByName(this.ItemName + _loc2_)));
            _loc3_.ItemDataMap = this.ItemDataMap;
            this.DisplayItems.push(_loc3_);
            _loc2_++;
         }
      }
      
      public function GetVisibleCount() : Number
      {
         return this.VisibleCount;
      }
      
      private function GetItemAtIndex(param1:Number) : FxCandidateListItemInterface
      {
         return this.DisplayItems[param1];
      }
      
      public function SetList() : void
      {
         var _loc3_:FxCandidateListItemInterface = null;
         var _loc4_:* = undefined;
         if(this.ListObj == null)
         {
            trace("FxListBoxWidget::SetList - ListObj must be defined.");
            return;
         }
         if(this.ItemName == null)
         {
            trace("FxListBoxWidget::SetList - ItemName is undefined.");
            return;
         }
         var _loc1_:* = this.ItemDataMap.length;
         var _loc2_:Number = 0;
         while(_loc2_ < this.VisibleCount)
         {
            _loc3_ = this.DisplayItems[_loc2_] as FxCandidateListItemInterface;
            _loc4_ = _loc3_.ItemObj;
            if(_loc2_ < this.DisplayItemIndex)
            {
               _loc4_.visible = true;
               if(this.SelectedItemIndex == _loc2_)
               {
                  if(_loc4_ != null)
                  {
                     _loc4_.GotoOnState();
                  }
               }
               else if(_loc4_ != null)
               {
                  _loc4_.GotoOffState();
               }
            }
            if(_loc2_ >= this.DisplayItemIndex)
            {
               _loc4_.visible = false;
            }
            _loc2_++;
         }
         if(this.DisplayCallback != null)
         {
            this.DisplayCallback(this.SelectedItemIndex);
         }
      }
      
      public function SetItemDataMap(param1:Array) : *
      {
         var _loc2_:String = null;
         var _loc3_:* = undefined;
         this.ItemDataMap = param1;
         if(this.ItemDataMap.length > 0)
         {
            _loc2_ = this.ItemDataMap[0];
            _loc3_ = 1;
            while(_loc3_ < this.ItemDataMap.length)
            {
               _loc2_ += "," + this.ItemDataMap[_loc3_];
               _loc3_++;
            }
         }
         MovieClip(this.ListObj.parent).SendIMEMessage("CandidateList_OnSetItemDataMap",_loc2_);
      }
      
      public function DisplayInfo(param1:String) : *
      {
         var _loc2_:FxCandidateListItemInterface = null;
         _loc2_ = this.GetItem(param1);
         if(_loc2_ != null)
         {
            _loc2_.DisplayInfo();
         }
      }
      
      private function GetItem(param1:String) : FxCandidateListItemInterface
      {
         if(this.ItemName == null)
         {
            return null;
         }
         if(param1 == null)
         {
            return null;
         }
         var _loc2_:* = parseInt(param1.substring(this.ItemName.length));
         return this.DisplayItems[_loc2_];
      }
      
      public function SelectItem(param1:String) : *
      {
         this.SelectedItemIndex = parseInt(param1.substring(this.ItemName.length));
         MovieClip(this.ListObj.parent).SendIMEMessage("CandidateList_OnItemSelect",this.SelectedItemIndex);
      }
      
      public function SelectDataItem(param1:Number) : *
      {
         this.SelectedItemIndex = param1;
      }
      
      public function SetListObject(param1:MovieClip) : *
      {
         this.ListObj = param1;
      }
      
      public function SetItemName(param1:String) : *
      {
         this.ItemName = param1;
      }
      
      public function RegisterPostDisplayCallback(param1:Function) : *
      {
         this.DisplayCallback = param1;
      }
   }
}

