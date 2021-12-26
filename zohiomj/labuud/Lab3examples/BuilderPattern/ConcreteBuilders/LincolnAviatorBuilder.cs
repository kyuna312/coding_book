using BuilderPattern.Builder;

namespace BuilderPattern.ConcreteBuilders
{
    class LincolnAviatorBuilder : VehicleBuilder
    {
        public override string Name
        {
            get { return "Lincoln"; }
        }

        public override string ModelName
        {
            get { return "Aviator"; }
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
            _vehicle.Model = "Lincoln Aviator";
        }

        public override void SetEngine()
        {
            _vehicle.Engine = "4.6 L DOHC Modular V8";
        }

        public override void SetTransmission()
        {
            _vehicle.Transmission = "5-speed automatic";
        }

        public override void SetBody()
        {
            _vehicle.Body = "SUV";
        }

        public override void SetDoors()
        {
            _vehicle.Doors = 4;
        }
    }
}