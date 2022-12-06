import logging

from flask import Blueprint, jsonify
from utils.utils import *
from logging_settings import create_logger


endpoints = Blueprint('api', __name__, template_folder='templates', url_prefix='/api')
logging.basicConfig(level=logging.INFO)


@endpoints.route('/posts')
def page_api_posts():
    create_logger('logger_api_posts').info("Запрос /api/posts")
    return jsonify(get_posts_all())


@endpoints.route('/posts/<int:post_id>')
def page_api_post_by_id(post_id):
    create_logger('logger_api_post_by_id').info(f"Запрос /api/posts/{post_id}")
    return jsonify(get_post_by_pk(post_id))
