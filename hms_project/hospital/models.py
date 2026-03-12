from django.db import models
from django.contrib.auth.models import User
from calendar_service import create_calendar_event
from datetime import datetime
import requests


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username


class Availability(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.doctor} - {self.date} {self.start_time}"


class Booking(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    availability = models.OneToOneField(Availability, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        # Run logic only when creating a new booking
        if not self.pk:

            # Mark slot as booked
            self.availability.is_booked = True
            self.availability.save(update_fields=['is_booked'])

            # Prepare calendar event time
            start = datetime.combine(self.availability.date, self.availability.start_time)
            end = datetime.combine(self.availability.date, self.availability.end_time)

            # Create Google Calendar event
            create_calendar_event(
                f"Appointment: {self.patient.user.username} with Dr {self.availability.doctor.user.username}",
                start,
                end
            )

            # Send email via Serverless Lambda API
            try:
                requests.post(
                    "http://localhost:3000/send-email",
                    json={
                        "action": "BOOKING_CONFIRMATION",
                        "email": self.patient.user.email
                    }
                )
            except Exception as e:
                print("Email service error:", e)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient} booked {self.availability}"