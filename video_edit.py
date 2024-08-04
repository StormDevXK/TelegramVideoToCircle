import ffmpeg

async def cut_video(input_file, output_file):
    print(input_file)
    # Прочитать видеофайл и получить его размеры
    probe = ffmpeg.probe(input_file)
    video_info = next(stream for stream in probe['streams'] if stream['codec_type'] == 'video')
    width = int(video_info['width'])
    height = int(video_info['height'])

    # Рассчитать новые размеры с учетом уменьшения меньшей стороны до 576 пикселей
    if width < height:
        new_width = 576
        new_height = int(height * (576 / width))
    else:
        new_height = 576
        new_width = int(width * (576 / height))

    # Обрезать большую сторону до 576 пикселей, центруя видео
    crop_x = (new_width - 576) // 2 if new_width > 576 else 0
    crop_y = (new_height - 576) // 2 if new_height > 576 else 0

    # Создать команду ffmpeg
    input_stream = ffmpeg.input(input_file)
    video = (
        input_stream
        .filter('scale', new_width, new_height)
        .filter('crop', w=576, h=576, x=crop_x, y=crop_y)
        .filter('fps', fps=30)
    )
    audio = input_stream.audio

    # Объединить видео и аудио, и сохранить в выходной файл
    ffmpeg.output(video, audio, output_file).run()
