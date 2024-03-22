import smtplib
import pyodbc
import sqlalchemy as sa
import CommonConnections
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email(to_email, subject, body, from_email=None, attachments=None):
    """
    Sends an email with optional attachments.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Email subject.
        body (str): Email body content.
        from_email (str): Sender's email address.  Defaults to the user's email address.
        attachments (list, optional): List of file paths for attachments. Defaults to None.

    Returns:
        str: Status message indicating success or failure.
    """
    try:
        # Create a MIME object for the email
        msg = MIMEMultipart()
        if from_email:
            msg['From'] = from_email
        else:
            msg['From'] = f"{CommonConnections.sysUser511}@ abbott.com"
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body of the email
        msg.attach(MIMEText(body, 'plain'))

        # Attach optional files
        if attachments:
            for attachment in attachments:
                with open(attachment, 'rb') as file:
                    part = MIMEApplication(file.read())
                    part.add_header('Content-Disposition', f'attachment; filename="{attachment}"')
                    msg.attach(part)

        # Connect to the SMTP server and send the email
        smtp_server = 'mail.abbott.com'
        smtp_port = 25  # Replace with the appropriate port

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # server.login(smtp_username, smtp_password)
            server.sendmail(from_email, to_email, msg.as_string())

        return "Email sent successfully!"
    except Exception as e:
        return f"Error sending email: {str(e)}"


def query_synapse_execute(sqlText):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrSynpase)
    cur = con1.cursor()
    do_cmd = sqlText
    cur.execute(do_cmd)


def query_sql_boa_execute(sqlText):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrMIDASQLBOA)
    cur = con1.cursor()
    do_cmd = sqlText
    cur.execute(do_cmd)


def query_synapse_return(sqlText):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrSynpase)
    cur = con1.cursor()
    cur.execute(sqlText)
    results = cur.fetchall()
    return results


def query_sql_boa_return(sqlText):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrMIDASQLBOA)
    cur = con1.cursor()
    cur.execute(sqlText)
    results = cur.fetchall()
    return results


def post_data_to_synapse_append(df, tblname, schma):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrSynpase)
    coxn = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(con1))
    df.to_sql(tblname, con=coxn, schema=schma, if_exists='append', index=True)


def post_data_to_sql_boa_append(df, tblname, schma):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrMIDASQLBOA)
    coxn = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(con1))
    df.to_sql(tblname, con=coxn, schema=schma, if_exists='append', index=True)


def post_data_to_synapse_overwrite(df, tblname, schma):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrSynpase)
    coxn = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(con1))
    df.to_sql(tblname, con=coxn, schema=schma, if_exists='replace', index=True)


def post_data_to_sql_boa_overwrite(df, tblname, schma):
    con1 = pyodbc.connect(CommonConnections.odbcConnStrMIDASQLBOA)
    coxn = sa.create_engine('mssql+pyodbc:///?odbc_connect={}'.format(con1))
    df.to_sql(tblname, con=coxn, schema=schma, if_exists='replace', index=True)


# Example email usage:
# if __name__ == "__main__":
#     recipient_email = "daniel.shields@abbott.com"
#     sender_email = "daniel.shields@abbott.com"
#     email_subject = "Hello from Python!"
#     email_body = "This is the email body. Feel free to customize it."
#     #attachment_paths = [r'C:/Users/shieldx1/OneDrive - Abbott/LoginInfo/BOADB__UID.txt',
#      #                   r'C:\Users\shieldx1\OneDrive - Abbott\LoginInfo\CDP_Storage_Endpoint.txt']  # Optional attachments
#
#     email = send_email(recipient_email, sender_email, email_subject, email_body)#, attachments=attachment_paths)

#Example simple query usage:
# # execute query on sql server - no return
# if __name__ == "__main__":
#     #collapse any potential lists sent into character values before execute.
#     text = f"select *\
#     from anpd_mida.item_dim\
#     where retailer_item_num_json like '%7468266%'\
#     or retailer_item_num_json like '%7468265%'"
#     results = query_synapse_return(text)
#     print(results)
