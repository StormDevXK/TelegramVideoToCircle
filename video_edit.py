import moviepy
import moviepy.editor as mpe
import moviepy.video.fx.all as mpec


def cut_video(en: str, ex: str):
    clip = mpe.VideoFileClip(en)
    cs = clip.size
    print(cs, (cs[0] - 576) // 2, (cs[1] - 576) // 2)
    res = mpec.crop(clip, x1=(cs[0] - 576) // 2, width=576, y1=(cs[1] - 576) // 2, height=576)
    res.write_videofile(ex)
