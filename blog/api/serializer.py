from rest_framework import serializers
from blog.models import Article
from persiantools.jdatetime import JalaliDate
from persiantools import characters, digits
from django.utils.timezone import now

class ArticleSerializer(serializers.ModelSerializer):
    publisher = serializers.SlugRelatedField(read_only=True , slug_field='username')
    day_ago = serializers.SerializerMethodField()
    class Meta:
        model = Article
        fields = ('__all__')
        read_only_fields = ('data_added' , 'is_public')
    
    def get_day_ago(self , obj):
        return f"{(now().date() - obj.date_added).days} days ago"