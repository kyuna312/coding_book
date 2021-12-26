using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AbstractFactoryPattern.AbstractProduct;

namespace AbstractFactoryPattern.ConcreteProducts
{
    class MitsubishiLancerEvoIX:Vehicle
    {
        public MitsubishiLancerEvoIX(System.Data.SqlClient.SqlDataReader reader)
        {
            Number = reader.GetValue(0).ToString();
            Model = "Mitsubishi Lancer Evo IX";
            Engine = "4B10 1.8 L DOHC I4";
            Transmission = "6-speed twin-clutch transmission";
            Body = "4-door sedar";
            Doors = 4;
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
