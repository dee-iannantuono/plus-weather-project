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


def convert_f_to_c(temp_in_f):
    if isinstance(temp_in_f, (float, int)):
        temp_in_f = float(temp_in_f)
        celsius = (temp_in_f - 32) * 5/9
        rounded_celsius = round(celsius, 1)
        return rounded_celsius
    elif isinstance(temp_in_f, str):
        try:
            temp_in_f = float(temp_in_f)
            celsius = (temp_in_f - 32) * 5/9
            rounded_celsius = round(celsius, 1)
            return rounded_celsius
        except ValueError:
            return rounded_celsius
    # """Converts an temperature from farenheit to celcius.
    # Args:
    #     temp_in_farenheit: float representing a temperature.
    # Returns:
    #     A float representing a temperature in degrees celcius, rounded to 1dp.
    # """


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


def load_data_from_csv(folder_path):
    # result = []
    # folder_path = "PLUS-WEATHER-PROJECT/tests/data"
    # for filename in os.listdir(folder_path):
    #     if filename.endswith(".csv"):
    #         file_path = os.path.join(folder_path, filename)
    #         with open(file_path, 'r') as csv_file:
    #             reader = csv.reader(csv_file)
    #             for row in reader:
    #                 if row:
    #                     result.append(row)
    # return result
    with open('wombatzrule\Desktop\she_codes\plus-weather-project\tests\data') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    """Reads a csv file and stores the data in a list.
    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    # with open(file="example_one.csv") as csv_file:


def find_min(temperatures):
    if not temperatures:
        return ()
    min_value = float(temperatures[0])
    min_index = 0
    for i in range(1, len(temperatures)):
        current_value = float(temperatures[i])
        if current_value <= min_value:
            min_value = current_value
            min_index = i
    return min_value, min_index
    """Calculates the minimum value in a list of numbers.
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

def find_max(temperatures):
    if not temperatures:
        return ()
    max_value = float(temperatures[0])
    max_index = 0
    for i in range(1, len(temperatures)):
        current_value = float(temperatures[i])
        if current_value >= max_value:
            max_value = current_value
            max_index = i
    return max_value, max_index
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """


def generate_summary(data):
#     num_days = len(data)
#     mintemperatures = [item[1] for item in data]
#     maxtemperatures = [item[2] for item in data]
#     lowest_temp = convert_f_to_c(min(mintemperatures))
#     highest_temp = convert_f_to_c(max(maxtemperatures))
#     average_low = (sum(mintemperatures)) / len(mintemperatures)
#     average_low_c = convert_f_to_c(average_low)
#     average_high = (sum(maxtemperatures[1:])) / (len(maxtemperatures) - 1)
#     average_high_c = convert_f_to_c(average_high)
#     dates = [datetime.fromisoformat(item[0]) for item in data]
#     formatted_dates = [date.strftime("%A %d %B %Y") for date in dates]
#     summary = f"""{num_days} Day Overview
#   The lowest temperature will be {format_temperature(lowest_temp)}, and will occur on {formatted_dates[0]}.
#   The highest temperature will be {format_temperature(highest_temp)}, and will occur on {formatted_dates[1]}.
#   The average low this week is {format_temperature(average_low_c)}.
#   The average high this week is {format_temperature(average_high_c)}"""
#     return summary
    num_days = len(data)
    mintemperatures = [item[1] for item in data]
    maxtemperatures = [item[2] for item in data]
    lowest_temp = (min(mintemperatures))
    lowest_temp_c = convert_f_to_c(lowest_temp)
    highest_temp = (max(maxtemperatures))
    highest_temp_c = convert_f_to_c(highest_temp)
    average_low = (sum(mintemperatures)) / len(mintemperatures)
    average_low_c = convert_f_to_c(average_low)
    average_high = sum(maxtemperatures[1:]) / (len(maxtemperatures) - 1)
    average_high_c = convert_f_to_c(average_high)
    dates = [datetime.fromisoformat(item[0]) for item in data]
    formatted_dates = [date.strftime("%A %d %B %Y") for date in dates]
    lowest_temp_index = mintemperatures.index(lowest_temp)
    highest_temp_index = maxtemperatures.index(highest_temp)
    summary = f"""{num_days} Day Overview
  The lowest temperature will be {format_temperature(lowest_temp_c)}, and will occur on {formatted_dates[lowest_temp_index]}.
  The highest temperature will be {format_temperature(highest_temp_c)}, and will occur on {formatted_dates[highest_temp_index]}.
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
