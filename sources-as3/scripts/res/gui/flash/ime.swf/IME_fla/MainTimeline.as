package IME_fla
{
   import adobe.utils.*;
   import fl.motion.*;
   import flash.accessibility.*;
   import flash.desktop.*;
   import flash.display.*;
   import flash.errors.*;
   import flash.events.*;
   import flash.external.*;
   import flash.filters.*;
   import flash.geom.*;
   import flash.globalization.*;
   import flash.media.*;
   import flash.net.*;
   import flash.net.drm.*;
   import flash.printing.*;
   import flash.profiler.*;
   import flash.sampler.*;
   import flash.sensors.*;
   import flash.system.*;
   import flash.text.*;
   import flash.text.engine.*;
   import flash.text.ime.*;
   import flash.ui.*;
   import flash.utils.*;
   import flash.xml.*;
   import scaleform.gfx.*;
   
   public dynamic class MainTimeline extends MovieClip
   {
      
      public var Repositioned:Boolean;
      
      public var candidateList:Object;
      
      public var inputWindow_mc:MovieClip;
      
      public var list_mc:MovieClip;
      
      public var isCandListOpen:Boolean;
      
      public var isListCreated:Boolean;
      
      public var candListHeight:Number;
      
      public var readingWindowTextColor:uint;
      
      public var readingWindowBckgndColor:uint;
      
      public var readingWindowFontSize:uint;
      
      public var inputWindowHeight:uint;
      
      public var candListx:uint;
      
      public var candListy1:uint;
      
      public var candListy2:uint;
      
      public var playerWindowH:*;
      
      public var playerWindowW:*;
      
      public var SendLangBarMessage:*;
      
      public function MainTimeline()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      public function IsCandidateList() : Boolean
      {
         return true;
      }
      
      public function InitReadingWindowDefaults(param1:IMECandidateListStyle) : void
      {
         this.readingWindowTextColor = param1.readingWindowTextColor == 0 ? 0 : uint(param1.readingWindowTextColor);
         this.readingWindowBckgndColor = param1.readingWindowBackgroundColor == 0 ? 15725300 : uint(param1.readingWindowBackgroundColor);
         this.readingWindowFontSize = param1.readingWindowFontSize == 0 ? 20 : uint(param1.readingWindowFontSize);
      }
      
      public function DisplayCallback(param1:Number) : *
      {
         var _loc3_:MovieClip = null;
         var _loc4_:Object = null;
         var _loc5_:Number = NaN;
         var _loc8_:* = undefined;
         var _loc2_:* = 0;
         var _loc6_:* = 0;
         while(_loc6_ < this.candidateList.DisplayItemIndex)
         {
            _loc4_ = this.candidateList.GetItemAtIndex(_loc6_);
            if(_loc4_ != null)
            {
               _loc3_ = _loc4_.ItemObj;
               _loc3_.Value.x = _loc3_.ID.x + _loc3_.ID.width;
               _loc5_ = _loc3_.Value.x + _loc3_.Value.width - _loc3_.bkGround_mc.x + 10;
               if(_loc2_ < _loc5_)
               {
                  _loc2_ = _loc5_;
               }
               _loc8_ = _loc3_.Value;
               if(_loc8_.text == "")
               {
                  _loc3_.ID.alpha = 25;
               }
               else
               {
                  _loc3_.ID.alpha = 100;
               }
            }
            _loc6_++;
         }
         var _loc7_:Number = Number(this.candidateList.GetItemAtIndex(0).ItemObj.y);
         this.candListHeight = 0;
         _loc6_ = 0;
         while(_loc6_ < this.candidateList.DisplayItemIndex)
         {
            _loc4_ = this.candidateList.GetItemAtIndex(_loc6_);
            if(_loc4_ != null)
            {
               _loc3_ = _loc4_.ItemObj;
               _loc3_.bkGround_mc.width = _loc2_;
               _loc3_.bkGround_mc.height = _loc3_.Value.height;
               _loc3_.RowNumberBackground_mc.width = _loc3_.ID.width;
               _loc3_.RowNumberBackground_mc.height = _loc3_.Value.height;
               this.candListHeight += _loc3_.Value.height;
               _loc3_.y = _loc7_;
               _loc3_.Value.y = 0;
               _loc3_.ID.y = 0;
               _loc3_.RowNumberBackground_mc.y = 0;
               _loc3_.bkGround_mc.y = 0;
               _loc7_ += _loc3_.height - 2;
            }
            _loc6_++;
         }
         this.isCandListOpen = true;
      }
      
      public function ChangeFont(param1:Number) : void
      {
         var _loc3_:* = undefined;
         var _loc4_:* = undefined;
         var _loc5_:Object = null;
         var _loc2_:* = 0;
         while(_loc2_ < this.candidateList.DisplayItemIndex)
         {
            _loc3_ = this.candidateList.GetItemAtIndex(_loc2_);
            if(_loc3_ != undefined)
            {
               _loc4_ = _loc3_.ItemObj;
               _loc5_ = new TextFormat();
               _loc5_.size = param1;
               _loc4_.Value.setNewTextFormat(_loc5_);
               _loc4_.ID.setNewTextFormat(_loc5_);
            }
            _loc2_++;
         }
      }
      
      public function SetCandidateListProps(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number, param7:Number) : *
      {
         this.candidateList.SetCandidateListProps(param1,param2,param3,param4,param5,param6,param7);
      }
      
      public function SetReadingWindowProps(param1:Number, param2:Number, param3:Number) : *
      {
         this.readingWindowTextColor = param1 >= 0 ? uint(param1) : this.readingWindowTextColor;
         this.readingWindowBckgndColor = param2 >= 0 ? uint(param2) : uint(param1);
         this.readingWindowFontSize = param3 >= 0 ? uint(param3) : this.readingWindowFontSize;
      }
      
      public function CreateList(param1:Number, param2:Number) : *
      {
         var _loc5_:MovieClip = null;
         this.RemoveList();
         this.isListCreated = true;
         this.Repositioned = false;
         var _loc3_:IMECandidateListStyle = IMEEx.getIMECandidateListStyle();
         this.InitReadingWindowDefaults(_loc3_);
         this.list_mc = new MovieClip();
         this.list_mc.visible = false;
         MovieClip(this).addChild(this.list_mc);
         this.candidateList.CreateCandidateList(this.list_mc,param1,"Character",0,0,"ListRow",new Array("Value"),_loc3_);
         var _loc4_:Number = 0;
         while(_loc4_ < param1)
         {
            _loc5_ = MovieClip(this.list_mc.getChildByName("Character" + _loc4_));
            _loc5_.ID.text = (_loc4_ + param2) % 10;
            _loc5_.Value.autoSize = "left";
            _loc4_++;
         }
         this.list_mc.tabEnabled = false;
         this.list_mc.tabChildren = false;
      }
      
      public function MakeVisible() : *
      {
         this.list_mc.visible = true;
      }
      
      public function MakeInvisible() : *
      {
         if(this.list_mc != null)
         {
            this.list_mc.visible = false;
         }
      }
      
      public function RepositionWindow(param1:Number, param2:Number, param3:Number, param4:Number, param5:Number, param6:Number) : Boolean
      {
         this.list_mc.x = param1;
         if(this.candListHeight < param6 - (param2 + param3))
         {
            this.list_mc.y = param2 + 5 + param3;
            this.MakeVisible();
            return false;
         }
         if(param6 - param2 > param4)
         {
            this.list_mc.y = param2 + 5 + param3;
            this.MakeVisible();
            return false;
         }
         this.list_mc.y = param4 - this.candListHeight - 5;
         this.MakeVisible();
         return true;
      }
      
      public function RepositionInputWindow(param1:Number, param2:Number) : void
      {
         if(this.inputWindow_mc == null)
         {
            return;
         }
         this.inputWindow_mc.x = param1;
         this.inputWindow_mc.y = param2;
      }
      
      public function DisplayInputWindow(param1:String, param2:Number, param3:Number, param4:uint) : void
      {
         var _loc7_:Number = NaN;
         if(param1 == "" && this.inputWindow_mc == null)
         {
            return;
         }
         if(param1 == "" && this.inputWindow_mc != null)
         {
            MovieClip(this).removeChild(this.inputWindow_mc);
            return;
         }
         this.inputWindow_mc = new InputWindow_mc();
         MovieClip(this).addChild(this.inputWindow_mc);
         this.inputWindow_mc.readingWindowTextFld.autoSize = "left";
         this.inputWindow_mc.readingWindowTextFld.text = param1;
         var _loc5_:TextFormat = this.inputWindow_mc.readingWindowTextFld.getTextFormat();
         var _loc6_:IMECandidateListStyle = IMEEx.getIMECandidateListStyle();
         this.InitReadingWindowDefaults(_loc6_);
         if(this.readingWindowTextColor >= 0)
         {
            _loc5_.color = Number(this.readingWindowTextColor);
         }
         if(this.readingWindowFontSize >= 0)
         {
            _loc5_.size = this.readingWindowFontSize;
         }
         if(this.readingWindowBckgndColor >= 0)
         {
            _loc7_ = Number(this.readingWindowBckgndColor);
            this.inputWindow_mc.inputWindowBackground_mc.transform.colorTransform = new ColorTransform(0,0,0,1,(_loc7_ & 0xFF0000) >> 16,(_loc7_ & 0xFF00) >> 8,_loc7_ & 0xFF,0);
         }
         this.inputWindow_mc.readingWindowTextFld.setTextFormat(_loc5_);
         this.inputWindow_mc.inputWindowBackground_mc.width = this.inputWindow_mc.readingWindowTextFld.width;
         this.inputWindow_mc.inputWindowBackground_mc.height = this.inputWindow_mc.readingWindowTextFld.height;
         this.inputWindow_mc.x = param2;
         this.inputWindow_mc.y = param3;
      }
      
      public function RemoveList() : *
      {
         removeEventListener(Event.ENTER_FRAME,this.OnEnterRepositionWindow);
         if(this.list_mc != null)
         {
            this.candidateList.DestroyList();
            MovieClip(this).removeChild(this.list_mc);
            this.isCandListOpen = false;
            this.isListCreated = false;
            this.list_mc = null;
         }
      }
      
      public function RemoveInputWindow() : void
      {
         if(this.inputWindow_mc != null && this.inputWindow_mc != null)
         {
            MovieClip(this).removeChild(this.inputWindow_mc);
            this.inputWindow_mc = null;
         }
      }
      
      public function RepositionCandWindow(param1:Number, param2:Number, param3:Number) : void
      {
         this.candListx = param1;
         this.candListy1 = param2;
         this.candListy2 = param2 - param3;
         if(this.isListCreated)
         {
            addEventListener(Event.ENTER_FRAME,this.OnEnterRepositionWindow);
         }
      }
      
      public function OnEnterRepositionWindow() : void
      {
         var _loc1_:Number = NaN;
         if(this.isCandListOpen)
         {
            removeEventListener(Event.ENTER_FRAME,this.OnEnterRepositionWindow);
            _loc1_ = 0;
            if(this.inputWindow_mc != null)
            {
               this.inputWindowHeight = this.inputWindow_mc.readingWindowTextFld.height;
            }
            else
            {
               this.inputWindowHeight = 0;
            }
            this.playerWindowH = stage.stageHeight;
            this.playerWindowW = stage.stageWidth;
            this.RepositionWindow(this.candListx,this.candListy1,this.inputWindowHeight,this.candListy2,this.playerWindowW,this.playerWindowH);
         }
      }
      
      internal function frame1() : *
      {
         this.Repositioned = false;
         this.candidateList = new FxCandidateListBox();
         this.candidateList.RegisterPostDisplayCallback(this.DisplayCallback);
         this.isCandListOpen = false;
         this.isListCreated = false;
         this.candListHeight = 0;
         this.readingWindowTextColor = 0;
         this.readingWindowBckgndColor = 15725300;
         this.readingWindowFontSize = 20;
         this.inputWindowHeight = 0;
         this.candListx = 0;
         this.candListy1 = 0;
         this.candListy2 = 0;
      }
   }
}

