import vonage

# Input recipient's phone number and the message
from_number = input("Enter the number you want to send the message from (along with code):\n")
message = input("Enter the message:\n")
number = input("Enter the number you want to send the message to (along with country code): ")

# Initialize the Vonage API client with your API key and secret
client = vonage.Client(key="6d834cd8", secret="vjaADkgy7l6N5eNy")

# Create an instance of the Vonage SMS class to interact with the SMS API
sms = vonage.Sms(client)	

# Send the message using the Vonage API
responseData = sms.send_message({
    "from": from_number,  # The sender ID or name that appears as the sender of the message
    "to": number,  # The recipient's phone number in international format (e.g., +1234567890)
    "text": message,  # The content of the message
})

# Check the response to see if the message was sent successfully
if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
