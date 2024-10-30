import subprocess   
from pathlib import Path
import glob
import re

def create_video_from_frames(frames_dir, output_path, fps=30):
    frames = sorted(glob.glob(f"{frames_dir}/*.png"))
    assert frames, "No PNG files in the directory."
    
    first_frame = frames[0]
    first_frame_number = Path(first_frame).stem
    print(first_frame_number)
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-framerate", str(fps),
        "-start_number", str(int(first_frame_number)),
        "-i", f"{frames_dir}/%05d.png",
        "-c:v","libx264",
        "-pix_fmt", "yuv420p",
        "-f", "mp4",
        output_path
    ]
    
    subprocess.run(ffmpeg_cmd, check=True)

if __name__ == "__main__":
    print("main")