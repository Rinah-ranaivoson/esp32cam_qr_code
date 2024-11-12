
# ESP32Cam QR Code Decoder

This project allows you to capture a video stream from an ESP32Cam module and decode QR codes in real-time. The ESP32Cam is set up to serve images at different resolutions (low, medium, high), which can be accessed via HTTP endpoints. The Python script fetches these images and uses the `pyzbar` library to decode any QR codes found in the stream.

## Requirements

### Software Requirements

Before running the Python script, ensure you have the following libraries installed:

1. **OpenCV**: For image processing and displaying the video feed.
2. **NumPy**: For handling image arrays.
3. **pyzbar**: For decoding QR codes from image frames.

You can install the required dependencies using `pip`:

```bash
pip install opencv-python numpy pyzbar
```

### Hardware Requirements

1. **ESP32Cam**: The ESP32Cam module must be set up and running a simple web server to serve images at different resolutions (low, medium, high).
2. **Wi-Fi Network**: Both the ESP32Cam and the device running the Python script must be on the same Wi-Fi network.

## Setup

### Step 1: Configure the ESP32Cam

Make sure your ESP32Cam is configured correctly to serve images at different resolutions. The ESP32Cam should be running the provided code (already in your repository), which sets up a web server to serve images at the following endpoints:

- **Low resolution**: `/cam-lo.jpg`
- **Medium resolution**: `/cam-mid.jpg`
- **High resolution**: `/cam-hi.jpg`

After uploading the code to the ESP32Cam and connecting it to your Wi-Fi network, the ESP32Cam will print its IP address to the Serial Monitor. For example:

```
http://192.168.1.100
  /cam-lo.jpg
  /cam-hi.jpg
  /cam-mid.jpg
```

### Step 2: Update and Run the Python QR Code Decoder

1. **Update the ESP32Cam Stream URL**:
   In the Python script, replace the URL with the IP address of your ESP32Cam. For example:
   ```python
   url = 'http://192.168.1.100/cam-hi.jpg'
   ```

2. **Run the Python Script**:
   Execute the script in your terminal or Python environment:
   ```bash
   python esp32cam_qr_decoder.py
   ```

3. **QR Code Detection**:
   The video stream will be displayed in a window called **"ESP32Cam QR Code Decoder"**. If any QR code is detected in the image frame, a green rectangle will be drawn around it, and the decoded content will be shown next to the code. The decoded QR code content will also be printed in the terminal.

4. **Exit the Application**:
   - To stop the script and close the video window, press the **`q`** key.

## Available Endpoints

The following HTTP endpoints are available to capture images from the ESP32Cam:

- **Low Resolution**: `/cam-lo.jpg`
- **Medium Resolution**: `/cam-mid.jpg`
- **High Resolution**: `/cam-hi.jpg`

You can change the resolution by modifying the Python script to request images from different endpoints.

## Example Output

- **QR Code detected**:
  ```
  1234567890abcdef
  ```
- **Image display**: The video feed will show a rectangle around any detected QR code, and the decoded text will be displayed next to the QR code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

