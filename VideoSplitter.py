import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from tkinter import Tk, filedialog, Label, Button, Entry

class VideoSplitter:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Splitter")

        self.file_path = None
        self.duration_entry = None

        self.label = Label(root, text="Select a video file and set the duration for each segment.")
        self.label.pack()

        self.select_button = Button(root, text="Select File", command=self.select_file)
        self.select_button.pack()

        self.duration_label = Label(root, text="Split Duration (seconds):")
        self.duration_label.pack()

        self.duration_entry = Entry(root)
        self.duration_entry.pack()

        self.split_button = Button(root, text="Split Video", command=self.split_video, state="disabled")
        self.split_button.pack()

        self.exit_button = Button(root, text="Exit", command=self.exit)
        self.exit_button.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
        if self.file_path:
            self.label.config(text=f"Selected File: {os.path.basename(self.file_path)}")
            self.split_button.config(state="normal")

    def exit(self):
        root.destroy()
        root.quit()

        
    def split_video(self):
        if self.file_path:
            try:
                self.duration = float(self.duration_entry.get())
            except ValueError:
                self.label.config(text="Invalid duration. Please enter a valid number.")
                return

            video_clip = VideoFileClip(self.file_path)
            segments = video_clip.duration // self.duration

            for i in range(int(segments)):
                start_time = i * self.duration
                end_time = (i + 1) * self.duration
                segment_clip = video_clip.subclip(start_time, end_time)
                output_path = f"{os.path.splitext(self.file_path)[0]}_{i + 1}.mp4"
                segment_clip.write_videofile(output_path, codec="libx264")

            self.label.config(text="Video split successfully!")

if __name__ == "__main__":
    root = Tk()
    app = VideoSplitter(root)
    root.mainloop()
