package net.polarfox.SettingsConstructor.utils
{
   public class ValueProxy
   {
      
      public var target:*;
      
      public var key:*;
      
      public function ValueProxy(param1:* = null, param2:* = null)
      {
         super();
         this.target = param1;
         this.key = param2;
      }
      
      public function get value() : *
      {
         return this.key != null ? this.target[this.key] : this.target;
      }
   }
}

