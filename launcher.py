# launcher.py
import os
import subprocess
import sys

def launch_game(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext in ['.iso', '.elf']:
        print(f"Launching Wii/GameCube game: {file_path}")
        subprocess.run(["Wii/Dolphin/build/bin/Dolphin", file_path])
        
    elif ext in ['.rpx']:
        print(f"Launching Wii U game: {file_path}")
        # Placeholder for Wii U emulator
        # subprocess.run(["WiiU/Emulator/bin/WiiUEmu", file_path])
        
    else:
        print("Unsupported file type")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python launcher.py <gamefile>")
    else:
        launch_game(sys.argv[1])
