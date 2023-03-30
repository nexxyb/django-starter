from celery import shared_task
from django.core.mail import send_mail
import logging
import smtplib
from email.message import EmailMessage
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

