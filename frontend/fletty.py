import flet as ft
import requests

def main(page: ft.Page):
    page.title = "SQL Query Generator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Define UI elements
    file_picker = ft.FilePicker(on_result=lambda e: print(f"File selected: {e.files}"))
    page.overlay.append(file_picker)  # Add the FilePicker to the page

    query_input = ft.TextField(label="Enter your request", multiline=True, width=600)
    output_area = ft.Text("Your SQL query will appear here.", selectable=True, width=600)
    generate_button = ft.ElevatedButton(
        "Generate SQL",
        on_click=lambda e: generate_query(file_picker.result, query_input.value, output_area)
    )
    upload_button = ft.ElevatedButton("Upload CSV File", on_click=lambda e: file_picker.pick_files(allow_multiple=False))

    page.add(
        ft.Column(
            [
                ft.Text("SQL Query Generator", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                upload_button,
                query_input,
                generate_button,
                ft.Text("Generated SQL Query:", style=ft.TextThemeStyle.HEADLINE_SMALL),
                output_area,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

def generate_query(file_picker_result, query, output_area):
    if not file_picker_result or not file_picker_result.files or not query:
        output_area.value = "Please upload a CSV file and enter a query."
        output_area.update()
        return

    file_path = file_picker_result.files[0].path

    url = "http://localhost:5011/generate-sql"
    files = {'csvFile': open(file_path, 'rb')}
    data = {'query': query}

    try:
        response = requests.post(url, files=files, data=data)
        response_data = response.json()
        output_area.value = response_data.get("sql_query", "No query generated.")
        output_area.update()
    except Exception as e:
        output_area.value = f"Error: {e}"
        output_area.update()

ft.app(target=main)
