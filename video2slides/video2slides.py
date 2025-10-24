import os
import glob
import imagehash
import shutil
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


def videos_to_frames(input_video_list, frames_dir):
    for i, input_video in enumerate(input_video_list):
        extract_keyframes_command = f'ffmpeg -skip_frame nokey -i "{input_video}" -vsync vfr -qscale:v 2 ./{frames_dir}/out-{i:03d}-%08d.jpg'
        print(extract_keyframes_command)
        os.system(extract_keyframes_command)

    n = len(os.listdir(frames_dir))
    return n


def select_unique_frames_by_hash(frames_dir, unique_images_dir):
    # frames_paths = glob.glob(os.path.join(frames_dir, '*.jpg'))
    frames_paths = sorted([os.path.join(frames_dir, item) for item in os.listdir(frames_dir)], reverse=True)
    previous_frame_hash = ""
    counter = 0

    print('detecting unique frame ...')
    for frame in frames_paths:
        img = Image.open(frame)
        # hash = str(imagehash.whash(img))
        # hash = str(imagehash.dhash(img))
        # hash = str(imagehash.average_hash(img))
        # hash = str(imagehash.colorhash(img))
        # hash = str(imagehash.crop_resistant_hash(img))
        # hash = str(imagehash.phash(img))
        # hash = str(imagehash.dhash_vertical(img))

        # the best! It's interesting that this hash can tolerate added things in a series of a slides and return a
        # unique hash for all!!! So we need check in reverse order
        hash = str(imagehash.phash_simple(img))

        if previous_frame_hash != hash:
            ext = os.path.splitext(frame)[1]
            dst = os.path.join(unique_images_dir, os.path.basename(frame)[:-len(ext)] + "_" + hash + ext)
            shutil.copy(frame, dst)
            counter +=1
            print(counter, '_', os.path.basename(frame), ":", hash)

            previous_frame_hash = hash

    return counter


def select_unique_frames_by_subtract(input_dir, output_dir):
    tmp_frames_paths = sorted([os.path.join(input_dir, item) for item in os.listdir(input_dir)])
    frames_paths = []
    for ff in tmp_frames_paths:
        if os.path.isfile(ff):
            frames_paths.append(ff)

    counter = 0
    for i in range(0, len(frames_paths)-1):
        img1 = cv2.imread(frames_paths[i])
        img2 = cv2.imread(frames_paths[i+1])
        res = cv2.subtract(img1, img2)
        print(f'img{i} - img{i+1}: {np.mean(res)}')

        # cv2.imshow('image', res)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        if np.mean(res) > 2:
            ext = os.path.splitext(frames_paths[i])[1]
            dst = os.path.join(output_dir, os.path.basename(frames_paths[i])[:-len(ext)] + "_" + ext)
            shutil.copy(frames_paths[i], dst)
            counter += 1
            print(counter, '_', os.path.basename(frames_paths[i]))

    return counter


def add_page_number_and_border_to_images(input_dir, start_number=1):
    unique_images = sorted(
        [os.path.join(input_dir, item) for item in os.listdir(input_dir) if item.endswith('jpg')])

    for i, img_path in enumerate(unique_images):
        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 30)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((10, 10), f'{start_number+i}', 0, font=font)

        img = ImageOps.expand(img, border=15, fill='white')
        # img_with_border.save('imaged-with-border.png')

        img.save(img_path)

        print(f'write image number on "{img_path}"')


def reverse_colors_of_frames(input_dir, output_dir):
    frames_paths = sorted([os.path.join(input_dir, item) for item in os.listdir(input_dir)])
    for frame in frames_paths:
        dst = os.path.join(output_dir, os.path.basename(frame))
        command = f'convert {frame} -channel RGB -negate {dst}'
        print(command)
        os.system(command)
        print(f'{dst} reversed.')


def four_frames_to_one_slide(input_dir, output_dir, is_right_to_left=False, first_page_name=''):
    """
    img2pdf 1-4.png 5-8.png 9-12.png 13-16.png 17-18.png -o out.pdf

    img2pdf `ls *.png|sort -g` -o ouput.pdf
    """

    images = glob.glob(os.path.join(input_dir, '*.jpg'))
    images = sorted(images, key=lambda x: os.path.basename(x))

    first_page_index = 0
    for i, img in enumerate(images):
        if os.path.basename(img) == first_page_name:
            first_page_index = i
            break

    if is_right_to_left is True:
        order_list = [1, 0, 3, 2]

    else:
        order_list = [0, 1, 2, 3]

    counter = 0
    for start_index in range(first_page_index, len(images), 4):
        four_in_one_command = 'montage '
        for i in order_list:
            ind = start_index + i
            if ind < len(images):
                # four_in_one_command += f'{os.path.basename(images[ind])} '
                four_in_one_command += f'{images[ind]} '

            else:
                four_in_one_command += f'white-empty-page.jpg '

        four_in_one_command += \
            f'-tile 2x2 -geometry +0+0 {output_dir}/{start_index + 1:04}-{min(start_index + 4, len(images)):04}.png'

        print(four_in_one_command)
        os.system(four_in_one_command)
        counter+=1

    return counter


def create_final_pdf(slides_dir, final_pdf_dir):
    create_pdf_command = f'img2pdf `ls "{slides_dir}"/*.png|sort -g` -o "{final_pdf_dir}/final.pdf"'
    print(create_pdf_command)
    os.system(create_pdf_command)

    final_pdf_path = f'{final_pdf_dir}/final.pdf'
    print(f'final_pdf_path: {final_pdf_path}')
    return


def main():
    videos_dir = '/imi/study/__Network__/A. [great] [6h 25m] Linux Networking and Troubleshooting/LinuxAcademy - Linux Networking and Troubleshooting/'
    input_video_list = sorted([os.path.join(videos_dir, item) for item in os.listdir(videos_dir) if item.endswith('mp4')])
    input_video_list = input_video_list[6:]
    do_reverse_color = True

    frames_dir = '1_frames'
    unique_frames_by_hash_dir = '2_unique_by_hash'
    unique_frames_by_subtract_dir = '3_unique_by_subtract'

    start_number = 35

    reversed_frames_dir = '4_reverse_colors'
    page_and_border = '5_add_page_number_and_border'
    four_images_in_one_image_dir = '5_four_in_one'
    final_pdf_dir = '6_final_pdf'

    if True:
        # number_of_frames = videos_to_frames(input_video_list, frames_dir)
        # print(f'{number_of_frames} frames were extracted.')

        # n = select_unique_frames_by_hash(frames_dir, unique_frames_by_hash_dir)
        # print(f'{n} unique frames were detected by hash.')

        # n = select_unique_frames_by_subtract(unique_frames_by_hash_dir, unique_frames_by_subtract_dir)
        # print(f'{n} unique frames were detected by subtract.')

        if do_reverse_color is True:
            reverse_colors_of_frames(unique_frames_by_subtract_dir, reversed_frames_dir)
            src = reversed_frames_dir
        else:
            src = unique_frames_by_subtract_dir

        add_page_number_and_border_to_images(reversed_frames_dir, start_number=start_number)

    else:
        n = four_frames_to_one_slide(src, four_images_in_one_image_dir)
        print(f'{n} slides are created. Each slide has 4 images.')

        create_final_pdf(four_images_in_one_image_dir, final_pdf_dir)
        print('Done! :)')


if __name__ == '__main__':
    # reverse_colors_of_frames('/imi/IMI/my-projects/my-toolbox/video2slides/4_reverse_colors/re/', '/imi/IMI/my-projects/my-toolbox/video2slides/tmp/')
    exit()
    main()
