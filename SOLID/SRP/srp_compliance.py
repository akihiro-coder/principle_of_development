"""
単一責任の原則遵守の例
各クラスが単一の責任のみを持つように設計する
"""

from typing import List, Dict, Optional
from abc import ABC, abstractmethod


# ユーザーデータの管理のみ
class User:
    """ユーザーエンティティ - ユーザーデータの表現のみ"""

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age

    def to_dict(self) -> Dict:
        return {"username": self.username, "age": self.age}

    @classmethod
    def from_dict(cls, data: Dict) -> 'User':
        return cls(username=data['username'], age=data['age'])


class UserRepository:
    """ユーザーデータの管理のみ - CRUD操作"""

    def __init__(self):
        self._users: List[User] = []
        self._next_id = 1

    def add(self, name: str, email: str, age: int) -> User:
        """ユーザーを追加"""
        user = User(self._next_id, name, email, age)
        self._users.append(user)
        self._next_id += 1
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        """IDでユーザーを取得"""
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def get_all(self) -> List[User]:
        """全ユーザーを取得"""
        return self._users.copy()

    def update(self, user: User) -> bool:
        """ユーザーを更新"""
        for i, existing_user in enumerate(self._users):
            if existing_user.id == user.id:
                self._users[i] = user
                return True
        return False

    def delete(self, user_id: int) -> bool:
        """ユーザーを削除"""
        for i, user in enumerate(self._users):
            if user.id == user_id:
                del self._users[i]
                return True
        return False


# 責任2: データの永続化のみ
class UserPersistence:
    """ユーザーデータの永続化のみ"""

    @staticmethod
    def save_to_file(users: List[User], filename: str):
        """ファイルに保存"""
        import json
        data = [user.to_dict() for user in users]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"ユーザーデータを {filename} に保存しました")

    @staticmethod
    def load_from_file(filename: str) -> List[User]:
        """ファイルから読み込み"""
        import json
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            users = [User.from_dict(user_data) for user_data in data]
            print(f"ユーザーデータを {filename} から読み込みました")
            return users
        except FileNotFoundError:
            print(f"ファイル {filename} が見つかりません")
            return []


# 責任3: データの検証のみ
class UserValidator:
    """ユーザーデータの検証のみ"""

    @staticmethod
    def validate_email(email: str) -> bool:
        """メールアドレスの形式チェック"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_age(age: int) -> bool:
        """年齢の妥当性チェック"""
        return 0 <= age <= 150

    @staticmethod
    def validate_name(name: str) -> bool:
        """名前の妥当性チェック"""
        return len(name.strip()) > 0

    @staticmethod
    def validate_user_data(name: str, email: str, age: int) -> List[str]:
        """
        ユーザーデータの総合検証
        """
        errors = []

        if not UserValidator.validate_name(name):
            errors.append("名前が無効です")

        if not UserValidator.validate_email(email):
            errors.append("メールアドレスの形式が無効です")

        if not UserValidator.validate_age(age):
            errors.append("年齢は0-150の範囲で入力してください")

        return errors



# 責任4: レポート生成のみ
class UserReportGenerator:
    """ユーザーレポートの生成のみ"""

    @staticmethod
    def generate_summary_report(users: List[User]) -> str:
        """サマリーレポートを生成"""
        if not users:
            return "ユーザーが登録されていません"

        report = "=== ユーザーサマリーレポート ===\n"
        total_age = sum(user.age for user in users)
        avg_age = total_age / len(users)

        report += f"総ユーザー数: {len(users)}\n"
        report += f"平均年齢: {avg_age:.1f}歳\n"

        return report

    @staticmethod
    def generate_detailed_report(users: List[User]) -> str:
        """詳細レポートを生成"""
        if not users:
            return "ユーザーが登録されていません"

        report = "=== ユーザー詳細レポート ===\n"
        for user in users:
            report += f"ID: {user.id}, 名前: {user.name}, "
            report += f"メール: {user.email}, 年齢: {user.age}\n"

        return report



# 責任5: 通知機能のみ
class UserNotificationService:
    """ユーザー通知機能のみ"""

    @staticmethod
    def send_welcome_email(user: User):
        """ウェルカムメール送信"""
        print(f"ウェルカムメールを {user.email} に送信しました")
        print(f"件名: {user.name}さん、ようこそ！")

    @staticmethod
    def send_notification(user: User, subject: str, message: str):
        """一般的な通知送信"""
        print(f"通知メールを {user.email} に送信しました")
        print(f"件名: {subject}")
        print(f"内容: {message}")



# 全体を強調させるサービスクラス
class UserService:
    """各責任を組合せてビジネス機能を提供"""

    def __init__(self):
        self._repository = UserRepository()
        self._persistence = UserPersistence()
        self._validator = UserValidator()
        self._report_generator = UserReportGenerator()
        self._notification_service = UserNotificationService()


    def create_user(self, name: str, email: str, age: int) -> Optional[User]:
        """ユーザーを作成し、検証と保存を行う"""
        errors = self._validator.validate_user_data(name, email, age)
        if errors:
            print("ユーザーデータの検証エラー:", errors)
            return None

        user = self._repository.add(name, email, age)
        self._persistence.save_to_file(self._repository.get_all(), 'users.json')
        self._notification_service.send_welcome_email(user)
        return user


    def get_user_report(self) -> str:
        """ユーザーレポートを取得"""
        users = self._repository.get_all()
        summary_report = self._report_generator.generate_summary_report(users)
        detailed_report = self._report_generator.generate_detailed_report(users)
        return summary_report + "\n\n" + detailed_report


    def save_users(self, filename: str):
        """ユーザーデータをファイルに保存"""
        self._persistence.save_to_file(self._repository.get_all(), filename)


    def load_users(self, filename: str):
        """ファイルからユーザーデータを読み込み"""
        users = self._persistence.load_from_file(filename)
        for user in users:
            self._repository.add(user.username, user.email, user.age)
