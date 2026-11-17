package net.polarfox.SettingsConstructor.lang
{
   public class STRINGS
   {
      
      public static var WINDOW_TITLE:String = "WINDOW_TITLE";
      
      public static var BUTTON_APPLY:String = "BUTTON_APPLY";
      
      public static var BUTTON_OK:String = "BUTTON_OK";
      
      public static var BUTTON_CANCEL:String = "BUTTON_CLOSE";
      
      public static var BUTTON_ENABLED_TOOLTIP:String = "BUTTON_ENABLED_TOOLTIP";
      
      public function STRINGS()
      {
         super();
      }
      
      public static function setLang(param1:Object) : void
      {
         WINDOW_TITLE = param1.WINDOW_TITLE;
         BUTTON_APPLY = param1.BUTTON_APPLY;
         BUTTON_OK = param1.BUTTON_OK;
         BUTTON_CANCEL = param1.BUTTON_CANCEL;
         BUTTON_ENABLED_TOOLTIP = param1.BUTTON_ENABLED_TOOLTIP;
      }
   }
}

