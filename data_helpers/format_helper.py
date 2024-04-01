import os

def get_cover_story(n):
    cover_story = ""
    if n > 5:
        raise ValueError("Cover Story Undefined")
    match n:
        case 1:
            print("task file one")
            cover_story = "task_1.txt"
        case 2:
            print("task file two")
            cover_story = "task_2.txt"
        case 3:
            print("task file three")
            cover_story = "task_3.txt"
        case 4:
            print("task file four")
            cover_story = "task_4.txt"
        case 5:
            print("task file five")
            cover_story = "task_5.txt"
    with open(os.path.abspath(os.path.join(os.path.join(os.pardir, os.path.join("files", "task_files")), cover_story))) as file:
        formatted_cover_story = file.read().replace('\n', '')
    return formatted_cover_story
