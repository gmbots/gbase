using System;
using System.Windows;
using csbase.services;

namespace csbase {
    public partial class MainWindow : Window {
        private readonly DamoSoft _damoSoft;

        public MainWindow() {
            InitializeComponent();
            _damoSoft = new DamoSoft();
        }

        private void ButtonBase_OnClick(object sender, RoutedEventArgs e) {
            Console.WriteLine(_damoSoft.Ver());
        }
    }
}