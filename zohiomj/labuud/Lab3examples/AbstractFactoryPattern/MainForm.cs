using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace AbstractFactoryPattern
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
            
            List<AbstractFactory.IVehicleFactory> factorys = new List<AbstractFactory.IVehicleFactory>(2);
            factorys.Add(new ConcreteFactories.FordFactory());
            factorys.Add(new ConcreteFactories.MitsubishiFactory());

            for (int i = 0; i < factorys.Count; i++)
                root.Nodes.Add(factorys[i].Node = new TreeNode(factorys[i].Name, i + 1, i + 1));

            SqlConnection connection = new SqlConnection("Data source=.;Initial Catalog=AlessonSE305;Persist Security Info=True;User ID=sa;Password=daimond;");
            SqlCommand command = new SqlCommand();
            command.Connection = connection;
            command.CommandType = CommandType.Text;
            command.CommandText = "SELECT * FROM vehicles";
            connection.Open();
            SqlDataReader reader = command.ExecuteReader();
            TreeNode newNode = null;
            AbstractProduct.Vehicle newCar = null;
            AbstractFactory.IVehicleFactory factory = null;
            while (reader.Read())
            {
                factory = null;
                newCar = null;
                switch (reader.GetValue(1).ToString())
                {
                    case "Ford":
                        factory = factorys[0];                        
                        break;
                    case "Mitsubishi":
                        factory = factorys[1];
                        break;
                }
                if (factory != null) newCar = factory.CreateCar(reader);
                if (newCar != null)
                {                    
                    newNode = new TreeNode(newCar.Number, factorys.Count + 1, factorys.Count + 1);
                    newNode.Tag = newCar;
                    factory.Node.Nodes.Add(newNode);
                }
            }
            connection.Close();

            this.treeView1.Nodes.Add(root);
            this.treeView1.ExpandAll();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            if (e.Node.Tag != null)
            {
                AbstractProduct.Vehicle selectedVehicle = (AbstractProduct.Vehicle)e.Node.Tag;
                this.textBox1.Text = selectedVehicle.GetInfo();
            }
            else
                this.textBox1.Text = "";
        }
    }
}
