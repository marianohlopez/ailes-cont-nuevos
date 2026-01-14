from db import connect_db
from extract import extract_mail_pas
from transform import gen_mails_pas
import os
from dotenv import load_dotenv

load_dotenv()

MAIL_DESTINO = os.getenv("MAIL_DESTINO")
MAIL_DESTINO_2 = os.getenv("MAIL_DESTINO_2")

def main():

  conn = connect_db()
  cursor = conn.cursor()
  #mails_pas = extract_mail_pas(cursor)
  mails_pas = [(MAIL_DESTINO,),(MAIL_DESTINO_2,)]
  gen_mails_pas(mails_pas)

if __name__ == "__main__":
  main()