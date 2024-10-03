import sys
import serial
from serial.tools import list_ports


import pandas as pd
import geopandas as gpd
from shapely import Point

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog
from PyQt5.QtCore import QTimer

from gui import Ui_MainWindow
from saving import Ui_Dialog
from ensure import Ui_Ensure

class MyArduino():

    """
    class that design Arduino process.
    """

    def __init__(self):
        
        # serial object initialization
        self.serial = serial.Serial()
        self.serial.baudrate = 115200
        self.serial.timeout = 3

        # data
        self.data = [["lat", "long"]]

        # flags 
        self.is_connected = False # True if the arduino device is connected
        self.is_ready = False # True if arduino is returning lat and long
        self.recording = False # True if recording: self.data is filling
        self.spin = False # To show recording on UI.
    
    def setup(self):

        """ Initialize return True if everything well."""

        if self.serial.is_open:
            return True
        
        done = self.set_port_and_open()

        self.is_connected = done
        
        return done
    
    def readline(self):

        """Read from arduino and parse responses. """
        try:
            line = self.serial.readline().decode("utf-8").strip()

            is_data, lat_long = self.lat_long_parser(line)

            if self.recording and is_data:

                self.data.append(lat_long)
            
            if is_data:

                return lat_long
            
            return None

        except Exception:
            self.is_connected = False
            self.is_ready = False
            try:
                self.serial.close()
                return None
            except serial.serialutil.SerialException:
                return None   
    
    def set_port_and_open(self):

        """Look for arduino port, set it and open communication."""

        ports = list_ports.comports() # serial.tools.list_ports

        if len(ports) == 0:
            return False

        arduino_port = None
        
        for port in ports:

            if "Arduino Uno" in port.description:
                arduino_port = port
            else: None

        if arduino_port:

            try:
                self.serial.port = arduino_port.name
                self.serial.open()
                return True

            except Exception:
                self.serial.port = None
                return False

    def lat_long_parser(self, line):
        
        """
        Split the string to extract latitude and longitude
        Convert latitude and longitude to a list of floats
        """
        lat_long_str = ""
        splited = ""

        try:
            splited = line.split("Location: ")

            lat_long_str = splited[1].split("  Date/Time:")[0]

            lat_long = list(map(float, lat_long_str.split(',')))

        except IndexError:

            return False, splited
        
        except ValueError:

            return False, lat_long_str

        return True, lat_long

class FileTypeDialog(QDialog):
    def __init__(self):
        super(FileTypeDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self) 

class EnsureDialog(QDialog):
    def __init__(self):
        super(EnsureDialog, self).__init__()
        self.ui = Ui_Ensure()
        self.ui.setupUi(self) 

