from django.core.mail import EmailMessage

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data["subject"],
            body=data['body'],
            to=["sylvaejike@gmail.com", "millyjohnzineth24@gmail.com"]# "millyjohnzineth24@gmail.com"]#"francisokatta1@gmail.com"]
        )
        email.send()
