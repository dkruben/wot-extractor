package
{
   public dynamic class NumericStepperEx extends NumericStepper
   {
      
      public function NumericStepperEx()
      {
         super();
      }
      
      override public function get currentValueIsDefault() : Boolean
      {
         return isNaN(value);
      }
   }
}

