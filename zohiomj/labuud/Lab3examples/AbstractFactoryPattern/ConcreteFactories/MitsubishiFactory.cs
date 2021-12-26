using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AbstractFactoryPattern.AbstractFactory;
using AbstractFactoryPattern.AbstractProduct;
using AbstractFactoryPattern.ConcreteProducts;

namespace AbstractFactoryPattern.ConcreteFactories
{
    public class MitsubishiFactory:IVehicleFactory
    {
        public string Name
        {
            get { return "Mitsubishi"; }
        }
        private System.Windows.Forms.TreeNode _Node;
        public System.Windows.Forms.TreeNode Node
        {
            get { return _Node; }
            set { _Node = value; }
        }

        public Vehicle CreateCar(System.Data.SqlClient.SqlDataReader reader)
        {
            switch (reader.GetValue(2).ToString())
            {
                case "I": return (new MitsubishiI(reader));
                case "LancerEvoIX": return (new MitsubishiLancerEvoIX(reader));
                case "Pajero": return (new MitsubishiPajero(reader));
            }
            return null;
        }
    }
}
