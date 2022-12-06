import pytest
from run import app


class TestApiPosts:
    response = app.test_client().get('/api/posts')

    def test_0(self):
        assert self.response.status_code == 200, 'список не возвращается'

    def test_1(self):
        assert isinstance(self.response.json, list), 'json-файл - не список'
        assert isinstance(self.response.json[0], dict), 'элементы списка - не словари'

    @pytest.mark.parametrize(
        "test_input",
        ["poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    )
    def test_2(self, test_input):
        assert self.response.json[0][test_input], 'нет ключа poster_name'


class TestApiGetPostByPk:

    @pytest.mark.parametrize(
        "test_input",
        [1, 2, 3]
    )
    def test_0(self, test_input):
        assert app.test_client().get(f'/api/posts/{test_input}').status_code == 200, 'пост не возвращается'

    @pytest.mark.parametrize(
        "test_input",
        [1, 2, 3]
    )
    def test_1(self, test_input):
        assert isinstance(app.test_client().get(f'/api/posts/{test_input}').json, dict), 'пост - не словарь'

    @pytest.mark.parametrize(
        "test_input",
        ["poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    )
    def test_2(self, test_input):
        response = app.test_client().get(f'/api/posts/1')
        assert response.json[test_input], f'нет ключа {test_input}'

