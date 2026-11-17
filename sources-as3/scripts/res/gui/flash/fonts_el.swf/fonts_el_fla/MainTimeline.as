package fonts_el_fla
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   
   public dynamic class MainTimeline extends MovieClip
   {
      
      public var t1:TextField;
      
      public var t2:TextField;
      
      public var t3:TextField;
      
      public var t6:TextField;
      
      public function MainTimeline()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      internal function frame1() : *
      {
      }
   }
}

