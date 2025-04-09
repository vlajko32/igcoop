from rest_framework import serializers
from .models import Machine, MachineValue, ExpertReport, Registration, Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class MachineValueSerializer(serializers.ModelSerializer):
    depreciation_value_per_year = serializers.ReadOnlyField()
    installment_value = serializers.SerializerMethodField()
    installments_this_year = serializers.SerializerMethodField()

    class Meta:
        model = MachineValue
        fields = '__all__'

    def get_installment_value(self, obj):
        return obj.installment_value()

    def get_installments_this_year(self, obj):
        return obj.installments_this_year()

class ExpertReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpertReport
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    value_info = MachineValueSerializer(read_only=True)
    expert_reports = ExpertReportSerializer(many=True, read_only=True)
    registrations = RegistrationSerializer(many=True, read_only=True)
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Machine
        fields = '__all__'