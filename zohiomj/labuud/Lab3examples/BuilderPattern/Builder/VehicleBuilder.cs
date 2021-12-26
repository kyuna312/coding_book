using BuilderPattern.Product;

namespace BuilderPattern.Builder
{
    public abstract class VehicleBuilder
    {
        protected Vehicle _vehicle;

        abstract public string Name { get; }
        abstract public string ModelName { get; }
        abstract public System.Windows.Forms.TreeNode Node { get; set; }

        public Vehicle GetVehicle()
        {
            return _vehicle;
        }

        public void VehicleClear()
        {
            _vehicle = null;
        }

        public void CreateVehicle()
        {
            _vehicle = new Vehicle();
        }

        public abstract void SetNumber(string number);
        public abstract void SetModel();
        public abstract void SetEngine();
        public abstract void SetTransmission();
        public abstract void SetBody();
        public abstract void SetDoors();
    }
}
