from moviepy.editor import vfx, VideoFileClip, concatenate_videoclips 

clipe1 = VideoFileClip(r'C:\Users\Guilherme\Desktop\Estudos.dev\Python\video.mp4').subclip(0, 6).fx(vfx.fadeout, 1)
clipe2 = VideoFileClip(r'C:\Users\Guilherme\Desktop\Estudos.dev\Python\video.mp4').subclip(12, 19).fx(vfx.fadein, 1).fx(vfx.fadeout, 1)

video_concatenado = concatenate_videoclips([clipe1, clipe2])

video_concatenado.write_videofile(r'C:\Users\Guilherme\Desktop\Estudos.dev\Python\video_editado.mp4')