from flask import request, jsonify
from flask_smorest import Blueprint, abort

def create_post_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description='posts api', url_prefix='/posts')

    @posts_blp.route('/', methods=['GET', 'POST'])
    def posts():
        cursor = mysql.connection.cursor()

        # 게시글 조회
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []
            for post in posts:
                post_list.append({
                    'id': post[0],
                    'title': post[1],
                    'content': post[2]
                })

            return jsonify(post_list)

        # 게시글 생성
        elif request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message='Title or Content cannot be empty')

            sql = 'INSERT INTO posts(title, content) VALUES(%s, %s)'
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({'msg': 'Successfully created post data'}), 201

    # 특정 게시글 조회
    # 게시글 수정 및 삭제
    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id):
        cursor = mysql.connection.cursor()

        # MySQLdb의 cursor.execute()는 %s 플레이스홀더와 튜플 파라미터를 지원
        # 기존 강사님이 썼던 f-string 방식은 오류나서 전면 수정함.

        # 공통: 게시글 존재 확인
        sql_select = "SELECT * FROM posts WHERE id = %s"  # %s로 변경
        cursor.execute(sql_select, (id,))  # 파라미터 튜플
        post = cursor.fetchone()
        if not post:
            abort(404, 'Not found post')

        if request.method == 'GET':
            return jsonify({
                'id': post[0],
                'title': post[1],
                'content': post[2]
            })

        elif request.method == 'PUT':
            # data = request.json
            # title = data['title']
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, 'Not found title or content')

            sql_update = "UPDATE posts SET title = %s, content = %s WHERE id = %s"  # %s 플레이스홀더 + 따옴표 자동 처리
            cursor.execute(sql_update, (title, content, id))  # 파라미터 튜플
            mysql.connection.commit()

            return jsonify({'msg': 'Successfully updated title & content'})

        elif request.method == 'DELETE':
            sql = f'DELETE FROM posts WHERE id={id}'
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({'msg': 'Successfully deleted post'})

    return posts_blp
