import time
import pandas as pd
import numpy as np

CITY_DATA = ['chicago.csv', 'new_york_city.csv', 'washington.csv' ]
MONTHS = [ 'January', 'February', 'March', 'April' , 'May', 'June', 'July' , 'August', 'September' , 'October', 'November', 'December' ]
WEEK_DAYS = ['friday', 'sunday','monday','tuesday','wednesday','thursday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    """
    print('Hello! Let\'s explore some US bikeshare data!')
    city = 0
    while(not city  in range(1,4)) :
        city = input("please choose the required city number \n 1- chicago \n 2- new york city \n 3- washington :\n")
        try:
            city = int(city)
            if (not city  in range(1,4)):
                print("Invalid input '{}', Please choose a value between 1 and 3!".format(city))
        except ValueError:
            print("'{}' is not a valid integer or 'all'! Please try again ...".format(city))

    month = 0
    while ((month not in range(1,13)) and (month != 'all')) :
        month = input("please choose the required month number or all \n 1- January \n 2- February \n 3- March \n 4- April \n 5- May \n 6-June \n 7- July \n 8- August \n 9- September \n 10- October \n 11- November \n 12- December \n")
        try:
            month = month if (month.lower() == 'all')  else int(month)
            if ((month not in range(1,13)) and (month != 'all')):
                print("Invalid input '{}', Please choose a value between 1 and 12!".format(month))
        except ValueError:
            print("'{}' is not a valid integer or 'all'! Please try again ...".format(month))

    day = 0
    while ((day not in range(1,8)) and (day != 'all')) :
        day  = input("please choose the required week day name or all \n 1- Friday \n 2- Sunday \n 3- Monday \n 4- Tuesday \n 5- Wednesday \n 6- Thursday \n 7- Saturday \n")
        try:
            day = day if (day.lower() == 'all')  else int(day)
            if((day not in range(1,8)) and (day != 'all')):
                print("Invalid input '{}', Please choose a value between 1 and 7!".format(day))
        except ValueError:
            print("'{}' is not a valid integer or 'all'! Please try again ...".format(day))

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city - 1])
    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] =  df['Start Time'].dt.day_name()
    #filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        #filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'].str.lower() == WEEK_DAYS[day-1]]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] =pd.to_datetime( df['Start Time'])
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    # find the most common Month
    popular_month = df['month'].mode()[0]

    print('Most Frequent Start Month: {} \n'.format(popular_month))

    # TO DO: display the most common day of week

    df['day'] = df['Start Time'].dt.day_name()

    # find the most common day
    popular_day = df['day'].mode()[0]

    print('Most Frequent Start Day: {} \n'.format(popular_day))

    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]

    print('Most Frequent Start Hour: {} \n'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('Most commonly used start station: {} \n'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station

    print('Most commonly used end station: {} \n'.format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip

    print('Most frequent combination of start station and end station trip are: {} \n'.format((df['Start Station'] + df['End Station']).mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    total_time_in_hours = int(total_time / 3600)
    total_time_in_minutes = int((total_time % 3600) / 60)
    total_time_in_seconds = (total_time % 3600) % 60
    print('Total travel time is {} hours and {} minutes and {} seconds \n'.format(total_time_in_hours , total_time_in_minutes , total_time_in_seconds ))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    mean_time_in_hours = int(mean_time / 3600)
    mean_time_in_minutes = int((mean_time % 3600) / 60)
    mean_time_in_seconds = (mean_time % 3600) % 60
    print('Mean travel time is {} hours and {} minutes and {} seconds \n'.format(mean_time_in_hours , mean_time_in_minutes , mean_time_in_seconds ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    user_types = user_types.reset_index().to_csv(header=None,index=None,sep='\t')[:-1]

    print('User types are \n{} \n'.format(user_types))

    # TO DO: Display counts of gender

    gender = df['Gender'].value_counts()
    gender = gender.reset_index().to_csv(header=None,index=None,sep='\t')[:-1]

    print('Gender counts are \n{}\n'.format(gender))
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year =  df['Birth Year'].min()
    most_recent_year =  df['Birth Year'].max()
    most_common_year =  df['Birth Year'].mode()[0]
    print('The earliest year of birth is {} \nThe most recent is {} \nThe most common year is {}'.format(earliest_year, most_recent_year, most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty:
            print('There is no data for the filters you choose, please try again \n ')
            continue
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
