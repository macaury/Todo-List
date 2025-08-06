import smtplib
import ssl

from dotenv import load_dotenv
import os


mail = os.getenv('SENDERMAIL')
password = os.getenv('SENDERPASSWORD')




try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 587, context=context, timeout=60) as server:
        server.login(mail, password)
        server.sendmail(
            "carvalhomacaury@gmail.com",
            ["seu_email_pessoal@exemplo.com"],
            "Subject: Teste SMTP\n\nFuncionou!"
        )
    print("✅ Email enviado com sucesso!")
except Exception as e:
    print(f"❌ Erro: {e}")