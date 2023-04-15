import time
import pandas as pd
import numpy as np

# Small change to test git
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

    # Get user input for city (chicago, new york city, washington)
    while True:
        city = input('Would you like to see data for "Chicago", "New York City" or "Washington". Please type the exact name as provided: ').title()
        if city not in ['Chicago', 'New York City', 'Washington']:
            print('Invalid input. Please enter a valid city name.')
        else:
            break

    # Get user input for month (all, january, february, ..., june)
    while True:
        month = input('Please enter the name of the month you want to analyze ("January", "February", "March", "April", "May", "June") or "all" to apply no month filter: ').title()
        if month != 'All' and month not in ['January', 'February', 'March', 'April', 'May', 'June']:
            print('Invalid input. Please enter a valid month name or "all".')
        else:
            break

    # Get user input for day of week (all, monday, tuesday, ..., sunday)
    while True:
        day = input('Please enter the name of the day of week you want to analyze ("Monday", "Tuesday", ..., "Sunday"), or "all" to apply no day filter: ').title()
        if day != 'All' and day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            print('Invalid input. Please enter a valid day of week or "all".')
        else:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city.lower()])
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    
    if month != 'All':
        df = df[df['Month'] == month]

    if day != 'All':
        df = df[df['Day of Week'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    common_month = df['Month'].mode()[0]
    print('The most common month is:', common_month)


    common_day = df['Day of Week'].mode()[0]
    print('The most common day of week is:', common_day)


    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('The most common start hour is:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', common_start_station)


    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is:', common_end_station)


    df['Start-End Stations'] = df['Start Station'] + ' to ' + df['End Station']
    common_start_end_station = df['Start-End Stations'].mode()[0]
    print('The most frequent combination of start station and end station trip is:', common_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', total_travel_time, 'seconds')


    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time, 'seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print('Counts of user types:')
    print(user_types)


    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:')
        print(gender_counts)
    else:
        print('\nGender data is not available for this city.')


    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest birth year:', earliest_birth_year)
        print('Most recent birth year:', most_recent_birth_year)
        print('Most common birth year:', common_birth_year)
    else:
        print('\nBirth year data is not available for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    start_loc = 0
    view_data = input('Do you want to see the first 5 rows of data? Enter "yes" to see the data. Other answer may be considered as no.').lower()
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input('Do you want to see the next 5 rows of data? Enter "yes" to see the data. Other answer may be considered as no.').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
