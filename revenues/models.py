from django.db import models
from django.utils.translation import gettext_lazy as _

class RevenueEntry(models.Model):
    class TimeLossReasons(models.TextChoices):
        NO_OPERATOR = "NO_OPERATOR", _("No operator")
        WAITING_FOR_WORK = "WAITING_FOR_WORK", _("Waiting for work")
        MACHINE_RELOCATION = "MACHINE_RELOCATION", _("Machine relocation")
        REGULAR_SERVICE = "REGULAR_SERVICE", _("Regular service")
        FAILURE = "FAILURE", _("Breakdown / Failure")
        OTHER_MACHINE_STOPPAGE = "OTHER_MACHINE_STOPPAGE", _("Stopped due to another machine")
        WEATHER_CONDITIONS = "WEATHER_CONDITIONS", _("Weather conditions")

    date = models.DateField()
    expense_location = models.CharField(max_length=255)
    internal_number = models.CharField(max_length=50, unique=True)
    machine_name = models.CharField(max_length=255)

    supervisor = models.CharField(max_length=255)
    operator_driver = models.CharField(max_length=255)

    time_losses = models.CharField(
        max_length=50,
        choices=TimeLossReasons.choices,
        null=True,
        blank=True
    )

    initial_state = models.DecimalField(max_digits=10, decimal_places=2)
    final_state = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.date} - {self.machine_name} ({self.internal_number})"