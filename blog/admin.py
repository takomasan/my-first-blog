from django.contrib import admin
from .models import Post

# Adminページ（管理画面）上で Postモデル が見えるようにする
admin.site.register(Post)

# username:takomasan
# mail:example@mail.com
# pass:passoword
