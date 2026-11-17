package net.polarfox.SettingsConstructor.utils
{
   public class Utils
   {
      
      public static const ERROR_PREFIX:String = "[vxSettingsApi] [ERROR]: ";
      
      public static const DEBUG_PREFIX:String = "[vxSettingsApi] [DEBUG]: ";
      
      public function Utils()
      {
         super();
      }
      
      public static function ErrorLog(param1:String, param2:String) : void
      {
         Logger.Error(param1 + " : " + param2);
      }
      
      public static function DebugLog(... rest) : void
      {
         if(Constants.IS_DEVELOPMENT)
         {
            Logger.Debug(rest.toString());
         }
      }
      
      public static function createTooltip(param1:String) : String
      {
         var _loc2_:XML = new XML(param1);
         return "";
      }
      
      public static function traceObject(param1:Object, param2:String = "") : void
      {
         var _loc3_:* = undefined;
         if(param2 == "")
         {
            param2 = "---";
         }
         else
         {
            param2 += "---";
         }
         for(_loc3_ in param1)
         {
            Utils.DebugLog(param2,_loc3_ + " : " + param1[_loc3_],"  ");
            if(typeof param1[_loc3_] == "object")
            {
               traceObject(param1[_loc3_],param2);
            }
         }
      }
      
      public static function setPrecision(param1:Number, param2:int) : Number
      {
         param2 = Math.pow(10,param2);
         return Math.round(param1 * param2) / param2;
      }
   }
}

