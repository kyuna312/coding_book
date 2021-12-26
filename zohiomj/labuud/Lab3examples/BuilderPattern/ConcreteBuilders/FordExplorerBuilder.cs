using BuilderPattern.Builder;

namespace BuilderPattern.ConcreteBuilders
{
    class FordExplorerBuilder : VehicleBuilder
    {
        public override string Name
        {
            get { return "Ford"; }
        }

        public override string ModelName
        {
            get { return "Explorer"; }
        }

        private System.Windows.Forms.TreeNode _Node;
        public override System.Windows.Forms.TreeNode Node
        {
            get { return _Node; }
            set { _Node = value; }
        }

        public override void SetNumber(string number)
        {
            _vehicle.Number = number;
        }

        public override void SetModel()
        {
            _vehicle.Model = "Ford Explorer";
        }

        public override void SetEngine()
        {
            _vehicle.Engine = "4.0 L Cologne V6";
        }

        public override void SetTransmission()
        {
            _vehicle.Transmission = "5-speed M5OD-R1 manual";
        }

        public override void SetBody()
        {
            _vehicle.Body = "SUV";
        }

        public override void SetDoors()
        {
            _vehicle.Doors = 5;
        }
    }
}