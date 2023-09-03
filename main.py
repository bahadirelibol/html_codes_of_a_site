import requests

while True:
    try:
        url = input("Enter the web page URL: ")
        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            with open("web_page.html", "w", encoding="utf-8") as file:
                file.write(html_content)
            print("The HTML codes of the web page have been saved successfully.")
            break
        else:
            print("The web page could not be downloaded. Error code:", response.status_code)

    except requests.exceptions.MissingSchema:
        print("Invalid URL format. Enter the URL correctly.")
    except requests.exceptions.ConnectionError:
        print("No internet connection or website unreachable.")
    except Exception as e:
        print("Something went wrong:", str(e))