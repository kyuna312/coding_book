using System.Collections.Generic;

namespace AbstractFactoryPattern.AbstractProduct
{
    public abstract class Vehicle
    {
        public string Number { get; set; }
        public string Model { get; set; }
        public string Engine { get; set; }
        public string Transmission { get; set; }
        public string Body { get; set; }
        public int Doors { get; set; }

        public abstract string GetInfo();
    }
}
