from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    is_author = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "last_updated",
            "content",
            "thumbnail",
            "is_author"
        )

    def get_is_author(self, obj):
        request = self.context["request"]
        if request.user:
            return request.user == obj.user
        return False


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "thumbnail",
        )


class PostUpdateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
    thumbnail = serializers.ImageField(required=False)

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "thumbnail",
        )
