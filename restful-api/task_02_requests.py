#!usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    fetch_and_print_posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        print(f"Status Code: {response.status_code}")
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    fetch_and_save_posts
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        stuct_data = []
        for post in posts:
            stuct_data.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
    with open("post.csv", 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(stuct_data)
