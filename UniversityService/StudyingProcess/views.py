from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import DirectionSerializer, DisciplineSerializer, StudyGroupSerializer, StudentSerializer
from .models import Direction, Discipline, StudyGroup, Student
from rest_framework import response
from rest_framework.generics import GenericAPIView
from django.http import JsonResponse
from .tasks import extract_db_and_send_email

task = 0


@api_view(['GET'])
def get_report(request) -> JsonResponse:
    global task
    task = extract_db_and_send_email.apply_async()
    return JsonResponse({'message': 'Task is queued'}, status=200)


@api_view(['GET'])
def report_status(request) -> JsonResponse:
    global task
    if task == 0:
        return JsonResponse({'massage': 'There is no task'}, status=404)
    else:
        return JsonResponse({'massage': str(task.status)}, status=200)


class DirectionApiView(GenericAPIView):
    serializer_class = DirectionSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        lst = Direction.objects.all()
        return response.Response({'direction': DirectionSerializer(lst, many=True).data})

    def post(self, request):
        serializer = DirectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'direction': serializer.data})

    def put(self, request, *args, **kwargs):
        direction_id = kwargs.get('id')
        try:
            instance = Direction.objects.get(pk=direction_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})

        serializer = DirectionSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'direction': serializer.data})

    def delete(self, request, *args, **kwargs):
        direction_id = kwargs.get('id')
        try:
            instance = Direction.objects.get(pk=direction_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})
        instance.delete()
        return response.Response({'direction': str(direction_id) + ' deleted'})


class DisciplineApiView(GenericAPIView):
    serializer_class = DisciplineSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lst = Discipline.objects.all()
        return response.Response({'discipline': DirectionSerializer(lst, many=True).data})

    def post(self, request):
        serializer = DisciplineSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'discipline': serializer.data})

    def put(self, request, *args, **kwargs):
        discipline_id = kwargs.get('id')
        try:
            instance = Discipline.objects.get(pk=discipline_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})

        serializer = DisciplineSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'discipline': serializer.data})

    def delete(self, request, *args, **kwargs):
        discipline_id = kwargs.get('id')
        try:
            instance = Discipline.objects.get(pk=discipline_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})
        instance.delete()
        return response.Response({'discipline': str(discipline_id) + ' deleted'})


class StudyGroupApiView(GenericAPIView):
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lst = StudyGroup.objects.all()
        return response.Response({'studygroup': StudyGroupSerializer(lst, many=True).data})

    def post(self, request):
        serializer = StudyGroupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'studygroup': serializer.data})

    def put(self, request, *args, **kwargs):
        studygroup_id = kwargs.get('id')
        try:
            instance = StudyGroup.objects.get(pk=studygroup_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})

        serializer = StudyGroupSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'studygroup': serializer.data})

    def delete(self, request, *args, **kwargs):
        studygroup_id = kwargs.get('id')
        try:
            instance = StudyGroup.objects.get(pk=studygroup_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})
        instance.delete()
        return response.Response({'discipline': str(studygroup_id) + ' deleted'})


class StudentApiView(GenericAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        lst = Student.objects.all()
        return response.Response({'student': StudentSerializer(lst, many=True).data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'student': serializer.data})

    def put(self, request, *args, **kwargs):
        student_id = kwargs.get('id')
        try:
            instance = Student.objects.get(pk=student_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})

        serializer = StudentSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response({'student': serializer.data})

    def delete(self, request, *args, **kwargs):
        student_id = kwargs.get('id')
        try:
            instance = Student.objects.get(pk=student_id)
        except APIException:
            return response.Response({'error': 'Object does not exist'})
        instance.delete()
        return response.Response({'student': str(student_id) + ' deleted'})
