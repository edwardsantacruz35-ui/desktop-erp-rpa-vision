import cv2
import numpy as np
import pyautogui

class VisionEngine:
    """Multi-scale computer vision template matcher for ERP UI detection"""
    
    def __init__(self, template_path, confidence_threshold=0.60):
        self.template_path = template_path
        self.confidence_threshold = confidence_threshold
        self.template = cv2.imread(template_path)
        
    def locate_window(self):
        """Captures active screen and performs multi-scale template matching"""
        if self.template is None:
            raise FileNotFoundError(f"Template not found at: {self.template_path}")
            
        screen_pil = pyautogui.screenshot()
        screen = cv2.cvtColor(np.array(screen_pil), cv2.COLOR_RGB2BGR)
        
        best_val = -1
        best_loc = None
        best_scale = 1.0
        
        # Search across 50% to 140% dynamic DPI scale factors
        for scale in np.linspace(0.50, 1.40, 46):
            w = int(self.template.shape[1] * scale)
            h = int(self.template.shape[0] * scale)
            if w <= 0 or h <= 0 or w > screen.shape[1] or h > screen.shape[0]:
                continue
            resized = cv2.resize(self.template, (w, h))
            res = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            if max_val > best_val:
                best_val = max_val
                best_loc = max_loc
                best_scale = scale
                
        if best_val >= self.confidence_threshold and best_loc is not None:
            return {
                "detected": True,
                "confidence": best_val,
                "scale": best_scale,
                "origin_x": best_loc[0],
                "origin_y": best_loc[1]
            }
            
        return {"detected": False, "confidence": best_val, "scale": 1.0, "origin_x": 0, "origin_y": 0}
