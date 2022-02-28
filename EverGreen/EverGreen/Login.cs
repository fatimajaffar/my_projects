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
    public partial class Login : Sample
    {
        public Login()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void loginbutton_Click(object sender, EventArgs e)
        {
            
            Mainclass main = new Mainclass();
            HomeScreen hs=new HomeScreen();
            Mainclass.showWindow(hs, this, MDI.ActiveForm);
        }
    }
}
