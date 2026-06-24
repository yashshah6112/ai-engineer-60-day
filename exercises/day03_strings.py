# Practice cleaning and changing a fake support message.
raw_message = "  vpn not working in the office  "

print("Original:", repr(raw_message))
print("Lowercase:", raw_message.lower())
print("Uppercase:", raw_message.upper())
print("No outer spaces:", raw_message.strip())
print("Updated wording:", raw_message.replace("office", "workspace"))
print("Words:", raw_message.split())

def clean_issue_title(raw_issue):
    # Remove extra spaces and turn repeated words into one clean sentence.
    cleaned_issue = " ".join(raw_issue.strip().split())

    # Make the sentence readable and keep VPN in its common uppercase form.
    cleaned_issue = cleaned_issue.capitalize()
    cleaned_issue = cleaned_issue.replace("Vpn", "VPN")

    return cleaned_issue

test_issue = " vpn not working "
clean_title = clean_issue_title(test_issue)

print("\nClean Title:", clean_title)

# Ask for a fictional request so the acknowledgement can be personalized.
requester_name = input("\nRequester name: ").strip()
raw_issue_message = input("Describe the issue: ")

cleaned_issue_message = clean_issue_title(raw_issue_message)

acknowledgement = f"""
---Ticket Acknowledgement---
Hello {requester_name},

Your request has been received.

Ticket title: {cleaned_issue_message}
Status: Open
Next Step: A support team member will review the issue.

Thank you,
Support Desk
"""

print(acknowledgement)

# Store fictional helpdesk requests for loop practice.
fake_requests = [
    " vpn not working  ",
    "cannot access email",
    "printer keeps showing offline",
    "laptop battery drains quickly",
    "need help resetting password"
]

print("--- Fake Helpdesk Requests ---")

for request in fake_requests:
    clean_request = clean_issue_title(request)
    print(f" -{clean_request}")

hidden_space_example = "  email access problem  "
print(repr(hidden_space_example))
print(repr(hidden_space_example.strip()))