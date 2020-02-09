import json

settings_path = 'C:/Users/Matthew/PycharmProjects/scratches/custom_widgets/widget_settings.json'
content_path = 'C:/Users/Matthew/PycharmProjects/scratches/custom_widgets/content.json'
# settings_path = 'widget_settings.json'
# content_path = 'content.json'


def get_settings(path, widget_name):
    with open(path, 'r') as file:
        return json.load(file)[widget_name][0]


def get_content(path, chapter, page):
    # print(chapter, page)
    with open(path, 'r') as file:
        return json.load(file)[chapter][0][page][0]


def content_to_text(content, tag):
    with open(content[tag]) as file:
        text_content = file.readlines()
        temp = ""
        for i in text_content:
            temp += i
        content[tag] = temp
    return temp


def get_c_content(path, chapter, page, tag):
    content_i = get_content(path, chapter, page)
    with open(content_i[tag], 'r') as file:
        text = file.readlines()
        temp = ""
        for i in text:
            temp += i
        content_i[tag] = temp
    return content_i


def get_dimension(instance, scalar):

    if len(instance.text) < 25:
        width = ((len(instance.text) / 2) * instance.font_size) * 1.1
    else:
        width = (len(instance.text) / 2) * instance.font_size

    height = instance.font_size * 1.35
    return width * scalar, height * scalar


def get_sub_content(path, chapter, page, tag):
    with open(path, 'r') as file:
        content = json.load(file)[chapter][0][page][0][tag][0]

        print(content)
        return content
