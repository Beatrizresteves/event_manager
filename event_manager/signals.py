from django.db.models.signals import post_save
from django.dispatch import receiver
from events.models import Event, Participant
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Event)
def notify_participants_on_event_update(sender, instance, created, **kwargs):
    print(f"[Signal] Evento salvo: {instance.title} (created={created})")
    if created:
        return

    participants = Participant.objects.filter(event=instance)
    emails = [p.user.email for p in participants if p.user.email]

    if emails:
        subject = f'Atualização no evento: {instance.title}'
        message = f'O evento "{instance.title}" foi atualizado. Confira as novidades.'
        from_email = settings.DEFAULT_FROM_EMAIL

        send_mail(subject, message, from_email, emails)
