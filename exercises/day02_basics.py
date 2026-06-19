# Collect the ticket details before creating a readable receipt.
requester_name = input("Requester name: ").strip()
issue_type = input("Issue type (Login, Email, Hardware): ").strip()
issue_title = input("Issue title: ").strip()
priority = input("Priority (Low, Medium, High): ").strip()

# Store example values that a real ticket system could track.
ticket_number = 1001
estimated_resolution_hours = 2.5
is_high_priority = priority.lower() == "high"

# Display the ticket details in a consistent, easy-to-read format.
print("\n--- Support Ticket Receipt ---")
print(f"Ticket Number: {ticket_number}")
print(f"Requester: {requester_name}")
print(f"Issue type: {issue_type}")
print(f"Issue title: {issue_title}")
print(f"Priority: {priority}")
print(f"High priority: {is_high_priority}")
print(f"Estimated resolution: {estimated_resolution_hours} hours")
print("------------------------------")