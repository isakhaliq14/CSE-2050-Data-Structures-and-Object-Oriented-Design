# Instructions:
# 1. **Remove the TODO comment and pass statement** once you’ve completed the function implementation.
#    - The TODO and pass are placeholders indicating that the function is not yet complete.
#    - Once the function is implemented, these should be removed to keep the code clean.
# 
# 2. **Best Coding Practices**:
#    - In professional programming, finalizing the code means removing unnecessary placeholders.
#    - This ensures your code is ready for review, testing, and does not contain clutter.
# 
# 3. **Adding Docstrings**:
#    - After removing TODO and pass, add a **docstring** for each function.
#    - The docstring should explain the function’s purpose, parameters, and expected output.
#    - Proper documentation improves code readability and helps with debugging and maintenance.

def read_weather_data(file_path: str):

    """
    Description: 
    Reads weather data from the provided text file and returns it as a list of tuples.

    Parameters:
    file_path (str): The path to the weather data file.
    
    Returns:
    List[Tuple(str, float, float)]: A list of tuples where each tuple contains the date (str), temperature (float), and rainfall (float).
    """

    with open(file_path, 'r') as f:
        list1 = []
        data = f.readlines()
        for i in data:
            date = i.split(',')[0]
            temp = i.split(',')[1]
            rainfall = i.split(',')[2]

            list1.append((date, float(temp), float(rainfall)))
    return list1


def calculate_average_temperature(weather_data):

    """
    Description: 
    Calculates and returns the average temperature.

    Parameters:
    data (List[Tuple(str, float, float)]): The weather data.

    Returns:
    float: The average temperature.
    """
  
    total_temp = 0
    count = 0
    for i in weather_data:
        string1 = str(i)
        temp = string1.split(',')[1]
        temp = float(temp)
        total_temp += temp
        count += 1
    
    average_temp = total_temp / count
    return average_temp


def calculate_total_rainfall(weather_data):

    """
    Description: 
    Calculates and returns the total rainfall.

    Parameters:
    data (List[Tuple(str, float, float)]): The weather data.

    Returns:
    float: The total rainfall.
    """

    total_rainfall = 0
    for i in weather_data:
        string1 = str(i)
        rainfall = string1.split(',')[2]
        rainfall = float(rainfall.replace(')', ''))
        total_rainfall += rainfall
        
    
    return total_rainfall
   

def find_highest_temperature(weather_data):

    """
    Description: 
    Finds the highest temperature and its date.

    Parameters:
    data (List[Tuple(str, float, float)]): The weather data.

    Returns:
    Tuple[str, float]: A tuple containing the date and temperature.
    """

    current_highest_temp = 0.0
    current_highest_date = ''
    for i in weather_data:
        string1 = str(i)
        temp = string1.split(',')[1]
        temp = float(temp)
        if temp > current_highest_temp:
            current_highest_temp = temp
            current_highest_date = string1.split(',')[0]

    current_highest_date = current_highest_date.replace('(', '')
    current_highest_date = current_highest_date.replace('\'', '')
    output = (current_highest_date, current_highest_temp)
    return output
    


def find_lowest_temperature(weather_data):

    """
    Description: 
    Finds the lowest temperature and its date.

    Parameters:
    data (List[Tuple(str, float, float)]): The weather data.

    Returns:
    Tuple[str, float]: A tuple containing the date and temperature. 
    """
    current_lowest_temp = 100000000
    current_lowest_date = ''
    for i in weather_data:
        string1 = str(i)
        temp = string1.split(',')[1]
        temp = float(temp)
        if temp < current_lowest_temp:
            current_lowest_temp = temp
            current_lowest_date = string1.split(',')[0]

    current_lowest_date = current_lowest_date.replace('(', '')
    current_lowest_date = current_lowest_date.replace('\'', '')
    output = (current_lowest_date, current_lowest_temp)
    return output


def find_day_with_most_rainfall(weather_data):

    """
    Description: 
    Finds the day with the most rainfall and its value.

    Parameters:
    data (List[Tuple(str, float, float)]): The weather data.

    Returns:
    Tuple[str, float]: A tuple containing the date and rainfall.
    """
    
    current_highest_rainfall = 0.0
    current_highest_date = ''
    for i in weather_data:
        string1 = str(i)
        rainfall = string1.split(',')[2]
        rainfall = float(rainfall.replace(')', ''))
        if rainfall > current_highest_rainfall:
            current_highest_rainfall = rainfall
            current_highest_date = string1.split(',')[0]

    current_highest_date = current_highest_date.replace('(', '')
    current_highest_date = current_highest_date.replace('\'', '')
    output = (current_highest_date, current_highest_rainfall)
    return output
