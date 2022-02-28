using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EverGreen
{
    public partial class HomeScreen : Sample
    {
        public HomeScreen()
        {
            InitializeComponent();
        }
        

        private void button1_Click(object sender, EventArgs e)
        {
            
            Staff st = new Staff();
            Mainclass.showWindow(st, this, MDI.ActiveForm);
           
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Classes cl = new Classes();
            Mainclass.showWindow(cl, this, MDI.ActiveForm);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Sections sec = new Sections();
            Mainclass.showWindow(sec, this, MDI.ActiveForm);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            Roles rol = new Roles();
            Mainclass.showWindow(rol, this, MDI.ActiveForm);
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }
    }
}
