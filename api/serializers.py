from rest_framework import serializers
from .models import Blog

# ==================================================
# serializerの役割　(Djangoをやっている人はFormのイメージ)
# RESTでやり取りするデータの入出力を扱う。
# 例えば、複雑な入力値をモデルに合わせてバリデーションしてレコードに伝える(GETメソッド)
#       Model(レコード)を適切な形式にフォーマットする(POSTメソッド、PUTメソッド)
#
# Serializer：単純なシリアライザ
# ModelSerializer：Modelからシリアライザを作成する。
# ListSerializer：複数レコードの登録、更新を行う際のシリアライザ
# 参考：https://note.crohaco.net/2018/django-rest-framework-serializer/
# ==================================================

# ModelSerializerを継承する事で、CRUD処理が行える。
class BlogSerializer(serializers.ModelSerializer):
    # 登録日時のフォーマット指定と、read_only=Trueをつける事でGETメソッド
    # ではレスポンスを返すがPOST、PUTなど更新時は受け取らない。
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')