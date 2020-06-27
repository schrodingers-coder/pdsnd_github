import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Choose a city out of Chicago, New York City or Washington? \n> ').lower()
    while True:
        if city in city:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input('Enter the month of your choice from January to June or choose \'all\' for no filters : '))


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input('Enter the day of week of your choice from Monday to Sunday or choose \'all\' for no filters: '))


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[ df['month'] == month ]


    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common month is: ', common_month)


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular Start Station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular End Station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_stations = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('This is the most popular Start-End Station combination: ', popular_start_end_stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60
    print('The total travel time is: ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() / 60
    print('The mean travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('Gender information for this city is unavailable.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print('The earliest birth year is: ', earliest_birth_year)
        print('The most recent birth year is: ', most_recent_birth_year)
        print('The most common birth year is: ',common_birth_year)
    else:
        print('Birth Year information for this city is unavailable.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

"""Display 5 lines of raw data to the user."""
def data(df):
    view_data = 0
    while True:
        answer = input('\nWould you like to see 5 rows of individual trip data? Enter Yes or No\n').lower()
        if answer not in ['yes','no']:
            answer = input('\n Oops! You seem to have entered an invalid input. Please try again.\n').lower()
        elif answer == 'yes':
            view_data += 5
            print(df.iloc[view_data : view_data + 5])
            view_again = input('\n Do you wish to see 5 more rows of individual trip data? Enter Yes or No\n').lower()
        if view_again == 'no':
            break
        elif answer == 'no':
            return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
