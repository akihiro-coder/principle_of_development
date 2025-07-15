# 疎結合な例の導入（まだ完全ではない）
# 疎結合なコードを目指すために、認証の機能と具体的な実装を分離することを考える。


from abc import ABC, abstractmethod


# 認証機能の契約を定義するインターフェース
class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        pass


# 「データベース認証」の具体的な実装
class DatabaseUserAuthenticator(Authenticator):
    def authenticate(self, username: str, password: str) -> bool:
        # ここで実際はデータベースからユーザー情報を取得して認証
        print(f"Authenticating {username} against the database...")
        return username == "admin" and password == "password" # 仮の認証ロジック


# 「LDAP認証」の具体的な実装 (将来的に追加される可能性がある)
class LdapAuthenticator(Authenticator):
    def authenticate(self, username: str, password: str) -> bool:
        # ここで実際はLDAPサーバーに接続して認証
        print(f"Authenticating {username} against LDAP...")
        return username == "ldap_user" and password == "ldap_password" # 仮の認証ロジック



# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


# この関数が具体的な認証の実装を知らないようにしたい
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # ここでまだ、どの認証方式を使うかを決定する必要がある。
    # authenticator = DatabaseUserAuthenticator() # ここがまだ疎結合でない部分

    # 理想的には、ここに外部から Authenticator のインスタンスが「渡されてくる形」にしたい。
    # 仮に、今は、直接インスタンスを渡す方法がないとすると、、
    # TODO: ここに認証ロジックを注入する方法が必要
    authenticator = None # 仮に、Noneを設定しておく
    # !!! login関数は Authenticator という「認証できるもの」さえあれば良く、それがデータベース認証なのか、LDAP認証なのかは関知しない。 !!!
    # !!! これが、「疎結合」の考え方。そして、この「具体を気にせず、抽象に依存する」という考え方が、「依存性逆転の法則」や「依存性の注入」につながっていく。 !!!


    if authenticator and authenticator.authenticate(username, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


if __name__ == '__main__':
    # アプリケーション起動時に、使用する Authenticator を設定する場所が必要になる
    # 現状の、app.py だけでは、具体的にどの認証方式を使うか決められない。
    pass
