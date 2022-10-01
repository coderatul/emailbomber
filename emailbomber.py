import os
import smtplib
from dataclasses import dataclass, field
from functools import partial

WELCOME_MSG = """  # noqa
███████╗███╗   ███╗ █████╗ ██╗██╗     ██████╗  ██████╗ ███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝████╗ ████║██╔══██╗██║██║     ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██╔════╝██╔══██╗
█████╗  ██╔████╔██║███████║██║██║     ██████╔╝██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██╔══╝  ██║╚██╔╝██║██╔══██║██║██║     ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
███████╗██║ ╚═╝ ██║██║  ██║██║███████╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
            version 1.1 : uses app password now, before it used less secure apps
                               Author : linktr.ee/coderatul
                        Before using please read "prerequisite section"
"""
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587


@dataclass
class InputArgs:
    sender: str = field(
        default_factory=partial(input, "Enter Sender's Gmail Id -> ")
    )
    password: str = field(
        default_factory=partial(input, "Enter App password -> ")
    )
    receiver: str = field(
        default_factory=partial(input, "Enter Receiver's Gmail Id -> ")
    )
    message: str = field(
        default_factory=partial(input, "Enter Your Message -> ")
    )
    count: int = field(
        default_factory=partial(input, "Enter number of mail's to be sent -> ")
    )


def run_bomber(args: InputArgs):
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    try:
        server.login(user=args.sender, password=args.password)
    except smtplib.SMTPException as exc:
        msg = exc.smtp_error.decode()  # noqa
        if os.name == "nt":
            msg = msg.replace("\n", os.linesep)
        print(msg)
        return

    for i in range(args.count):
        server.sendmail(
            from_addr=args.sender,
            to_addrs=args.receiver,
            msg=args.message,
        )
    if args.count < 2:
        print(args.count, "mail have been sent to :", args.receiver)
    else:
        print(args.count, "mails have been sent to :", args.receiver)
    server.close()


if __name__ == "__main__":
    print(WELCOME_MSG)
    run_bomber(InputArgs())
