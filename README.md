# 🚗 Car Plate Detection using OpenCV

This project performs **real-time number plate detection** using OpenCV and a Haar Cascade Classifier. It captures live video from a webcam, identifies number plates, highlights them with bounding boxes, and displays cropped regions (ROI) for a closer look.

---

## 📌 Features

- Real-time video feed from webcam
- Automatic detection of number plates
- Bounding box and label overlay for detected plates
- Display of cropped plate (ROI) for each detection
- Adjustable detection sensitivity and frame settings

---

## 🛠️ Requirements

- Python 3.x
- OpenCV (`opencv-python`)

Install OpenCV using pip:

```bash
pip install opencv-python
```
##📁 File Structure
```bash 
CarPlateDetection/
│
├── haarcascade_russian_plate_number.xml  # Pre-trained Haar cascade model
├── car_plate_detection.py                # Main detection script
└── README.md                              # Documentation file
```
## ▶️ How to Run

1. **Clone this repository** or download the project files.

2. **Ensure the path** to the `haarcascade_russian_plate_number.xml` file is correctly set in the script. 

   
3. **Run the script:**
   ```bash
   python car_plate_detection.py
   ```
4. A webcam window will appear. Detected number plates will be outlined with a bounding box and shown in a separate cropped window.

5. Press `q` to quit the application.
  
