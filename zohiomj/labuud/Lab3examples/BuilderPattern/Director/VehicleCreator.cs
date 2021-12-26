using BuilderPattern.Builder;
using BuilderPattern.Product;

namespace BuilderPattern.Director
{
    public class VehicleCreator
    {
        private readonly VehicleBuilder _builder;

        public string Name
        {
            get { return _builder.Name; }
        }

        public System.Windows.Forms.TreeNode Node
        {
            get { return _builder.Node; }
            set { _builder.Node = value; }
        }

        public VehicleCreator(VehicleBuilder builder)
        {
            _builder = builder;
        }

        public void CreateVehicle(System.Data.SqlClient.SqlDataReader reader)
        {
            if (reader.GetValue(2).ToString() == _builder.ModelName)
            {
                _builder.CreateVehicle();
                _builder.SetNumber(reader.GetValue(0).ToString());
                _builder.SetModel();
                _builder.SetEngine();
                _builder.SetBody();
                _builder.SetDoors();
                _builder.SetTransmission();
            }
            else _builder.VehicleClear();
        }

        public Vehicle GetVehicle()
        {
            return _builder.GetVehicle();
        }
    }
}
