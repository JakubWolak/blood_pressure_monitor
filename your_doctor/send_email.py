from django.core.mail import EmailMessage
from easy_pdf.rendering import render_to_pdf


def send_email(obj, user, userdata, doctordata, measurements) -> bool:
    """sends email from user's email to doctor, message contains all user's measurements and an attachment - PDF file

    Args:
        obj (SendDataToDoctor): [object representing view]
        user (UserData): [user's data]
        doctor (DoctorData): [doctor's data]
        measurements (Measurement): [all measurements belongs to logged user]
    """
    topic = "Pomiary ciśnienia krwi"
    message = "Pomiary ciśnienia krwi dla użytkownika {name} {surname}".format(
        name=userdata.name, surname=userdata.surname
    )

    context = {}
    context["user"] = userdata
    context["measurements"] = measurements

    try:
        attachment = render_to_pdf("generate_files/PDF_template.html", context)
    except Exception as e:
        print(e)
        print("Błąd przy tworzeniu załącznika")
        attachment = None
        return False

    email = EmailMessage(topic, message, user.email, [doctordata.email])
    email.attach("pomiary.pdf", attachment)
    email.send()
    return True

