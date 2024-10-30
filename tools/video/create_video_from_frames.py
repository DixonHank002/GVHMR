import subprocess   
from pathlib import Path
import glob

def create_video_from_frames(frames_dir, output_path, fps=30):
    frames = sorted(glob.glob(f"{frames_dir}/*.png"))
    assert frames, "No PNG files in the directory."
    
    ffmpeg_cmd = [
        "ffmpeg",
        "-y",
        "-framerate", str(fps),
        "-i", f"{frames_dir}/%05d.png",
        "-c:v","libx264",
        "-pix_fmt", "yuv420p",
        "-f", "mp4",
        output_path
    ]
    
    subprocess.run(ffmpeg_cmd, check=True)

if __name__ == "__main__":
    print("main")