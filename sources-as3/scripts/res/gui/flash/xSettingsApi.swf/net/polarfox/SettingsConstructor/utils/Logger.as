package net.polarfox.SettingsConstructor.utils
{
   import flash.events.EventDispatcher;
   import net.polarfox.SettingsConstructor.events.LoggerEvent;
   
   public class Logger
   {
      
      public static const globalDispatcher:EventDispatcher = new EventDispatcher();
      
      public function Logger()
      {
         super();
      }
      
      public static function Error(... rest) : void
      {
         rest.unshift("ERROR");
         __doLog.apply(null,rest);
      }
      
      public static function Debug(... rest) : void
      {
         rest.unshift("DEBUG");
         __doLog.apply(null,rest);
      }
      
      private static function __doLog() : void
      {
         var _loc2_:Array = [];
         while(arguments.length)
         {
            _loc2_.push(String(arguments.shift()));
         }
         globalDispatcher.dispatchEvent(new LoggerEvent(LoggerEvent.LOG,_loc2_));
      }
   }
}

