using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using AbstractFactoryPattern.AbstractFactory;
using AbstractFactoryPattern.AbstractProduct;
using AbstractFactoryPattern.ConcreteProducts;

namespace AbstractFactoryPattern.ConcreteFactories
{
    class FordFactory:IVehicleFactory
    {
        public string Name
        {
            get { return "Ford"; }
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
                case "Explorer": return (new FordExplorer(reader));
                case "Focus": return (new FordFocus(reader));
                case "GT1": return (new FordGT1(reader));
            }
            return null;
        }
    }
}
