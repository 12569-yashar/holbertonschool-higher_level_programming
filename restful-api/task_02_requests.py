#!/usr/bin/python3
import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts and print the status code + titles."""
    response = requests.get(API_URL)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If success, parse JSON
    if response.status_code == 200:
        data = response.json()  # JSON list of posts

        # Print all titles
        for post in data:
            print(post.get("title"))
    else:
        print("Failed to fetch data")


def fetch_and_save_posts():
    """Fetch posts and save selected fields to a CSV file."""
    response = requests.get(API_URL)

    if response.status_code != 200:
        print("Failed to fetch data")
        return

    data = response.json()

    # Extract specific fields: id, title, body
    posts_list = [
        {
            "id": post.get("id"),
            "title": post.get("title"),
            "body": post.get("body")
        }
        for post in data
    ]

    # Write to CSV file
    with open("posts.csv", "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()  # write column names
        writer.writerows(posts_list)  # write posts

    print("posts.csv successfully created.")
