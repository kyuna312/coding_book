using AbstractFactoryPattern.AbstractProduct;

namespace AbstractFactoryPattern.AbstractFactory
{
    public interface IVehicleFactory
    {
        string Name { get; }
        System.Windows.Forms.TreeNode Node { get; set; }
        Vehicle CreateCar(System.Data.SqlClient.SqlDataReader reader);
    }
}
