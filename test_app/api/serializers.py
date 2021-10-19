from django.db import models
from rest_framework import serializers
from test_app.models import Note, Category, Review


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
class NoteSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Note
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    categories = NoteSerializer(many=True, read_only=True)
    # categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie_details')
    class Meta:
        model = Category
        fields = '__all__'
    


    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and Description can't be the same!!!")
    #     else:
    #         return data
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too Short')
        
    #     if value.startswith != value.upper:
    #         raise serializers.ValidationError("Use your head a name starts with an upper case")
        
    #     else:
    #         return value
        
    
    # def validate_description(self, value):
    #     if value.startswith != value.upper:
    #         raise serializers.ValidationError('Plase start with an upper case')
    #     else:
    #         return value
    # def validate_description(self, value):
    #     if value != value.startswith(value.upper()):
    #         raise serializers.ValidationError("Please start with an upper case")
    #     else:
    #         return value
# def name_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short!!')
#     else:
#         return value
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255, validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, vallidated_data):
#         return Movie.objects.create(**vallidated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description can't be the same!!!")
#         else:
#             return data
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short')
    #     else:
    #         return value