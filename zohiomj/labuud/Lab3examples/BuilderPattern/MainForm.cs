using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace BuilderPattern
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.treeView1.Nodes.Clear();
            TreeNode root = new TreeNode("Тээврийн хэрэгслүүд", 0, 0);

            List<Director.VehicleCreator> creators = new List<Director.VehicleCreator>(2);
            creators.Add(new Director.VehicleCreator(new ConcreteBuilders.FordExplorerBuilder()));
            creators.Add(new Director.VehicleCreator(new ConcreteBuilders.LincolnAviatorBuilder()));

            for (int i = 0; i < creators.Count; i++)
                root.Nodes.Add(creators[i].Node = new TreeNode(creators[i].Name, i + 1, i + 1));

            SqlConnection connection = new SqlConnection("Data source=.;Initial Catalog=AlessonSE305;Persist Security Info=True;User ID=sa;Password=daimond;");
            SqlCommand command = new SqlCommand();
            command.Connection = connection;
            command.CommandType = CommandType.Text;
            command.CommandText = "SELECT * FROM vehicles";
            connection.Open();
            SqlDataReader reader = command.ExecuteReader();
            TreeNode newNode = null;
            Product.Vehicle newCar = null;
            Director.VehicleCreator creator = null;
            while (reader.Read())
            {
                creator = null;
                newCar = null;
                switch (reader.GetValue(1).ToString())
                {
                    case "Ford":
                        creator = creators[0];                        
                        break;
                    case "Lincoln":
                        creator = creators[1];
                        break;
                }
                if (creator != null)
                {
                    creator.CreateVehicle(reader);
                    newCar = creator.GetVehicle();
                }
                if (newCar != null)
                {
                    newNode = new TreeNode(newCar.Number, creators.Count + 1, creators.Count + 1);
                    newNode.Tag = newCar;
                    creator.Node.Nodes.Add(newNode);
                }
            }
            connection.Close();

            this.treeView1.Nodes.Add(root);
            this.treeView1.ExpandAll();

            //var vehicleCreator = new VehicleCreator(new FordExplorerBuilder());
            //vehicleCreator.CreateVehicle();
            //var vehicle = vehicleCreator.GetVehicle();
            //vehicle.GetInfo();

            //Console.WriteLine("---------------------------------------------");

            //vehicleCreator = new VehicleCreator(new LincolnAviatorBuilder());
            //vehicleCreator.CreateVehicle();
            //vehicle = vehicleCreator.GetVehicle();
            //vehicle.GetInfo();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            if (e.Node.Tag != null)
            {
                Product.Vehicle selectedVehicle = (Product.Vehicle)e.Node.Tag;
                this.textBox1.Text = selectedVehicle.GetInfo();
            }
            else
                this.textBox1.Text = "";
        }
    }
}
