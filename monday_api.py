import requests

API_URL = "https://api.monday.com/v2"

API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYzMTAwODY0NCwiYWFpIjoxMSwidWlkIjoxMDA4MTMwMzYsImlhZCI6IjIwMjYtMDMtMTBUMDU6NTk6MDMuMDAwWiIsInBlciI6Im1lOndyaXRlIiwiYWN0aWQiOjM0MTUzNDQzLCJyZ24iOiJhcHNlMiJ9.1-TeJeJXVJ7qpgQ6-XumvVmJGLE-fzlGAtHJ-wkNY6I"

headers = {
    "Authorization": API_KEY
}


def fetch_board_data(board_id):

    query = f"""
    query {{
      boards(ids: [{board_id}]) {{
        name
        items_page(limit: 500) {{
          items {{
            name
            column_values {{
              column {{
                title
              }}
              text
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(API_URL, json={"query": query}, headers=headers)

    data = response.json()

    print("Monday API Response:", data)

    return data