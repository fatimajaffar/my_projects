using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EverGreen
{
    class Mainclass
    {
      public static string path = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);

      public static void showWindow(Form openwin,Form closewin, Form MDI)
      {
          closewin.Close();
          openwin.WindowState = FormWindowState.Maximized;
          openwin.MdiParent = MDI;
          openwin.Show();

      }
      public static DialogResult showMsg(string msg, string heading, string type)
      {
          if (msg == "success")
          {
              return MessageBox.Show(msg, heading, MessageBoxButtons.OK, MessageBoxIcon.Information);
          }
          else
          {
              return MessageBox.Show(msg, heading, MessageBoxButtons.OK, MessageBoxIcon.Error);
          }
      }
      public static void disable_reset(Panel p)
      {
          foreach (Control c in p.Controls)
          {
              if (c is TextBox)
              {
                  TextBox t = (TextBox)c;
                  t.Enabled = false;
                  t.Text = "";
              }
              if (c is ComboBox)
              {
                  ComboBox cb = (ComboBox)c;
                  cb.Enabled = false;
                  cb.SelectedIndex = -1;
              }
              if (c is RadioButton)
              {
                  RadioButton rb = (RadioButton)c;
                  rb.Enabled = false;
                  rb.Checked = false;
              }
              if (c is CheckBox)
              {
                  CheckBox ch = (CheckBox)c;
                  ch.Enabled = false;

              }
              if (c is DateTimePicker)
              {
                  DateTimePicker dtp = (DateTimePicker)c;
                  dtp.Enabled = false;
                  dtp.Value = DateTime.Now;

              }
              if (c is Button)
              {
                  Button b = (Button)c;
                  b.Enabled = false;
              }
          }
      }
      public static void disable(Panel p)
      {
          foreach (Control c in p.Controls)
          {
              if (c is TextBox)
              {
                  TextBox t = (TextBox)c;
                  t.Enabled = false;
                  
              }
              if (c is ComboBox)
              {
                  ComboBox cb = (ComboBox)c;
                  cb.Enabled = false;
                  
              }
              if (c is RadioButton)
              {
                  RadioButton rb = (RadioButton)c;
                  rb.Enabled = false;
                 
              }
              if (c is CheckBox)
              {
                  CheckBox ch = (CheckBox)c;
                  ch.Enabled = false;

              }
              if (c is DateTimePicker)
              {
                  DateTimePicker dtp = (DateTimePicker)c;
                  dtp.Enabled = false;
              }
              if (c is Button)
              {
                  Button b = (Button)c;
                  b.Enabled = false;
              }
          }
      }

      public static void enable_reset(GroupBox gb)
      {
          foreach (Control c in gb.Controls)
          {
              if (c is TextBox)
              {
                  TextBox t = (TextBox)c;
                  t.Enabled = true;
                  t.Text = "";
              }
              if (c is ComboBox)
              {
                  ComboBox cb = (ComboBox)c;
                  cb.Enabled = true;
                  cb.SelectedIndex = -1;
              }
              if (c is RadioButton)
              {
                  RadioButton rb = (RadioButton)c;
                  rb.Enabled = true;
                  rb.Checked = false;
              }
              if (c is CheckBox)
              {
                  CheckBox ch = (CheckBox)c;
                  ch.Enabled = true;

              }
              if (c is DateTimePicker)
              {
                  DateTimePicker dtp = (DateTimePicker)c;
                  dtp.Enabled = true;
                  dtp.Value = DateTime.Now;

              }
              if (c is Button)
              {
                  Button b = (Button)c;
                  b.Enabled = true;
              }
          }
      }
      public static void enable_reset(Panel p)
      {
          foreach (Control c in p.Controls)
          {
              if (c is TextBox)
              {
                  TextBox t = (TextBox)c;
                  t.Enabled = true;
                  t.Text = "";
              }
              if (c is ComboBox)
              {
                  ComboBox cb = (ComboBox)c;
                  cb.Enabled = true;
                  cb.SelectedIndex = -1;
              }
              if (c is RadioButton)
              {
                  RadioButton rb = (RadioButton)c;
                  rb.Enabled = true;
                  rb.Checked = false;
              }
              if (c is CheckBox)
              {
                  CheckBox ch = (CheckBox)c;
                  ch.Enabled = true;

              }
              if (c is DateTimePicker)
              {
                  DateTimePicker dtp = (DateTimePicker)c;
                  dtp.Enabled = true;
                  dtp.Value = DateTime.Now;

              }
              if (c is Button)
              {
                  Button b = (Button)c;
                  b.Enabled = true;
              }
          }
      }
      public static void enable(Panel p)
      {
          foreach (Control c in p.Controls)
          {
              if (c is TextBox)
              {
                  TextBox t = (TextBox)c;
                  t.Enabled = true;
                 
              }
              if (c is ComboBox)
              {
                  ComboBox cb = (ComboBox)c;
                  cb.Enabled = true;
                  
              }
              if (c is RadioButton)
              {
                  RadioButton rb = (RadioButton)c;
                  rb.Enabled = true;
                 
              }
              if (c is CheckBox)
              {
                  CheckBox ch = (CheckBox)c;
                  ch.Enabled = true;

              }
              if (c is DateTimePicker)
              {
                  DateTimePicker dtp = (DateTimePicker)c;
                  dtp.Enabled = true;
                  

              }
              if (c is Button)
              {
                  Button b = (Button)c;
                  b.Enabled = true;
              }
          }
      }




    }
}
