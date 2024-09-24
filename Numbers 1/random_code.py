with open("numbers_video_base64.txt", "rb") as fp:
    numbers_video_description = str(fp.readline())

print(numbers_video_description.replace("/", "").replace("+", ""))
