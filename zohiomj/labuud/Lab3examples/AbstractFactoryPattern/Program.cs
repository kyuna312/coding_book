using System;
using System.Collections.Generic;
using System.Reflection;
using AbstractFactoryPattern.AbstractFactory;
using System.Windows.Forms;

namespace AbstractFactoryPattern
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
