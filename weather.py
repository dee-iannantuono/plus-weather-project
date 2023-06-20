import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(date):
    date_obj = datetime.fromisoformat(date)
    formatted_date = date_obj.strftime ("%A %d %B %Y")
    return formatted_date
    # """Converts and ISO formatted date into a human readable format.

    # Args:
    #     iso_string: An ISO date string..
    # Returns:
    #     A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    # """
    #WORKS BUT DATES SHOW IN THE WRONG ORDER


def convert_f_to_c(temp_in_f):
    temp_in_f = int(temp_in_f)
    celsius = (temp_in_f - 32) * 5/9
    rounded_celsius = round(celsius, 1)
    return rounded_celsius
    # """Converts an temperature from farenheit to celcius.

    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """
    # WORKS EXCEPT FOR ONE 17.8 != 18 


def calculate_mean(temperatures):
    temperatures = [int(num) if isinstance(num, str) else num for num in temperatures]
    total = sum(temperatures)
    mean = total/len(temperatures)
    return mean 
    # """Calculates the mean value from a list of numbers.
    # Args:
    #     weather_data: a list of numbers.
    # Returns:
    #     A float representing the mean value.
    # """
    #WORKS :) 


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # with open(file="example_one.csv") as csv_file:
    data = []
    with open(tests/data, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    return data
    pass


def find_min(temperatures):
    min_value = min(temperatures)
    min_value_formatted = "{:.1f}".format(min_value)
    min_index = temperatures.index(min_value)
    print(min_value, min_index)
    return min_value_formatted, min_index
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    #NEED MORE HELP WITH THIS ONE 


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(data):
    num_days = len(data)
    mintemperatures = [item[1] for item in data]
    maxtemperatures = [item[2] for item in data]
    lowest_temp = convert_f_to_c(min(mintemperatures))
    highest_temp = convert_f_to_c(max(maxtemperatures))
    average_low = (sum(mintemperatures)) / len(mintemperatures)
    average_low_c = convert_f_to_c(average_low)
    average_high = (sum(maxtemperatures[1:])) / (len(maxtemperatures) - 1)
    average_high_c = convert_f_to_c(average_high)
    dates = [datetime.fromisoformat(item[0]) for item in data]
    formatted_dates = [date.strftime("%A %d %B %Y") for date in dates]
    summary = f"""{num_days} Day Overview
  The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {formatted_dates[0]}.
  The highest temperature will be {format_temperature(highest_temp)}, and will occur on {formatted_dates[1]}.
  The average low this week is {format_temperature(average_low_c)}.
  The average high this week is {format_temperature(average_high_c)}"""
    return summary
    """Outputs a summary for the given weather data.
    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # KEEP GETTING ERRORS ON THIS 

# example_one = [
#             ["2021-07-02T07:00:00+08:00", 49, 67],
#             ["2021-07-03T07:00:00+08:00", 57, 68],
#             ["2021-07-04T07:00:00+08:00", 56, 62],
#             ["2021-07-05T07:00:00+08:00", 55, 61],
#             ["2021-07-06T07:00:00+08:00", 53, 62]
#         ]

# print(generate_summary(example_one))

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
