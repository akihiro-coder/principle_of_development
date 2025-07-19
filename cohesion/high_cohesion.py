# 高凝集度の例：関連する責任のみを持つクラス

class UserRepository:
    # ユーザーデータの永続化のみに責任を持つ
    def save(self, user_data):
        # ユーザーデータの保存
        print("データベースに保存:", user_data)

    def find_by_id(self, user_id):
        print("ユーザーをIDで検索:", user_id)

    def delete(self, user_id):
        print("ユーザーを削除:", user_id)


class EmailService:
    # メール送信のみに責任を持つ
    def send_welcome_email(self, email):
        # ウェルカムメールの送信
        print(f"ウェルカムメールを {email} に送信")

    def send_notification(self, email, subject, body):
        print(f"通知メールを {email} に送信: {subject}\n{body}")


class TaxCalculator:
    # 税金計算のみに責任を持つ
    def calculate_tax(self, amount):
        # 税金計算
        return amount * 0.1  # 仮の税率計算

class PhoneFormatter:
    # 電話番号フォーマットのみに責任を持つ
    def format_phone_number(self, phone_number):
        # 電話番号のフォーマット
        return phone_number.replace("-", "")


"""
高凝集のメリット
- クラスの目的が明確で理解しやすい
- 変更時の影響範囲が限定される
- 再利用しやすい
- テストが書きやすい
"""

