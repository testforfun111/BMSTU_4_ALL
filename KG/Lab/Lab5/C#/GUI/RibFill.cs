using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using System.Drawing;
using System.Diagnostics;
using System.Data;

namespace GUI
{
    class RibFill : IFilling
    {
        public void Find_intersection(List<Point> points, Point A, Point B)
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
                Point temp = new Point((int)Math.Round(xStart), y);
                points.Add(temp);  
                xStart += dx;
            }
        }
        public float FillArea(Bitmap canvas, Color fillColor, Color backgroundColor, List<List<Point>> polygons)
        {
            var sw = new Stopwatch();
            sw.Start();
            int maxX = GetMaxX(polygons);
            foreach (var polygon in polygons)
            {
                List<Point> extremums = new List<Point>();
                for (int i = 0; i < polygon.Count - 2; i++)
                    if (IsExtremumY_B(polygon[i], polygon[i + 1], polygon[i + 2]) == true)
                        extremums.Add(polygon[i + 1]);
                if (IsExtremumY_B(polygon[polygon.Count - 1], polygon[0], polygon[1]) == true)
                    extremums.Add(polygon[0]);

                for (int i = 0; i < polygon.Count - 1; i++)
                    FillEdge(canvas, polygon[i], polygon[i + 1], maxX, extremums, fillColor, backgroundColor);
                FillEdge(canvas, polygon[polygon.Count - 1], polygon[0], maxX, extremums, fillColor, backgroundColor);
            }
            sw.Stop();
            return sw.ElapsedMilliseconds;
        }

        public void FillAreaWithDelay(Bitmap canvas,
            Color fillColor, Color backgroundColor,
            List<List<Point>> polygons,
            PictureBox pb, int delay)
        {
            int maxX = GetMaxX(polygons);
            foreach (var polygon in polygons)
            {
                List<Point> extremums = new List<Point>();
                for (int i = 0; i < polygon.Count - 2; i++)
                    if (IsExtremumY_B(polygon[i], polygon[i + 1], polygon[i + 2]) == true)
                        extremums.Add(polygon[i + 1]);

                if (IsExtremumY_B(polygon[polygon.Count - 1], polygon[0], polygon[1]) == true)
                    extremums.Add(polygon[0]);

                for (int i = 0; i < polygon.Count - 1; i++)
                {
                    FillEdgeWithDelay(canvas, polygon[i], polygon[i + 1], maxX, extremums, fillColor, backgroundColor, pb, delay);
                    pb.Refresh();
                }
                FillEdgeWithDelay(canvas, polygon[polygon.Count - 1], polygon[0], maxX, extremums, fillColor, backgroundColor, pb, delay);
                pb.Refresh();
            }
        }
            
        private void FillEdge(Bitmap canvas, Point A, Point B, int xMax, List<Point> extremums,
            Color fillColor, Color backgroundColor)
        {
            List<Point> intersections = new List<Point>();
            Find_intersection(intersections, A, B);

            foreach (Point dot in intersections)
            {
                for (int x = dot.X+ 1; x < xMax; x++)
                    InvertColor(canvas, x, dot.Y, fillColor, backgroundColor);
            }
            if (extremums.Contains(B))
                InvertColor(canvas, B.X, B.Y, fillColor, backgroundColor);
        }

        private bool IsExtremumY_B(Point A, Point B, Point C)
        {
            return A.Y < B.Y && C.Y < B.Y || A.Y > B.Y && C.Y > B.Y;
        }

        private void FillEdgeWithDelay(Bitmap canvas, 
            Point A, Point B, int xMax, List<Point> extremums,
            Color fillColor, Color backgroundColor,
            PictureBox pb, int delay)
        {
            List<Point> intersections = new List<Point>();
            Find_intersection(intersections, A, B);

            foreach (Point dot in intersections)
            {
                for (int x = dot.X + 1; x < xMax; x++)
                    InvertColor(canvas, x, dot.Y, fillColor, backgroundColor);
                pb.Refresh();
                Thread.Sleep(delay);
            }

            if (extremums.Contains(B))
                InvertColor(canvas, B.X, B.Y, fillColor, backgroundColor);
        }

        private void InvertColor(Bitmap canvas, int x, int y, Color fillColor, Color backgroundColor)
        {
            Color color = canvas.GetPixel(x, y);
            Console.WriteLine(color);
           
            if (color.ToArgb() != Color.Black.ToArgb())
            {
                if (color.ToArgb() == fillColor.ToArgb())
                    canvas.SetPixel(x, y, backgroundColor);
                else
                    canvas.SetPixel(x, y, fillColor);
            }
        }

        private int GetMaxX(List<List<Point>> polygons)
        {
            return polygons.Max(s => s.Max(t => t.X));
        }
    }
}
