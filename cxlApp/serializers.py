from rest_framework import serializers
from .models import StudentDetail, StudentMark, StudDetail

class StudentMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentMark
        fields = '__all__'

class StudentDetailSerializer(serializers.ModelSerializer):
    student_marks = StudentMarkSerializer(many=True, read_only=True)

    class Meta:
        model = StudentDetail
        fields = '__all__'
        
    def to_representation(self, instance):
        stu_mark_seri=StudentMarkSerializer(instance.student_marks.all(), many=True).data
        result= {
            'sid': instance.sid,
            'sno': instance.sno,
            'sname': instance.sname,
            'sclass': instance.sclass,
            'saddress': instance.saddress,
            
        }
        for mark in stu_mark_seri:
            result.update(mark)
        return result
    
class StudDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudDetail
        fields = '__all__'
