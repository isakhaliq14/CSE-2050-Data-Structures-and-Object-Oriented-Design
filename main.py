# main.py

import weather_analysis

def weather_analyze(file_path):

    """
    Description: 
    Analyzes the weather data and returns a dictionary with statistical insights.

    Parameters:
    file_path (str): The path to the weather data file.

    Returns:
    dict: A dictionary containing the calculated statistics.
    """
    
    dict1 = {}

    dict1['average_temperature'] = weather_analysis.calculate_average_temperature(file_path)


    dict1['total_rainfall'] = weather_analysis.calculate_total_rainfall(file_path)


    dict2 = {}
    dict2['date'] = (weather_analysis.find_highest_temperature(file_path)).split(',')[0]
    dict2['temperature'] = (weather_analysis.find_highest_temperature(file_path)).split(',')[1]
    dict1['highest_temperature'] = dict2


    dict3 = {}
    dict3['date'] = (weather_analysis.find_lowest_temperature(file_path)).split(',')[0]
    dict3['temperature'] = (weather_analysis.find_lowest_temperature(file_path)).split(',')[1]
    dict1['lowest_temperature'] = dict3


    dict4 = {}
    dict4['date'] = (weather_analysis.find_day_with_most_rainfall(file_path)).split(',')[0]
    dict4['rainfall'] = (weather_analysis.find_day_with_most_rainfall(file_path)).split(',')[1]
    dict1['most_rainfall'] = dict4

    return dict1



if __name__ == "__main__":
    
    results = weather_analyze("weather_data.txt") #or the path to the file
    print(results)