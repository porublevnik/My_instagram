import json
from json import JSONDecodeError


def get_posts_all():
    """Загружает файл с постами и преобразует из формата JSON"""
    try:
        with open('static/data/posts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print('Файл posts.json отсутствует')
    except JSONDecodeError:
        print("Файл posts.json не удается преобразовать")


def get_comments_all():
    """Загружает файл с комментариями и преобразует из формата JSON"""
    try:
        with open('static/data/comments.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print('Файл comments.json отсутствует')
    except JSONDecodeError:
        print("Файл comments.json не удается преобразовать")


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    return [post for post in get_posts_all() if post['poster_name'] == user_name]


def get_comments_by_post_id(post_id):
    """Возвращает комментарии к выбранному посту"""
    return [comment for comment in get_comments_all() if comment['post_id'] == post_id]


def search_for_posts(query):
    """Из файла с постами получает список постов, содержащих поисковой запрос"""
    return [post for post in get_posts_all() if query.lower() in post['content'].lower()]


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    for post in get_posts_all():
        if post['pk'] == pk:
            return post


def cut_posts(posts):
    """Укорачивает посты в списке до 100 символов"""
    for post in posts:
        post['content'] = post['content'][0:99]+'...'
    return posts


def convert_tags_to_links(content):
    """Преобразует хэштеги в ссылки в одной строке"""
    words = content.split(' ')
    for word in words:
        if len(word) > 1 and word[0] == '#' and word[1] != '#':
            content = content.replace(word, f'<a href="/tag/{word[1:]}">{word}</a>', 1)
    return content

def convert_tags_in_posts(posts):
    """Преобразует хэштеги в ссылки в списке постов"""
    for post in posts:
        post['content'] = convert_tags_to_links(post['content'])
    return posts


def get_bookmarks():
    """Возвращает список номеров постов в закладках"""
    try:
        with open('static/data/bookmarks.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print('Файл bookmarks.json отсутствует')
    except JSONDecodeError:
        print("Файл bookmarks.json не удается преобразовать")
    return


def load_posts_in_bookmarks():
    """Возвращает посты в закладках"""
    posts = list(filter(lambda x: x['pk'] in get_bookmarks(), get_posts_all()))
    return posts


def add_bookmark(post_pk):
    """Добавляет номер поста в закладки"""
    data = get_bookmarks()
    data.append(post_pk)
    data = list(set(data))
    with open('static/data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
    return


def delete_bookmark(post_pk):
    """Удаляет номер поста из закладок"""
    data = get_bookmarks()
    if post_pk in data:
        data.remove(post_pk)
        with open('static/data/bookmarks.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
    return
