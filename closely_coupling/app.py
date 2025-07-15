from flask import Flask, request, jsonify

app = Flask(__name__)


# データベースに直接依存するクラス (密結合)
class DatabaseUserAuthenticator:
    def authenticate(self, username, password):
        # ここで直接データベースに接続し、ユーザーを検索するロジック
        if username == "admin" and password == "password":  # 仮の認証ロジック（実際はDB問い合わせ）
            return True
        return False


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    authenticator = DatabaseUserAuthenticator()  # ここで具体的な実装を直接生成
    if authenticator.authenticate(username, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    app.run(debug=True)

"""
このコードの問題点
- 認証方式をデータベース認証から、LDAP認証やOAuth認証などに変更したい場合、
  DatabaseUserAuthenticatorの中身だけでなく、login関数のauthenticator=DatabaseUserAuthenticator()の部分も変更する必要がある。

- login関数をテストするときに、実際のデータベースへの接続が必要になる。
  テストごとにデータベースの状態を管理するのは非常に手間がかかる。
"""
