from email_builder import EmailBuilder


# Director
def main():
    email_message = (
        EmailBuilder()
        .add_from("bhoyar.sanket@gmail.com")
        .add_to("bhoyarsanket@gmail.com")
        .add_to("ksrandive07@gmail.com.com")
        .add_cc("kaustubhalkeri@gmail.com")
        .with_subject("The Builder Pattern Code")
        .with_body("Checkout this code on Builder Pattern")
        .add_attachment("Builder-Pattern.pdf")
        .build()
    )
    email_message.send()


if __name__ == "__main__":
    main()