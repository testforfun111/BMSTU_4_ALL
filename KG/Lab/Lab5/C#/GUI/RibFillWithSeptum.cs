using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using System.Drawing;
using System.Diagnostics;

namespace GUI
{
    class RibFillWithSeptum : IFilling
    {
        public float FillArea(Bitmap canvas, Color fillColor, Color backgroundColor, List<List<Point>> polygons)
        {
            var sw = new Stopwatch();
            sw.Start();
            int xSeptum = GetXSeptum(polygons);
            foreach (var polygon in polygons)
            {
                for (int i = 0; i < polygon.Count - 1; i++)
                    FillEdge(canvas, polygon[i], polygon[i + 1], xSeptum, fillColor, backgroundColor);
                FillEdge(canvas, polygon[polygon.Count - 1], polygon[0], xSeptum, fillColor, backgroundColor);
            }
            sw.Stop();
            Console.WriteLine($"Time: {sw.ElapsedMilliseconds}");
            return sw.ElapsedMilliseconds;
        }

        public void FillAreaWithDelay(Bitmap canvas,
            Color fillColor, Color backgroundColor,
            List<List<Point>> polygons,
            PictureBox pb, int delay)
        {
            int xSeptum = GetXSeptum(polygons);
            foreach (var polygon in polygons)
            {
                for (int i = 0; i < polygon.Count - 1; i++)
                {
                    FillEdgeWithDelay(canvas, polygon[i], polygon[i + 1], xSeptum, fillColor, backgroundColor, pb, delay);
                    pb.Refresh();
                }
                FillEdgeWithDelay(canvas, polygon[polygon.Count - 1], polygon[0], xSeptum, fillColor, backgroundColor, pb, delay);
                pb.Refresh();
            }
        }

        private void FillEdge(Bitmap canvas, Point A, Point B, int xSeptum,
            Color fillColor, Color backgroundColor)
        {
            if (A.Y == B.Y)
                return;

            if (A.Y > B.Y)
            {
                Point temp = A;
                A = B;
                B = temp;
            }

            float dx = (B.X - A.X) / (float)(B.Y - A.Y);
            float xStart = A.X;
            for (int y = A.Y; y < B.Y; y++)
            {
                // определяем пересечение 
                int xStartInt = (int)Math.Round(xStart);
                for (int x = xStartInt; x < xSeptum; x++)
                    InvertColor(canvas, x, y, fillColor, backgroundColor);

                for (int x = xStartInt; x >= xSeptum; x--)
                    InvertColor(canvas, x, y, fillColor, backgroundColor);
                xStart += dx;
            }
        }

        private bool isExtremumY_B(Point A, Point B, Point C)
        {
            return A.Y < B.Y && C.Y < B.Y || A.Y > B.Y && C.Y > B.Y;
        }

        private void FillEdgeWithDelay(Bitmap canvas,
            Point A, Point B, int xSeptum,
            Color fillColor, Color backgroundColor,
            PictureBox pb, int delay)
        {
            if (A.Y == B.Y)
                return;

            if (A.Y > B.Y)
            {
                Point temp = A;
                A = B;
                B = temp;
            }

            float dx = (B.X - A.X) / (float)(B.Y - A.Y);
            float xStart = A.X;
            for (int y = A.Y; y < B.Y; y++)
            {
                // определяем пересечение  

                for (int x = (int)Math.Round(xStart); x < xSeptum; x++)
                    InvertColor(canvas, x, y, fillColor, backgroundColor);

                for (int x = (int)Math.Round(xStart); x >= xSeptum; x--)
                    InvertColor(canvas, x, y, fillColor, backgroundColor);
                xStart += dx;

                pb.Refresh();
                Thread.Sleep(delay);
            }
        }

        private void InvertColor(Bitmap canvas, int x, int y, Color fillColor, Color backgroundColor)
        {
            Color color = canvas.GetPixel(x, y);
            if (color.ToArgb() == fillColor.ToArgb())
                canvas.SetPixel(x, y, backgroundColor);
            else
                canvas.SetPixel(x, y, fillColor);
        }

        // получить координату X ближайшей к середине вершины
        private int GetXSeptum(List<List<Point>> polygons)
        {
            double x = 0;
            int count = 0;
            foreach (var polygon in polygons)
            {
                foreach (var point in polygon)
                {
                    x += point.X;
                    count++;
                }
            }
            x /= count;
            return (int)Math.Round(x);
        }
    }
}
