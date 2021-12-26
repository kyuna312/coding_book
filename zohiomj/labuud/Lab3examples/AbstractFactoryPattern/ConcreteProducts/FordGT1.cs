using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AbstractFactoryPattern.AbstractProduct;

namespace AbstractFactoryPattern.ConcreteProducts
{
    public class FordGT1 : Vehicle
    {
        public FordGT1(System.Data.SqlClient.SqlDataReader reader)
        {
            Number = reader.GetValue(0).ToString();
            Model = "Ford GT1";
            Engine = "5.4 L Supercharged Modular V8";
            Transmission = "6-speed manual";
            Body = "Roadster";
            Doors = 2;
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
