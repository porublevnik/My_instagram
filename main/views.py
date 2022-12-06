from flask import Blueprint, render_template, request, redirect
from utils.utils import *

# logging.basicConfig(filename="basic.log", level=logging.INFO)

main = Blueprint('main', __name__, template_folder='templates', url_prefix='/')


@main.route('/')
def page_index():
    """Главная страница"""
    posts = get_posts_all()
    posts = convert_tags_in_posts(posts)
    posts = cut_posts(posts)
    bookmarks = get_bookmarks()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@main.route('/post/<int:postid>')
def page_post(postid):
    """Отдельный пост по индексу"""
    post, comments = get_post_by_pk(postid), get_comments_by_post_id(postid)
    post['content'] = convert_tags_to_links(post['content'])
    bookmarks = get_bookmarks()
    return render_template('post.html', postid=postid, post=post, bookmarks=bookmarks, comments=comments)


@main.route('/search', methods=['GET', 'POST'])
def page_post_search():
    """Страница с результатом поиска"""
    query = request.args.get('s')
    posts = search_for_posts(query)
    posts = convert_tags_in_posts(posts)
    posts = cut_posts(posts)
    bookmarks = get_bookmarks()
    return render_template('search.html', s=query, posts=posts, bookmarks=bookmarks, number_of_posts=len(posts))


@main.route('/users/<username>')
def page_user_posts(username):
    """Страница с постами выбранного пользователя"""
    posts = get_posts_by_user(username)
    posts = cut_posts(posts)
    bookmarks = get_bookmarks()
    return render_template('user-feed.html', bookmarks=bookmarks, posts=posts)


@main.route('/tag/<tag>')
def page_post_search_by_tag(tag):
    """Страница с постами, содержащими тег"""
    query = f'#{tag}'
    posts = search_for_posts(query)
    posts = cut_posts(posts)
    bookmarks = get_bookmarks()
    return render_template('tag.html', s=query, posts=posts, bookmarks=bookmarks, number_of_posts=len(posts))


@main.route('/bookmarks/add/<int:post_id>')
def page_add_bookmark(post_id):
    """Добавление закладки"""
    add_bookmark(post_id)
    return redirect("/", code=302)


@main.route('/bookmarks/del/<int:post_id>')
def page_delete_bookmark(post_id):
    """Удаление закладки"""
    delete_bookmark(post_id)
    return redirect("/", code=302)



@main.route('/bookmarks')
def page_bookmarks():
    """Страница с постами в закладках"""
    posts = load_posts_in_bookmarks()
    posts = convert_tags_in_posts(posts)
    posts = cut_posts(posts)
    bookmarks = get_bookmarks()
    return render_template('bookmarks.html', posts=posts, bookmarks=bookmarks)