using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AbstractFactoryPattern.AbstractProduct;

namespace AbstractFactoryPattern.ConcreteProducts
{
    public class FordFocus : Vehicle
    {
        public FordFocus(System.Data.SqlClient.SqlDataReader reader)
        {
            Number = reader.GetValue(0).ToString();
            Model = "Ford Focus";
            Engine = "1.0 L EcoBoost I3";
            Transmission = "6-speed PowerShift automatic";
            Body = "5-door hatchback";
            Doors = 5;
        }

        public override string GetInfo()
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
