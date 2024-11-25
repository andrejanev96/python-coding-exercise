import requests

def fetch_data_and_process():
    #This part fetches the JSON data using an HTTP request
    url='https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)

    #This part checks if the request we sent was successful
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Failed to fetch the data. HTTP Status Code received: {response.status_code}")
        return
    
    #This part processes the data to extract the titles that contain the keyword ('what')
    keyword='what'
    filtered_titles = [todo['title'] for todo in data if keyword in todo['title']]

    #This part displays the results using f strings
    print('\nFiltered Titles:')
    for title in filtered_titles:
        print(f"Title: {title}")

    #This part checks the type of the first title, first ensuring that there is at least one title
    if filtered_titles:
        first_title=filtered_titles[0]
        print("\n Type Checking:")
        print(f"Is the first title of type 'int'? {'Yes' if isinstance(first_title, int) else 'No'}")
    else:
        print("\nNo titles matched the filter.")


fetch_data_and_process()