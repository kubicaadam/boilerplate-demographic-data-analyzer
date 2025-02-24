import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby(["race"]).size()

    # What is the average age of men?
    average_age_men = df.loc[df["sex"] == "Male"]["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df["education"] == "Bachelors"].shape[0] / df["education"].shape[0] * 100.0, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    he_df = df.loc[(df["education"].isin(["Bachelors", "Masters", "Doctorate"]))]
    le_df = df.loc[~(df["education"].isin(["Bachelors", "Masters", "Doctorate"]))]

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = round(he_df.loc[he_df["salary"] == "<50K"].shape[0] / he_df.shape[0] * 100, 1)
    lower_education = round(le_df.loc[le_df["salary"] == "<50K"].shape[0] / le_df.shape[0] * 100, 1)

    # percentage with salary >50K
    higher_education_rich = round(he_df.loc[he_df["salary"] == ">50K"].shape[0] / he_df.shape[0] * 100, 1)
    lower_education_rich = round(le_df.loc[le_df["salary"] == ">50K"].shape[0] / le_df.shape[0] * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    mh_df = df.loc[df["hours-per-week"] == min_work_hours]

    num_min_workers = mh_df.shape[0]

    rich_percentage = round(mh_df.loc[mh_df["salary"] == ">50K"].shape[0] / num_min_workers * 100, 1)
    
    hpg_df = df.groupby(["native-country", "salary"]).count().reset_index().rename(columns={'age': 'cnt'})
    hpgr_df = hpg_df.loc[hpg_df["salary"] == ">50K"][["native-country", "cnt"]].set_index("native-country")
    hpgp_df = hpg_df.loc[hpg_df["salary"] == "<=50K"][["native-country", "cnt"]].set_index("native-country")
    print(hpgp_df.join(hpgr_df, lsuffix="p", rsuffix="r"))

    #df_combined = pd.concat([df1, df2], axis=1)
    #.rename(columns={'A': 'New_A'})

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }



calculate_demographic_data(print_data=True)