from database import cursor
import smtplib


# Check if temperature exceeds the threshold
def check_thresholds(city):
    cursor.execute('''SELECT temp FROM weather WHERE city = ? ORDER BY timestamp DESC LIMIT 2''', (city,))
    temps = cursor.fetchall()

    if len(temps) == 2 and all(temp[0] > 35 for temp in temps):
        send_alert(city, temps[0][0])


# Function to send email alert
def send_alert(city, temp):
    sender = 'youremail@example.com'
    recipient = 'recipient@example.com'
    subject = f'Weather Alert for {city}'
    body = f'Temperature in {city} has exceeded 35°C. Current temperature: {temp}°C.'

    email_text = f"""\
    From: {sender}
    To: {recipient}
    Subject: {subject}

    {body}
    """

    try:
        smtp_server = smtplib.SMTP('smtp.example.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender, 'yourpassword')
        smtp_server.sendmail(sender, recipient, email_text)
        smtp_server.close()
        print(f"Alert sent for {city}: {temp}°C")
    except Exception as e:
        print(f"Error sending alert: {e}")


# Test alert system
if __name__ == "__main__":
    check_thresholds('Hyderabad')
