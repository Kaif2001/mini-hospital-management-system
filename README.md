# Mini Hospital Management System

A simple Hospital Management System built using Django, Google Calendar API, and a Serverless Email Notification Service using the Serverless Framework.

## Features

Authentication
- Doctor and Patient users
- Secure password storage using Django authentication

Doctor Availability
- Doctors can create available time slots
- Slots include date and time
- Only future and unbooked slots are visible to patients

Appointment Booking
- Patients can view doctors
- Patients can book available slots
- Once booked, the slot is locked and cannot be booked again

Google Calendar Integration
- Automatically creates an event when a booking is made
- Event is added to Google Calendar

Email Notification Service
- Implemented using Serverless Framework
- Sends booking confirmation emails
- Runs locally using serverless-offline

## Tech Stack

Backend Framework
Django (Python)

Database
SQLite (PostgreSQL-ready architecture)

Serverless Email Service
Serverless Framework  
Python  
serverless-offline

APIs
Google Calendar API

Tools
Git  
GitHub

## Project Structure

mini-hospital-management-system
│
├── hms_project
│   ├── hospital
│   ├── hms_project
│   ├── calendar_service.py
│   └── manage.py
│
└── email_service
    └── email-service
        ├── handler.py
        └── serverless.yml

## Running the Project

Run Django Server

cd hms_project  
python manage.py runserver

Access admin panel

http://127.0.0.1:8000/admin

Run Email Service

cd email_service/email-service  
serverless offline

Email endpoint

http://localhost:3000/send-email

## Demo Features

The demo showcases

- Creating doctors and patients
- Doctor availability management
- Patient booking appointments
- Automatic Google Calendar event creation
- Email confirmation for bookings
- Serverless email service working locally

## Author

Mohammed Kaif  
GitHub: https://github.com/Kaif2001