class MyApp(QMainWindow, Ui_MainWindow):

    """Process class. """


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # arduino instance
        self.arduino = MyArduino()

        # process loop
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.process)
        self.timer.start()

        # status loop
        self.status = QTimer(self)
        self.status.setInterval(1000)
        self.status.timeout.connect(self.check_status)
        self.status.start()

        # connect buttons interactions
        self.saveButton.clicked.connect(self.save)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)
        self.clearButton.clicked.connect(self.clear)
        self.restartButton.clicked.connect(self.restart)
        self.slider.valueChanged.connect(self.timeoutChange)
 
    def timeoutChange(self, value):
        
        """ Get the slider value and change interval acordingly."""
        self.timer.setInterval(1000 * value)
        self.sliderLabel.setGeometry(740, 252 - 16 * value, 30, 10)
        self.sliderLabel.setText(f"{value}s")

    def process(self):

        """Set up, read and display data."""

        if not self.arduino.is_connected:
            is_set = self.arduino.setup()

            if is_set:
                self.displayLabel.setText(
                    "Welcome to GPS recording tool with ARDUINO. \n"
                    "Click on \"Start\" to start."
                )
            else:
                self.displayLabel.setText(
                    "Welcome to GPS recording tool with ARDUINO. \n"
                    "Arduino is not connected. \n"
                    "Please connect your arduino device."
                )

        else:
            response = self.arduino.readline()

            if response is not None: 

                # display lat and long  
                self.lat.display(response[0])
                self.long.display(response[1])
                
                # set is ready to start recording
                self.arduino.is_ready = True

                
            else:
                self.lat.display(0)
                self.long.display(0)
                self.arduino.is_ready = False           
            
    def check_status(self):

        """Check arduino status and display."""

        if self.arduino.is_connected:
            self.titleLight.setStyleSheet("QLabel {\n"
                "    background-color: green;  \n"
                "    border-radius: 10px;    \n"
                "    min-width: 20px;         \n"
                "    min-height: 20px;  \n"
                "}"
            )
        else: 
            self.titleLight.setStyleSheet("QLabel {\n"
                "    background-color: red;  \n"
                "    border-radius: 10px;    \n"
                "    min-width: 20px;         \n"
                "    min-height: 20px;  \n"
                "}"
            )

        if self.arduino.recording:

            self.readyLabel.setText("RECORDING :")

            if self.arduino.spin:
                self.arduino.spin = False
                self.readyLight.setStyleSheet("QLabel {\n"
                    "    background-color: green;  \n"
                    "    border-radius: 10px;    \n"
                    "    min-width: 20px;         \n"
                    "    min-height: 20px;  \n"
                    "}"
                )
            else:
                self.arduino.spin = True
                self.readyLight.setStyleSheet("QLabel {\n"
                    "    background-color: red;  \n"
                    "    border-radius: 10px;    \n"
                    "    min-width: 20px;         \n"
                    "    min-height: 20px;  \n"
                    "}"
                )
            
        else: 
            self.readyLabel.setText("READY TO START :")

            if self.arduino.is_ready:
                self.readyLight.setStyleSheet("QLabel {\n"
                    "    background-color: green;  \n"
                    "    border-radius: 10px;    \n"
                    "    min-width: 20px;         \n"
                    "    min-height: 20px;  \n"
                    "}"
                )
            else:
                self.readyLight.setStyleSheet("QLabel {\n"
                    "    background-color: red;  \n"
                    "    border-radius: 10px;    \n"
                    "    min-width: 20px;         \n"
                    "    min-height: 20px;  \n"
                    "}"
                )

    def save(self):

        """File saving process."""

        # Will not do anything if the device is not connected 
        if not self.arduino.is_connected:

            return

        if len(self.arduino.data) == 1:

            self.displayLabel.setText(
                "There is not any recorded data to save. \n"
                "Click on \"Start\" to start."
            )

            return
        
        dialog = FileTypeDialog()
        
        if dialog.exec_() == QDialog.Accepted:
            pd_data = pd.DataFrame(data=self.arduino.data[1:], columns=self.arduino.data[0])


            options = QFileDialog.Options()

            options |= QFileDialog.DontUseNativeDialog
            
            if dialog.ui.CSV.isChecked():

                file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)
                if file_path:
                    if not file_path.endswith(".csv"):
                        file_path += ".csv"
                    pd_data.to_csv(file_path, index=False)
                else:
                    self.displayLabel.setText(
                        "Saving data in CSV canceled.\n"
                        "Click on \"Save\" to save data."
                    )

            if dialog.ui.Excel.isChecked():

                file_path, _ = QFileDialog.getSaveFileName(self, "Save XLSX", "", "Excel Files (*.xlsx);;All Files (*)", options=options)
                if file_path:
                    if not file_path.endswith(".xlsx"):
                        file_path += ".xlsx"
                    pd_data.to_excel(file_path, index=False)
                else:
                    self.displayLabel.setText(
                        "Saving data in Excel canceled.\n"
                        "Click on \"Save\" to save data."
                    )

            if dialog.ui.Shp.isChecked():

                espg_code = 4326

                try :
                    espg_code = int(dialog.ui.espgInput.text)
                except Exception:
                    pass

                file_path, _ = QFileDialog.getSaveFileName(self, "Save SHP", "", "SHP Files (*.shp);;All Files (*)", options=options)
                if file_path:
                    geometry = [Point(xy) for xy in zip(pd_data["long"], pd_data["lat"])]
                    gpd_data = gpd.GeoDataFrame(pd_data, geometry=geometry)
                    gpd_data.set_crs(epsg=espg_code)
                    gpd_data.to_file(file_path, index=False)
                else:
                    self.displayLabel.setText(
                        "Saving data in SHP canceled.\n"
                        "Click on \"Save\" to save data."
                    )

    def clear(self):

        """Initialize everything: clear the data."""

        # Will not do anything if the device is not connected 
        if not self.arduino.is_connected:

            return

        # Display "No recorded data." and will not do anything if 
        # there is not any recorded data.
        if len(self.arduino.data) == 1:

            self.displayLabel.setText("No recorded data.")

            return
        
        dialog = EnsureDialog()

        if dialog.exec_() == QDialog.Accepted:

            try:

                self.arduino.data = [["lat", "long"]]

                self.arduino.recording = False

                self.displayLabel.setText("Data cleared Successfully !")

                self.startButton.setText("Start")

            except: 
                self.displayLabel.setText("An error occurs when clearing data !")
    
    def stop(self):

        """Stop recording"""

        if not self.arduino.recording:
            return
        
        self.arduino.recording = False

    def start(self):
        """Start recording."""

        # Should start only if the device is connected.
        if not self.arduino.is_connected: 

            return

        if self.arduino.recording:

            self.arduino.recording = False

            self.displayLabel.setText(
                "Recording paused ! \n"
                "Click on \"Continue\" to continue. \n"
                "Or click \"Restart\" to restart"
            )

            self.startButton.setText("Continue")
        
        else :
        
            self.arduino.recording = True

            self.displayLabel.setText(
                "Recording ... \n"
                "Click on \"Save\" to save your data."
            )

            self.startButton.setText("Pause")

    def restart(self):
        
        """Restart recording."""

        if not self.arduino.recording:
            return
        
        dialog = EnsureDialog()

        if dialog.exec_() == QDialog.Accepted:

            try:

                self.arduino.data = [["lat", "long"]]

                self.displayLabel.setText("Data recording restarted !")

            except: 
                self.displayLabel.setText("An error occurs when restarting !")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
