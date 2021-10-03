from rest_framework import serializers

class NationalIDInfoSerializer(serializers.Serializer):
	birthday = serializers.DateField()
	govermant_code = serializers.CharField()
	gender = serializers.CharField()
	unique_number_per_governorate_day = serializers.CharField()
