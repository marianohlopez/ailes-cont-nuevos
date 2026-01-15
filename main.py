from db import connect_db
from extract import extract_mail_pas
from transform import gen_mails_pas

def main():

  conn = connect_db()
  cursor = conn.cursor()
  mails_pas = extract_mail_pas(cursor)
  gen_mails_pas(mails_pas)

if __name__ == "__main__":
  main()