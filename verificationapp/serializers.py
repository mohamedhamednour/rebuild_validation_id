from rest_framework import serializers
from .validation import NationalIdValidator  

class NationalIdSerializer(serializers.Serializer):
    national_id = serializers.CharField(max_length=14)
    birthdate = serializers.DateField(read_only=True)

    def validate_national_id(self, value : str) -> str:
       
        try:
            validator = NationalIdValidator(value).build()
        except ValueError as e:
            raise serializers.ValidationError(str(e))

        self._birthdate = validator.birthdate

        return value

    def create(self, validated_data : dict) -> dict:
     
        validated_data["birthdate"] = getattr(self, "_birthdate", None)
        return validated_data 

 