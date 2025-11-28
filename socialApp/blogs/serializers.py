from rest_framework import serializers
from .models import Blog, comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'
        
        
class blogSerializer(serializers.ModelSerializer):
    comment = CommentSerializer(many=True, read_only =True)
    class Meta:
        model = Blog
        fields = '__all__'