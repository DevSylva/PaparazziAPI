from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data["subject"],
            body=data['body'],
            to=["eletuoalexander2019@gmail.com", "sylvaejike@gmail.com"]
        )
        email.send()
