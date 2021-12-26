using System;
using BuilderPattern.ConcreteBuilders;
using BuilderPattern.Director;

using System.Windows.Forms;

namespace BuilderPattern
{
    class Program
    {
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
