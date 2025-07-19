# 低凝集度の例：複数の責任が混在

class UserManager:

    def save_user(self, user_data):
        # ユーザーデータの保存
        print("データベースに保存")

    def send_welcome_email(self, email):
        # ウェルカムメールの送信
        print(f"ウェルカムメールを {email} に送信")

    def calculate_tax(self, amount):
        # 税金計算（ユーザー管理と無関係)　
        return amount * 0.1  # 仮の税率計算

    def format_phone_number(self, phone_number):
        # 電話番号のフォーマット（ユーザー管理と無関係）
        return phone_number.replace("-", "")