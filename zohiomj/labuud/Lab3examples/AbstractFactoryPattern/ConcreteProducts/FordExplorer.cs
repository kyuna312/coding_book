using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AbstractFactoryPattern.AbstractProduct;

namespace AbstractFactoryPattern.ConcreteProducts
{
    public class FordExplorer:Vehicle
    {
        public FordExplorer(System.Data.SqlClient.SqlDataReader reader)
        {
            Number = reader.GetValue(0).ToString();
            Model = "Ford Explorer";
            Engine = "4.0 L Cologne V6";
            Transmission = "5-speed M50D-R1 manual";
            Body = "SUV";
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
