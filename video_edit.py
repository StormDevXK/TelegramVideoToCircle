import moviepy
import moviepy.editor as mpe
import moviepy.video.fx.all as vfx


def cut_video(en: str, ex: str):
    clip = mpe.VideoFileClip(en)
    cs = clip.size
    print(cs, (cs[0] - 576) // 2, (cs[1] - 576) // 2)
    # res = vfx.crop(clip, x1=(cs[0] - 576) // 2, width=576, y1=(cs[1] - 576) // 2, height=576)
    if cs[0] < cs[1]:
        res = vfx.resize(clip, width=576)
        res = vfx.crop(res, y1=(res.size[1] - 576) // 2,  height=576)
    else:
        res = vfx.resize(clip, height=576)
        res = vfx.crop(res, x1=(res.size[0] - 576) // 2,  width=576)
    res.write_videofile(ex)
