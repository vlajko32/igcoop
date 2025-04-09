from datetime import date
from decimal import Decimal
from django.db import models

class Machine(models.Model):

    MACHINE_TYPE_CHOICES = [
        ('TV', 'Transport Vehicle'),
        ('PV', 'Passenger Vehicle'),
        ('CV', 'Construction Vehicle'),
        ('OT', 'Other'),
    ]
    name = models.CharField(max_length=255)
    internal_number = models.CharField(max_length=100, unique=True)
    inventory_number = models.CharField(max_length=100, unique=True)
    account_number = models.CharField(max_length=100, unique=True)

    machine_type = models.CharField(
        max_length=2,
        choices=MACHINE_TYPE_CHOICES,
        default='OT',
    )

    location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='machines')

    status = models.CharField(
        max_length=50,
        choices=[
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('under_maintenance', 'Under Maintenance'),
        ],
        default='active',
    )

    def __str__(self):
        return f"{self.name} ({self.internal_number})"
    
class MachineValue(models.Model):
    machine = models.OneToOneField("Machine", on_delete=models.CASCADE, related_name="value_info")

    purchase_value = models.DecimalField(max_digits=12, decimal_places=2)
    purchase_date = models.DateField()

    number_of_installments = models.PositiveIntegerField()
    annual_depreciation_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentage per year")

    @property
    def depreciation_value_per_year(self):
        return (self.purchase_value * self.annual_depreciation_rate / 100).quantize(Decimal('0.01'))

    def installment_value(self):
        if self.number_of_installments:
            return (self.purchase_value / self.number_of_installments).quantize(Decimal('0.01'))
        return Decimal('0.00')

    def installments_this_year(self):
        """
        Return number of installments to be paid this year.
        You can expand logic based on purchase_date.
        """
        # Let's assume one installment per month starting from purchase_date
        today = date.today()
        months_passed = (today.year - self.purchase_date.year) * 12 + (today.month - self.purchase_date.month)
        total_months = self.number_of_installments
        months_left = max(0, total_months - months_passed)

        months_this_year = min(12, months_left)
        return months_this_year    

class Location(models.Model):
    division_choices = [
        ('BG', 'Belgrade'),
        ('KG', 'Kragujevac'),
        ('E', 'Eastern Division'),
    ]
    division = models.CharField(max_length=2, choices=division_choices)
    location_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.get_division_display()} - {self.location_number}"

class ExpertReport(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='expert_reports')
    valid_from = models.DateField()
    valid_to = models.DateField()
    report_number = models.CharField(max_length=100, unique=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"Expert Report {self.report_number} for {self.machine.name}"

class Registration(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='registrations')
    registration_number = models.CharField(max_length=100, unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Registration {self.registration_number} for {self.machine.name}"
