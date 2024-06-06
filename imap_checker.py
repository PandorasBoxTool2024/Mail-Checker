import imaplib

class Checker:
    def __init__(self, imap_server, imap_port=993):
        self.imap_server = imap_server
        self.imap_port = imap_port

    def check_credentials(self, email:str, password:str) -> bool:
        try:
            with imaplib.IMAP4_SSL(self.imap_server, self.imap_port) as imap_connection:
                imap_connection.login(email, password)
        except imaplib.IMAP4.error as error:
            print(f"IMAP Error: {error}")
            return False
        else:
            return True
