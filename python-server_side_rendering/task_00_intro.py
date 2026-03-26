def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input types")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    for index, attendee in enumerate(attendees, start=1):
        content = template.replace('{name}', attendee.get('name') or 'N/A')
        content = content.replace('{event_title}', attendee.get('event_title') or 'N/A')
        content = content.replace('{event_date}', attendee.get('event_date') or 'N/A')
        content = content.replace('{event_location}', attendee.get('event_location') or 'N/A')

        with open(f"output_{index}.txt", "w") as f:
            f.write(content)
