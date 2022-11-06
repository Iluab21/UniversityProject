from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Discipline, Student, StudyGroup, Direction


class DirectionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Direction.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        return instance

    class Meta:
        model = Direction
        fields = ('name',)


class DisciplineSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    direction = serializers.PrimaryKeyRelatedField(queryset=Direction.objects.all())

    def create(self, validated_data):
        return Discipline.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.direction = validated_data.get('direction', instance.direcion)
        return instance

    class Meta:
        model = Discipline
        fields = ('name', 'direction')


class StudyGroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    direction = serializers.PrimaryKeyRelatedField(queryset=Direction.objects.all())

    def create(self, validated_data):
        return StudyGroup.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.direction = validated_data.get('direction', instance.direcion)
        return instance

    class Meta:
        model = StudyGroup
        fields = ('name', 'direction')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    studygroup = serializers.PrimaryKeyRelatedField(queryset=StudyGroup.objects.all())
    phone = serializers.CharField(validators=[Student.phoneNumberRegex,
                                                     UniqueValidator(queryset=Student.objects.all())],
                                         max_length=16)
    gender = serializers.ChoiceField(choices=Student.GENDER)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.studygroup = validated_data.get('studygroup', instance.studygroup)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        return instance

    class Meta:
        model = Student
        fields = ('name', 'studygroup', 'phone', 'gender')
