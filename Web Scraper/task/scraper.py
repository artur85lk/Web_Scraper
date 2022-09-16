import requests

print("Input the URL:")
url = input()
page_content = requests.get(url)

if page_content.status_code == 200:
    with open("source.html", "wb") as f:
        f.write(page_content.content)

    print("\nContent saved.")
else:
    print(f"\nThe URL returned {page_content.status_code}")



