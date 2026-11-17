package
{
   import flash.display.MovieClip;
   import flash.text.TextField;
   
   [Embed(source="/_assets/assets.swf", symbol="symbol13")]
   public dynamic class InputWindow_mc extends MovieClip
   {
      
      public var inputWindowBackground_mc:MovieClip;
      
      public var readingWindowTextFld:TextField;
      
      public function InputWindow_mc()
      {
         super();
         addFrameScript(0,this.frame1);
      }
      
      internal function frame1() : *
      {
         this.readingWindowTextFld.autoSize = "left";
      }
   }
}

