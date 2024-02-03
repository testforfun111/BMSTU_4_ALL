using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Drawing;

namespace GUI
{
    interface IFilling
    {
        float FillArea(Bitmap canvas, Color fillColor, Color backgroundColor, List<List<Point>> polygons);

        void FillAreaWithDelay(Bitmap canvas, Color fillColor, Color backgroundColor, List<List<Point>> polygons, PictureBox pb, int delay);
    } 
}
