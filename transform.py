import os
from dotenv import load_dotenv
import yagmail
from assets.mail import content_mail

load_dotenv()

MAIL_AUTOR = os.getenv("MAIL_AUTOR")
APP_GMAIL_PASS = os.getenv("APP_GMAIL_PASS")

def send_mail(mail):
  try:
    yag = yagmail.SMTP(MAIL_AUTOR, APP_GMAIL_PASS)
    yag.send(
      to=mail,
      subject="Información área contable Ailes - NO CONTESTAR",
      contents=content_mail,
    )
    print(f"📧 Mail enviado a {mail}")
  except Exception as e:
    print(f"❌ Error enviando mail a {mail}: {e}")

def gen_mails_pas(mails):

  if not mails:
    print("No hubo PAs nuevos asignados esta semana")
    return

  for (mail,) in mails:
    if not mail:
      print("⚠️ Mail nulo detectado, se omite")
      continue
    send_mail(mail)