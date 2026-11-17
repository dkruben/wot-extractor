package net.polarfox.SettingsConstructor.events
{
   import flash.events.Event;
   
   public class vxSettingsApiComponentEvent extends Event
   {
      
      public static const MOD_SETTINGS_CHANGED:String = "onModSettingsChanged";
      
      public var modLinkage:String = "";
      
      public function vxSettingsApiComponentEvent(param1:String, param2:String, param3:Boolean = false, param4:Boolean = false)
      {
         super(param1,param3,param4);
         this.modLinkage = param2;
      }
      
      override public function clone() : Event
      {
         return new vxSettingsApiComponentEvent(type,this.modLinkage,bubbles,cancelable);
      }
   }
}

