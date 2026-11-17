package net.polarfox.SettingsConstructor.events
{
   import flash.events.Event;
   import net.polarfox.SettingsConstructor.views.vxSettingsAPI;
   
   public class LoggerEvent extends Event
   {
      
      public static const LOG:String = "log";
      
      public var data:Array;
      
      public function LoggerEvent(param1:String, param2:Array, param3:Boolean = true, param4:Boolean = false)
      {
         super(param1,param3,param4);
         this.data = param2;
         vxSettingsAPI.manager.flashLogS(param2);
      }
      
      override public function clone() : Event
      {
         return new LoggerEvent(type,this.data,bubbles,cancelable);
      }
   }
}

