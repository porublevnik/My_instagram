import json
from json import JSONDecodeError


class Post:
    def __init__(self, poster_name, poster_avatar, pic, content, views_count, likes_count, pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def cut_post(self):
        """Укорачивает пост до 100 символов"""
        self.content = self.content[0:99] + '...'

    def convert_tags_to_links(self):
        """Преобразует хэштеги в ссылки в одной строке"""
        self.content = self.content.split(' ')
        for word in self.content:
            if len(word) > 1 and word[0] == '#' and word[1] != '#':
                self.content = self.content.replace(word, f'<a href="/tag/{word[1:]}">{word}</a>', 1)


class PostDAO:
    def __init__(self, file):
        self.file = file


    def get_posts_all(self):
        """Загружает файл с постами и преобразует из формата JSON"""
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            posts = [Post(i['poster_name'], i['poster_avatar'], i['pic'], i['content'], i['views_count'],
                          i['likes_count'], i['pk']) for i in data]
            return posts
        except FileNotFoundError:
            print(f'Файл {self.file} отсутствует')
        except JSONDecodeError:
            print(f'Файл {self.file} не удается преобразовать')


    def search_for_posts(self, query):
        """Из файла с постами получает список постов, содержащих поисковой запрос"""
        return [post for post in self.get_posts_all() if query.lower() in post.content.lower()]


    def get_posts_by_user(self, user_name):
        """Возвращает посты определенного пользователя"""
        return [post for post in self.get_posts_all() if post.poster_name == user_name]

    def get_post_by_pk(pk):
        """Возвращает один пост по его идентификатору"""
        for post in self.get_posts_all():
            if post['pk'] == pk:
                return post

    def get_posts_in_bookmarks():
        """Возвращает посты в закладках"""
        bookmarks = Bookmarks()
        posts = list(filter(lambda x: x['pk'] in bookmarks.get_bookmarks(), get_posts_all()))
        return posts


class Comment:
    def __init__(self):
        self.post_id = post_id
        self.commener_name = commener_name
        self.comment = comment
        self.pk = pk


class CommentDAO:
    def __init__(self, file):
        self.file = file

    def get_comments_all(self):
        """Загружает файл с комментариями и преобразует из формата JSON"""
        try:
            with open(self.file, 'r', encoding='utf-8') as file:
                data = json.load(file)

            comments = [Comment(i['post_id'], i['commener_name'], i['comment'], i['pk']) for i in data]
            return data
        except FileNotFoundError:
            print(f'Файл {self.file} отсутствует')
        except JSONDecodeError:
            print(f'Файл {self.file} не удается преобразовать')

    def get_comments_by_post_id(post_id):
        """Возвращает комментарии определенного пользователя"""
        return [comment for comment in self.get_comments_all() if comment.post_id == post_id]

class Bookmarks:
    def __init__(self, file):
        self.file = file

    def get_bookmarks(self):
        """Возвращает список номеров постов в закладках"""
        try:
            with open('static/data/bookmarks.json', 'r', encoding='utf-8') as file:
                self.data = json.load(file)
            return data
        except FileNotFoundError:
            print(f'Файл {self.file} отсутствует')
        except JSONDecodeError:
            print(f'Файл {self.file} не удается преобразовать')


    def add_bookmark(self, post_pk):
        """Добавляет номер поста в закладки"""
        data = self.get_bookmarks()
        data.append(post_pk)
        data = list(set(data))
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(data, file)


    def delete_bookmark(self, post_pk):
        """Удаляет номер поста из закладок"""
        data = self.get_bookmarks()
        if post_pk in data:
            data.remove(post_pk)
            with open(self.file, 'w', encoding='utf-8') as file:
                json.dump(data, file)


def convert_tags_in_posts(posts):
    """Преобразует хэштеги в ссылки в списке постов"""
    for post in posts:
        post['content'] = convert_tags_to_links(post['content'])
    return posts










