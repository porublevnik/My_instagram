import pytest
from utils.utils import *


class TestGetPostsAll:

    def test_0(self):
        assert get_posts_all(), 'Ошибка, файл  posts.json не загружен или пустой'


class TestGetPostsByUser:
    @pytest.mark.parametrize(
        "test_input",
        ["leo", "johnny", "hank"]
    )
    def test_0(self, test_input):
        assert get_posts_by_user(test_input), f'Ошибка, нет постов пользователя "{test_input}"'

    @pytest.mark.parametrize(
        "test_input, excepted",
        [("poster_avatar", str), ("pic", str), ("content", str), ("views_count", int), ("likes_count", int),
         ("pk", int)]
    )
    def test_1(self, test_input, excepted):
        assert get_posts_by_user('leo'), 'Ошибка, нет постов пользователя "leo"'
        assert isinstance(get_posts_by_user('leo')[0][test_input], excepted), f'ключ {test_input} - не {excepted}'


class TestGetCommentsByPostID:
    @pytest.mark.parametrize(
        "test_input",
        [1, 2, 3]
    )
    def test_0(self, test_input):
        assert get_comments_by_post_id(test_input), f'Ошибка, нет поста с номером {test_input}'

    @pytest.mark.parametrize(
        "test_input",
        [1, 2, 3]
    )
    def test_1(self, test_input):
        assert len(get_comments_by_post_id(test_input)), f'Ошибка, пост с номером {test_input} не имеет комментариев'

    @pytest.mark.parametrize(
        "test_input, excepted",
        [("post_id", int), ("commenter_name", str), ("comment", str), ("pk", int)]
    )
    def test_2(self, test_input, excepted):
        assert isinstance(get_comments_by_post_id(1)[0][test_input], excepted), f'ключ {test_input} - не {excepted}'


class TestSearchForPosts:
    @pytest.mark.parametrize(
        "test_input",
        ["ед", "ага", "ВСЕ", "елки"]
    )
    def test_0(self, test_input):
        assert len(search_for_posts(test_input)) > 0, f'Ошибка, нет постов, содержащих {test_input}'


class TestGetPostByPK:
    @pytest.mark.parametrize(
        "test_input, excepted",
        [(1, "Ага, опять еда!"), (2, "Вышел погулять днем"), (3, 'Смотрите-ка – ржавые елки!')]
    )
    def test_0(self, test_input, excepted):
        post = get_post_by_pk(test_input)
        assert excepted in get_post_by_pk(test_input)['content'], f'Ошибка, по pk {test_input} возвращен не тот пост'
