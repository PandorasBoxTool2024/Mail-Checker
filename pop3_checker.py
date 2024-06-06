import poplib
from email.parser import Parser

class Checker:
    def __init__(self, pop3_server, pop3_port=995):
        self.pop3_server = pop3_server
        self.pop3_port = pop3_port

    def check_credentials(self, email:str, password:str) -> bool:
        try:
            pop3_connection = poplib.POP3_SSL(self.pop3_server, self.pop3_port)
            pop3_connection.user(email)
            pop3_connection.pass_(password)
        except poplib.error_proto as error:
            print(f"POP3 Error: {error}")
            return False
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return False
        else:
            pop3_connection.quit()
            return True
