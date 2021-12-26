using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AbstractFactoryPattern.AbstractProduct;

namespace AbstractFactoryPattern.ConcreteProducts
{
    class MitsubishiPajero:Vehicle
    {
        public MitsubishiPajero(System.Data.SqlClient.SqlDataReader reader)
        {
            Number = reader.GetValue(0).ToString();
            Model = "Mitsubishi Pajero Super Exceed";
            Engine = "6G75 3.8 V6";
            Transmission = "5-speed manual";
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
