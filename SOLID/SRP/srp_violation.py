"""
単一責任原則に違反したコード例
"""


class UserManager:
    def __init__(self):
        self.users = []

    # ユーザーの管理
    def add_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users

    def remove_user(self, user):
        self.users.remove(user)

    # データの永続化
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for user in self.users:
                file.write(f"{user}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            self.users = [line.strip() for line in file.readlines()]

    # データの検証
    def validate_user(self, user):
        import re
        if not re.match(r"^[a-zA-Z0-9_]+$", user):
            raise ValueError("Invalid username")
        if user in self.users:
            raise ValueError("User already exists")
        return True

    def validate_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise ValueError("Invalid age")
        return True


    # レポート作成
    def generate_report(self):
        report = "User Report\n"
        report += "------------\n"
        for user in self.users:
            report += f"User: {user}\n"
        return report

    # 通話機能
    def call_user(self, user):
        if user not in self.users:
            raise ValueError("User not found")
        print(f"Calling {user}...")
