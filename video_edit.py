import moviepy
import moviepy.editor as mpe
import moviepy.video.fx.all as vfx
# import ffmpeg


def add_image(clip, img_name: str):
    img = (mpe.ImageClip(f'imgs/{img_name}.png')
           .set_duration(clip.duration)
           # .resize(height=50)  # если необходимо поменять размер...
           # .margin(right=8, top=8, opacity=0)  # (опционально) logo-border padding
           .set_pos(('center', 'center')))
    final = mpe.CompositeVideoClip([clip, img])
    return final


async def cut_video(en: str, ex: str, img: str = None):
    cclip = mpe.VideoFileClip(en)
    clip = cclip.set_fps(30)
    cs = clip.size
    print(cs, (cs[0] - 576) // 2, (cs[1] - 576) // 2)
    if cs[0] < cs[1]:
        res = vfx.resize(clip, width=576)
        res = vfx.crop(res, y1=(res.size[1] - 576) // 2, height=576)
    else:
        res = vfx.resize(clip, height=576)
        res = vfx.crop(res, x1=(res.size[0] - 576) // 2, width=576)
    if img is not None:
        res = add_image(res, img)
    res.write_videofile(ex)


# stream = ffmpeg.input('video.mp4')
# stream = ffmpeg.filter(stream, 'fps', fps=10, round='up')
# stream = ffmpeg.output(stream, 'out.mp4')
# ffmpeg.run(stream)
# abs = ffmpeg.probe('out.mp4')

# stream = ffmpeg.input('input.mp4')
# stream = ffmpeg.hflip(stream)
# stream = ffmpeg.output(stream, 'output.mp4')
# ffmpeg.run(stream)
