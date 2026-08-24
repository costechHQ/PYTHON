def show_messages(messages_list):
    """Loops through a list and prints each message."""
    for message in messages_list:
        print(f"{message}")

text_messages = ["Hey, are you free tonight?", "Don't forget the milk!", "Python is amazing!"]

show_messages(text_messages)
print("\n" + "="*40 + "\n")

def send_messages(messages_to_send, sent_messages_archive):
    """Simulates sinding messages by moving them from one list to another."""
    print("Sending messages now...")

    while messages_to_send:
        current_msg = messages_to_send.pop(0)
        print(f"Sending: '{current_msg}'")
        sent_messages_archive.append(current_msg)
    print("All messages sent successfully!\n")

sent_messages = []

send_messages(text_messages, sent_messages)

print("Verification checks:")
print(f"Original list (text_messages): {text_messages}")
print(f"Archive list (sent_messages): {sent_messages}")
print("\n" + "="*40 + "\n")

#8.11
text_messages = ["Hey, are you free tonight?", "Don't forget the milk!", "Python is amazing!"]
sent_messages = []

send_messages(text_messages[:], sent_messages)
print(f"Original list (tex_messages): {text_messages}")
print(f"Archive list (sent_messages): {sent_messages}")