using System;
using System.Collections.Generic;

namespace BuilderPattern.Product
{
    public class Vehicle
    {
        public string Number { get; set; }
        public string Model { get; set; }
        public string Engine { get; set; }
        public string Transmission { get; set; }
        public string Body { get; set; }
        public int Doors { get; set; }

        public string GetInfo()
        {
            string info = "";
            info += "Улсын дугаар: " + Number + Environment.NewLine;
            info += "Модель: " + Model + Environment.NewLine;
            info += "Хөдөлгүүр: " + Engine + Environment.NewLine;
            info += "Төрөл: " + Body + Environment.NewLine;
            info += "Хаалга: " + Doors + Environment.NewLine;
            info += "Хурдны хайрцаг: " + Transmission + Environment.NewLine;
            return info;
        }
    }

    

}
