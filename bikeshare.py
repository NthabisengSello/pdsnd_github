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
    print("We have bikeshare data for chicago,new york city and Washington")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
           cities = ['chicago', 'new york city', 'washington']
           city = input("Which city would you like to explore?:" ).lower()

           if city in cities:
                print(city)
                break
           else:
             print("Your input is incorrect,please try again")


    # TO DO: get user input for month (all, january, february, march, april, may , june)
    while True:
          months = ['all','january', 'february', 'march','april','may','june']
          month = input("Which month?Please enter month from January to June or Enter 'All' for all months:").lower()

          if month in months:
             print(month)
             break
          else:
            print("Your input is incorrect,please try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
          days = ['all','monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
          day = input("Which day?If you want data for all the days please type 'All':").lower()

          if day in days:
             print(day)
             break
          else:
            print("Your input is incorrect,please try again")

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is:",common_month)

    
    # TO DO: display the most common day of week
    common_weekday = df['day_of_week'].mode()[0]
    print("The most common day of week  is:",common_weekday)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is:",common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station =  df['Start Station'].mode()[0]
    print("The most commonly used start station is:",common_start_station)
    


    # TO DO: display most commonly used end station
    common_end_station =  df['End Station'].mode()[0]
    print("The most commonly used end station is:",common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['station_combination'] = df[['Start Station','End Station']].agg('-->'.join,axis=1)
    frequent_station_combination = df['station_combination'].mode()[0]
    print("The most frequent combination of start station and end station trip is: ",frequent_station_combination )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is:",total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean() 
    print("The mean travel time is:",mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Types of users and their counts")
    user_types =df['User Type'].value_counts()
    print(user_types)
    print()


    if city == 'chicago':
        # TO DO:Display counts of gender
        print("Gender and counts in chicago")
        counts_of_gender = df['Gender'].value_counts()
        print(counts_of_gender)
        print()
        
        # TO DO: Display earliest, most recent, and most common year of birth earliest in chicago
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print("The earliest year of birth in chicago is: ",earliest_year)
        print("The most recent year of birth in chicago is: ",recent_year)
        print("The most common year of birth in chicago is: ",common_year)
        
    elif city == 'new york city':
        # Display counts of gender
        print("Gender and counts in new york city")
        counts_of_gender = df['Gender'].value_counts()
        print(counts_of_gender)
        
        # TO DO: Display earliest, most recent, and most common year of birth in chicago
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        
        print("The earliest year of birth in new york city is: ",earliest_year)
        print("The most recent year of birth in new york city is: ",recent_year)
        print("The most common year of birth in new york city is: ",common_year)
       
    else:
        print("gender and birth year data not available for washington")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """
    Prompt the user if they want to see 5 lines of raw data,
    Display that data if the answer is 'yes',
    Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration,
    Stop the program when the user says 'no' or there is no more raw data to display.
    """
    row_index = 0
    while True:
       user_input = input("Do you want to view some raw data?Please enter 'yes' or 'no' ").lower()
       if user_input == 'no':
          break
       elif user_input == 'yes':
        print(df.iloc[row_index:row_index+5])
        row_index+=5
       else:
          print("Please enter only 'yes' or 'no' ")
          
          

            
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
