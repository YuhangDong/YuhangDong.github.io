# -*- coding: utf-8 -*-
# @Author: AI悦创
# @Date:   2022-05-19 11:40:50
# @Last Modified by:   aiyc
# @Last Modified time: 2022-05-20 11:28:48
import os, time, uuid

BASEURL = "https://cd.xfomo.net/"


def parse_path(path):
    # for i in os.walk(path):
    target = ["mp4", "mov"]
    for dirpath, dirnames, filenames in os.walk(path):
        # print(i)
        # print(filenames)
        for path in filenames:
            # print(path.split("."))
            # print(filenames)
            # print(os.path.join(dirpath, path))
            # file_path = os.path.join(dirpath, path)
            # if file_path.split(".")[-1] == "mp4":
            # if path.split(".")[-1] == "mp4":
            if path.split(".")[-1].lower() in target:
                # print(path)
                yield path


def generate_html():
    pass


def save_readme(content):
    with open("../README.md", "a+", encoding="utf-8") as f:
        f.write(
            f"""```url
{content}
```""" + "\n"
        )


def split_movie(path, movie_name="Defualt"):
    # os.system("cd result")
    flodr = str(uuid.uuid4())
    if not os.path.exists(flodr):
        os.mkdir(flodr)
    os.chdir(flodr)  # 指定输出路径
    print(os.getcwd())
    time.sleep(6)
    os.system(f"ffmpeg -i {path} -profile:v " \
              "baseline -level 3.0 -s 1920x1080 -start_number 0 " \
              f"-hls_time 10 -hls_list_size 0 -f hls {movie_name}.m3u8")
    url = BASEURL + flodr + "/" + f"{movie_name}.m3u8"
    save_readme(url)


def main():
    root = os.getcwd()
    # print("root", root)
    path = "."
    file_path = parse_path(path)
    # print(list(file_path))
    for path in file_path:
        try:
            new_path = path.replace(" ", "")
            os.rename(path, new_path)
        except FileNotFoundError as e:
            print("e:>>>", e)
        finally:
            r_path = os.path.join(os.getcwd(), new_path)
            # print(r_path)
            movie_name = new_path.split(".")[0]
            # print(movie_name)
            print(f"r_path: {r_path}, \nmovie_name: {movie_name}")
            # print(os.getcwd())
            # print(os.path.join(os.getcwd(), file_path))
            split_movie(r_path, movie_name)
            # os.remove(new_path)
            # print(new_path)
    # os.system("git add .")
    # os.system("git commit -m 'up'")
    # os.system("git push")
    # os.chdir(root)
    # os.system("sh deploy.sh")


if __name__ == "__main__":
    main()

# Auto Delete Code
