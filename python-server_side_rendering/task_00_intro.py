#!/usr/bin/python3
"""
salam
"""

import os


def generate_invitations(template, attendees):
    """
    salam
    """

    # -------- Input type validation ----------
    if not isinstance(template, str):
        print("Invalid input: template should be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees should be a list of dictionaries.")
        return

    # -------- Empty template ----------
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    # -------- Empty attendees list ----------
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # -------- Process attendees ----------
    for index, person in enumerate(attendees, start=1):

        # Replace missing or None values with "N/A"
        name = person.get("name") or "N/A"
        event_title = person.get("event_title") or "N/A"
        event_date = person.get("event_date") or "N/A"
        event_location = person.get("event_location") or "N/A"

        # Create personalized content
        filled_template = (
            template
            .replace("{name}", name)
            .replace("{event_title}", event_title)
            .replace("{event_date}", event_date)
            .replace("{event_location}", event_location)
        )

        # Output file name: output_X.txt
        filename = f"output_{index}.txt"

        # Write the file
        with open(filename, "w") as f:
            f.write(filled_template)
