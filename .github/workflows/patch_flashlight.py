import sys
import os

try:
    filepath = 'bootable/recovery/twrp-functions.cpp'
    if not os.path.exists(filepath):
        filepath = 'bootable/recovery/gui/action.cpp' # fallback
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Replace the standard '1', '255', and '0' strings with the OPPO matrix string
    content = content.replace('write_file(flashlight_path, "1")', 'write_file(flashlight_path, "0 0 0 1")')
    content = content.replace('write_file(flashlight_path, "255")', 'write_file(flashlight_path, "0 0 0 1")')
    content = content.replace('write_file(flashlight_path, "0")', 'write_file(flashlight_path, "0 0 0 0")')
    
    with open(filepath, 'w') as f:
        f.write(content)
        
    print("Flashlight patch applied successfully!")
except Exception as e:
    print(f"Failed to patch flashlight: {e}")
