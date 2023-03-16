import logging
import logging.handlers


# debe configura la cuenta de gmail, que va enviar con la pass
#y modimficar Acceso de apps menos seguras y permitir
#No puede usar la cuenta de Gmail para enviar correos electrónicos con el módulo
#  de logging. Es porque Google requiere una conexión TLS y el módulo de registro
#  no lo admite.

#Solución
#Para usar gmail, debe extender la clase logging.handlers.SMTPHandler y anular 
# el método SMTPHandler.emit (). Aquí está el código fuente.

class TlsSMTPHandler(logging.handlers.SMTPHandler):
    def emit(self, record):
        """
        Emite un registro.

        Formatee el registro y envíelo a los destinatarios especificados.
        """
        try:
            import smtplib            
            try:
                from email.utils import formatdate
            except ImportError:
                formatdate = self.date_time
            port = self.mailport
            if not port:
                port = smtplib.SMTP_PORT
            smtp = smtplib.SMTP(self.mailhost, port)
            msg = self.format(record)
            msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\nDate: %s\r\n\r\n%s" % (self.fromaddr,",".join(self.toaddrs),self.getSubject(record),formatdate(), msg)
            if self.username:
                smtp.ehlo() 
                smtp.starttls() 
                smtp.ehlo() 
                smtp.login(self.username, self.password)
            smtp.sendmail(self.fromaddr, self.toaddrs, msg)
            
            smtp.quit()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#gm = TlsSMTPHandler(("smtp.gmail.com", 587), ' no se', ['hacia@gmail.com'], 'Asunto!', ('desde@gmail.com', 'pass-desde'))
gm = TlsSMTPHandler(("smtp.gmail.com", 587), 'mail.google.com', ['arbbar20dev@gmail.com'], 'Error De la App', ('miemail@gmail.com', 'tupass-miemail'))
gm.setLevel(logging.INFO)
gm.setFormatter(formatter)
logger.addHandler(gm)
logger.error("Ocurrio un Error")
logger.warning("Esto es critico")
logger.critical('Esto explotara')