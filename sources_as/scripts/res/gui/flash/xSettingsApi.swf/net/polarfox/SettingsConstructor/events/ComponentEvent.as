package net.polarfox.SettingsConstructor.events
{
   import flash.events.Event;
   
   public class ComponentEvent extends Event
   {
      
      public static const VALUE_CHANGED:String = "onValueChanged";
      
      public function ComponentEvent(param1:String, param2:Boolean = false, param3:Boolean = false)
      {
         super(param1,param2,param3);
      }
      
      override public function clone() : Event
      {
         return new ComponentEvent(type,bubbles,cancelable);
      }
   }
}

