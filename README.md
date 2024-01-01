Weather Information CLI

    A simple command-line interface (CLI) tool to fetch real-time weather information using OpenWeatherMap API based on a provided location.

    Usage:
        The CLI provides the following commands to retrieve specific weather information:
        1. All Information:
            Fetches complete weather information for the given location.
            Command:
                python weather_cli.py all --place "Place"
        2. Description:
            Fetches and displays only the weather description for the given location.
            Command:
                python weather_cli.py description --place "Place"
        3. Temperature:
            Fetches and displays temperature information in Celsius, Fahrenheit, and Kelvin for the given location.
            Command:
                python weather_cli.py temperature --place "Place"
        4. Pressure:
            Fetches and displays atmospheric pressure for the given location.
            Command:
                python weather_cli.py pressure --place "Place"
        5. Humidity:
            Fetches and displays humidity information for the given location.
            Command:
                python weather_cli.py humidity --place "Place"
                
    API Key:
        To use the OpenWeatherMap API, you need to replace the placeholder "Your API key" in the generate function with your actual API key.

If you encounter any issues or have suggestions, feel free to open an issue or create a pull request.
Happy weather checking!
