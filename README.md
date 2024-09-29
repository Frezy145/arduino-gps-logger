# arduino-gps-logger
## GPS Data recorder ARDUINO UNO, Python and PyQt5

This project allows you to record GPS coordinates from an Arduino device and save the data in different formats (CSV, Excel, Shapefile) using a PyQt5-based graphical user interface (GUI). The GUI also provides an option to specify an EPSG code when saving shapefiles for geographic coordinate system reference.

<div>
  <img src="https://github.com/user-attachments/assets/5920efb7-139e-4759-9fc1-31c7fa2e6a90" alt="Image" width=550 height=450/>
</div>

### Features

- Record real-time GPS data from Arduino Uno
- Save the recorded data in CSV, Excel, and Shapfiles formats.
- Option to specify an EPSG code for shapefiles (default : EPSG 4326 for WGS84).
- Simple & intuitive PyQt5-based GUI.

### Prerequisites 
Before running the project, ensure you have the following installed: 
- Python 3.x
- PyQt5
- pandas
- geopandas
- pyserial
- shapely

You can install the required Python libraries using:
```python
pip install pyqt5 pandas geopandas pyserial shapely
```
## Getting Started
1. **Clone the repository**

```bash
git clone https://github.com/your-username/arduino-gps-logger.git
cd gps-data-recorder
```
2. **Connect your Arduino**

Ensure your Arduino Uno device is connected and transmitting GPS data.

3. **Run the GUI**

To launch the application, run:
```python
python main.py
```

4. **Using the Application:**

Click "Start" to begin recording GPS data from the Arduino.
After recording, click "Save" to open the save dialog.
Choose the desired file format (CSV, Excel, Shapefile).
If saving as a Shapefile, you can enter the EPSG code (default: 4326).
Click "Save" to save the data to the chosen format and location.

## How to Test
1. **Simulate GPS Data:**

If you don't have an Arduino, you can modify the code to simulate GPS data. In the readline() method, return dummy latitude and longitude values for testing.

2. **Test Saving Features:**

Run the GUI and simulate recording data. Test saving in all three formats:
- CSV
- Excel
- Shapefile (with and without custom EPSG codes)

3. **Validate Saved Files:**

- Open the CSV and Excel files to ensure the data is recorded correctly.
- Use GIS software (like QGIS) to open the Shapefile and verify the EPSG code and data.

## License
This project is licensed under the MIT License.
   
