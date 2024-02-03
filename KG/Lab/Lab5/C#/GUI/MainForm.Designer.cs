namespace GUI
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox = new System.Windows.Forms.PictureBox();
            this.btnFill = new System.Windows.Forms.Button();
            this.btnClear = new System.Windows.Forms.Button();
            this.labelDelay = new System.Windows.Forms.Label();
            this.pictureBoxFillColor = new System.Windows.Forms.PictureBox();
            this.btnChangeFillColor = new System.Windows.Forms.Button();
            this.colorDialogFill = new System.Windows.Forms.ColorDialog();
            this.menuStrip = new System.Windows.Forms.MenuStrip();
            this.numericUpDownDelay = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.textBox2 = new System.Windows.Forms.TextBox();
            this.button1 = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.listBox1 = new System.Windows.Forms.ListBox();
            this.button2 = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxFillColor)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDelay)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox
            // 
            this.pictureBox.BackColor = System.Drawing.Color.White;
            this.pictureBox.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBox.Location = new System.Drawing.Point(87, 84);
            this.pictureBox.Name = "pictureBox";
            this.pictureBox.Size = new System.Drawing.Size(1224, 803);
            this.pictureBox.TabIndex = 0;
            this.pictureBox.TabStop = false;
            this.pictureBox.Click += new System.EventHandler(this.pictureBox_Click);
            this.pictureBox.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pictureBox_MouseMove);
            // 
            // btnFill
            // 
            this.btnFill.Location = new System.Drawing.Point(1450, 781);
            this.btnFill.Name = "btnFill";
            this.btnFill.Size = new System.Drawing.Size(115, 36);
            this.btnFill.TabIndex = 1;
            this.btnFill.Text = "Закрасить";
            this.btnFill.UseVisualStyleBackColor = true;
            this.btnFill.Click += new System.EventHandler(this.btnFill_Click);
            // 
            // btnClear
            // 
            this.btnClear.Location = new System.Drawing.Point(1655, 781);
            this.btnClear.Name = "btnClear";
            this.btnClear.Size = new System.Drawing.Size(111, 36);
            this.btnClear.TabIndex = 2;
            this.btnClear.Text = "Очистить экран";
            this.btnClear.UseVisualStyleBackColor = true;
            this.btnClear.Click += new System.EventHandler(this.btnClear_Click);
            // 
            // labelDelay
            // 
            this.labelDelay.AutoSize = true;
            this.labelDelay.Location = new System.Drawing.Point(1447, 727);
            this.labelDelay.Name = "labelDelay";
            this.labelDelay.Size = new System.Drawing.Size(91, 16);
            this.labelDelay.TabIndex = 4;
            this.labelDelay.Text = "С задержкой";
            this.labelDelay.Click += new System.EventHandler(this.labelDelay_Click);
            // 
            // pictureBoxFillColor
            // 
            this.pictureBoxFillColor.BackColor = System.Drawing.Color.Black;
            this.pictureBoxFillColor.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pictureBoxFillColor.Location = new System.Drawing.Point(1724, 63);
            this.pictureBoxFillColor.Name = "pictureBoxFillColor";
            this.pictureBoxFillColor.Size = new System.Drawing.Size(79, 71);
            this.pictureBoxFillColor.TabIndex = 5;
            this.pictureBoxFillColor.TabStop = false;
            // 
            // btnChangeFillColor
            // 
            this.btnChangeFillColor.Location = new System.Drawing.Point(1489, 84);
            this.btnChangeFillColor.Name = "btnChangeFillColor";
            this.btnChangeFillColor.Size = new System.Drawing.Size(198, 36);
            this.btnChangeFillColor.TabIndex = 6;
            this.btnChangeFillColor.Text = "Цвет заполнения";
            this.btnChangeFillColor.UseVisualStyleBackColor = true;
            this.btnChangeFillColor.Click += new System.EventHandler(this.btnChangeFillColor_Click);
            // 
            // menuStrip
            // 
            this.menuStrip.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.menuStrip.Location = new System.Drawing.Point(0, 0);
            this.menuStrip.Name = "menuStrip";
            this.menuStrip.Size = new System.Drawing.Size(1882, 24);
            this.menuStrip.TabIndex = 8;
            this.menuStrip.Text = "menuStrip1";
            this.menuStrip.ItemClicked += new System.Windows.Forms.ToolStripItemClickedEventHandler(this.menuStrip_ItemClicked);
            // 
            // numericUpDownDelay
            // 
            this.numericUpDownDelay.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.numericUpDownDelay.Location = new System.Drawing.Point(1615, 725);
            this.numericUpDownDelay.Maximum = new decimal(new int[] {
            1000,
            0,
            0,
            0});
            this.numericUpDownDelay.Name = "numericUpDownDelay";
            this.numericUpDownDelay.Size = new System.Drawing.Size(151, 22);
            this.numericUpDownDelay.TabIndex = 9;
            this.numericUpDownDelay.ValueChanged += new System.EventHandler(this.numericUpDownDelay_ValueChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(1486, 192);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(15, 16);
            this.label1.TabIndex = 10;
            this.label1.Text = "X";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(1486, 249);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(16, 16);
            this.label2.TabIndex = 11;
            this.label2.Text = "Y";
            // 
            // textBox1
            // 
            this.textBox1.Location = new System.Drawing.Point(1553, 189);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(100, 22);
            this.textBox1.TabIndex = 12;
            // 
            // textBox2
            // 
            this.textBox2.Location = new System.Drawing.Point(1553, 246);
            this.textBox2.Name = "textBox2";
            this.textBox2.Size = new System.Drawing.Size(100, 22);
            this.textBox2.TabIndex = 13;
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(1705, 209);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(98, 36);
            this.button1.TabIndex = 14;
            this.button1.Text = "Добавить";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(1471, 350);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(105, 16);
            this.label3.TabIndex = 15;
            this.label3.Text = "Таблица точек";
            this.label3.Click += new System.EventHandler(this.label3_Click);
            // 
            // listBox1
            // 
            this.listBox1.FormattingEnabled = true;
            this.listBox1.ItemHeight = 16;
            this.listBox1.Location = new System.Drawing.Point(1475, 384);
            this.listBox1.Name = "listBox1";
            this.listBox1.Size = new System.Drawing.Size(291, 292);
            this.listBox1.TabIndex = 16;
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(1553, 295);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(100, 32);
            this.button2.TabIndex = 17;
            this.button2.Text = "Замкнуть";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1882, 853);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.listBox1);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.textBox2);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.numericUpDownDelay);
            this.Controls.Add(this.btnChangeFillColor);
            this.Controls.Add(this.pictureBoxFillColor);
            this.Controls.Add(this.labelDelay);
            this.Controls.Add(this.btnClear);
            this.Controls.Add(this.btnFill);
            this.Controls.Add(this.pictureBox);
            this.Controls.Add(this.menuStrip);
            this.MainMenuStrip = this.menuStrip;
            this.Name = "MainForm";
            this.Text = "Lab_05";
            this.Load += new System.EventHandler(this.MainForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBoxFillColor)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDownDelay)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox;
        private System.Windows.Forms.Button btnFill;
        private System.Windows.Forms.Button btnClear;
        private System.Windows.Forms.Label labelDelay;
        private System.Windows.Forms.PictureBox pictureBoxFillColor;
        private System.Windows.Forms.Button btnChangeFillColor;
        private System.Windows.Forms.ColorDialog colorDialogFill;
        private System.Windows.Forms.MenuStrip menuStrip;
        private System.Windows.Forms.NumericUpDown numericUpDownDelay;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.TextBox textBox2;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.ListBox listBox1;
        private System.Windows.Forms.Button button2;
    }
}

