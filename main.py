import cv2
import numpy as np

def detect_color(hsv_mean):
    """Detect color using HSV values"""
    h, s, v = hsv_mean
    
    # Check for white/gray/black first (low saturation)
    if s < 50:
        if v > 180:
            return 'White'
        elif v < 60:
            return 'Black'
        else:
            return 'Gray'
    
    # If brightness is too low
    if v < 60:
        return 'Black'
    
    # Define hue ranges for colors (tighter ranges)
    colors = [
        ('Red', 0, 8),
        ('Orange', 8, 20),
        ('Yellow', 20, 33),
        ('Green', 33, 78),
        ('Cyan', 78, 95),
        ('Blue', 95, 130),
        ('Purple', 130, 150),
        ('Pink', 150, 170),
        ('Red', 170, 180)
    ]
    
    # Find matching color based on hue
    for color_name, hue_min, hue_max in colors:
        if hue_min <= h <= hue_max:
            return color_name
    
    return 'Unknown'


video = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = video.read()
        
        # Get center region
        height, width = frame. shape[:2]
        center_x, center_y = width // 2, height // 2
        sample_size = 100
        
        center_region = frame[
            center_y - sample_size:center_y + sample_size,
            center_x - sample_size:center_x + sample_size
        ]
        
        # Convert to HSV
        hsv_region = cv2.cvtColor(center_region, cv2.COLOR_BGR2HSV)
        
        # Get MEDIAN instead of mean (more accurate)
        h_mean = np.median(hsv_region[:, :, 0])
        s_mean = np. median(hsv_region[:, :, 1])
        v_mean = np.median(hsv_region[:, :, 2])
        
        # Detect color
        color_name = detect_color([h_mean, s_mean, v_mean])
        
        # Draw detection box
        cv2.rectangle(frame, 
                     (center_x - sample_size, center_y - sample_size),
                     (center_x + sample_size, center_y + sample_size),
                     (0, 255, 0), 3)
        
        # Display color with larger text
        cv2.putText(frame, f"{color_name}", 
                   (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 5)
        cv2.putText(frame, f"{color_name}", 
                   (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
        
        # Show HSV values for debugging
        cv2.putText(frame, f"H:{int(h_mean)} S:{int(s_mean)} V:{int(v_mean)}", 
                   (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        
        cv2.imshow('Color Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
finally:
    video.release()
    cv2.destroyAllWindows()
    print('Camera released and windows closed')