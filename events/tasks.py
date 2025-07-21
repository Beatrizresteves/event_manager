from celery import shared_task
from django.core.mail import send_mail

@shared_task
def enviar_email_inscricao_confirmada(email, nome_evento):
    assunto = f'Confirmação de inscrição no evento {nome_evento}'
    mensagem = f'Sua inscrição no evento "{nome_evento}" foi confirmada. Obrigado por participar!'
    send_mail(
        assunto,
        mensagem,
        'no-reply@events.com',
        [email],
        fail_silently=False,
    )
