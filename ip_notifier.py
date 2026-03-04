import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import sys
import os

def get_public_ip():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=10)
        response.raise_for_status()
        return response.json()['ip']
    except Exception as e:
        try:
            response = requests.get('https://ifconfig.me/ip', timeout=10)
            response.raise_for_status()
            return response.text.strip()
        except Exception as e2:
            raise Exception(f"Failed to get IP: {e}, {e2}")

def send_email(ip_address, smtp_server, smtp_port, sender_email, sender_password, recipient_email):
    subject = f"Public IP Address - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    body = f"""
    Your public IP address is: {ip_address}
    
    Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    Computer: {os.environ.get('COMPUTERNAME', 'Unknown')}
    """
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        raise Exception(f"Failed to send email: {e}")

def main():
    SMTP_SERVER = os.environ.get('SMTP_SERVER', 'smtp.qq.com')
    SMTP_PORT = int(os.environ.get('SMTP_PORT', '587'))
    SENDER_EMAIL = os.environ.get('SENDER_EMAIL', '')
    SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD', '')
    RECIPIENT_EMAIL = '704457936@qq.com'
    
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("Error: SENDER_EMAIL and SENDER_PASSWORD environment variables must be set")
        sys.exit(1)
    
    try:
        print("Getting public IP address...")
        ip = get_public_ip()
        print(f"Public IP: {ip}")
        
        print("Sending email...")
        send_email(ip, SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
