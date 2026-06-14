# Geelong Weather Dashboard - User Manual
This manual illustrates how to set up and operate the automated local weather dashboard.

## 1. Prerequistes
* Python 3.10+ installed
* Active internet connection for live BOM data
* A modern web browser

## 2. Setup and Installation
1. Open a terminal appliaction (e.g. Git Bash) and navigate to the project directory:
    ```bash
    cd ICTPRG343_AT3
    ```
2. Install the required Python modules by running:
    ```bash
    pip install flask matplotlib requests
    ```

## 3. Runnin the Application 
1. Start the Flask local web server with this command:
    ```bash
    python app.py
    ```
2. Once the terminal shows `* Running on http://127.0.0.1:5000` open your web browser.
3. Go to the page using the address:
    ```text
    http://127.0.0.1:5000
    ```

## 4. How to Use the Dashboard
* **View Data**: The top four panels display live data. The graphs show the latest tweleve hours of rolling data.
* **Refresh Numbers**: Select Refresh on your browser. Data is fetched from the server and the graphs are updated instantaneously. 
* **Turn off Server**: Click your terminal window and select Crtl + C. 

## 5. Troubleshooting
* **Boxes Show "N/A"**: This means either your internet is disconnected or the BOM API is down. Check your internet connection and refresh your browser.
* **"Site Can't Be Reached"**: Thsi means you closed the terminal window that runs in the background. The terminal must remain open while you acces the site.

