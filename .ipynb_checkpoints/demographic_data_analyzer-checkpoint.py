import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    df1=df.copy()
    df2=list(df1.drop_duplicates(['race'])['race'])
    lst=[]
    for i,j in enumerate(df2):
        cnt=df[df.race==j]['race'].count()
        lst.append(cnt)
    

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count=pd.Series(lst,index=df2)

    AgeOfMen=df[df.sex=='Male'].age.sum()
    TotalCountAge=df[df.sex=='Male'].age.count()
    
    # What is the average age of men?
    average_age_men = round(AgeOfMen/TotalCountAge,1)
    
    # What is the percentage of people who have a Bachelor's degree?
    No_of_people_having_Bachleor=df[df.education=='Bachelors'].education.count()
    TotalCount=df['education'].count()
    percentage_bachelors = round((No_of_people_having_Bachleor/TotalCount)*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    unique_education=set(df.drop_duplicates(['education'])['education'])
    masterEdu=set(['Bachelors','Masters','Doctorate'])
    lowerEdu=unique_education - masterEdu
    
    
    higher_education = df1[df1.education.isin(masterEdu)]['education'].count()
    lower_education = df1[df1.education.isin(lowerEdu)]['education'].count()
    
    higher_education_rich1 = df1[(df1.education.isin(masterEdu)) & (df1.salary=='>50K')]['education'].count()
    lower_education_rich1 = df1[(df1.education.isin(lowerEdu)) & (df1.salary=='>50K') ]['education'].count()
    # percentage with salary >50K
    
    higher_education_rich =  round((higher_education_rich1/people_with_advance_edu)*100,1)
    lower_education_rich = round((lower_education_rich1/people_with_lower_edu)*100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df1["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df1[df1["hours-per-week"]== 1]['hours-per-week'].count()
    rich_count=df1[(df1["hours-per-week"]== 1) & (df1['salary']=='>50K')]['hours-per-week'].count()

    rich_percentage = int((rich_count/num_min_workers)*100)

    # What country has the highest percentage of people that earn >50K?
    people_earning_more = df1[df1.salary=='>50K']
    people_earning_more_count_country_wise=df1[df1.salary=='>50K'].groupby(['native-country'])['native-country'].value_counts()
    count_total_people=df1.groupby(['native-country'])['native-country'].value_counts()
    rich_people_count_df=people_earning_more_count_country_wise/count_total_people

    highest_earning_country = rich_people_count_df.idxmax()
    highest_earning_country_percentage = round(rich_people_count_df.max()*100,1)

    # Identify the most popular occupation for those who earn >50K in India
    occupation_df=df1[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    group_by_occ=occupation_df.groupby(['occupation'])['occupation'].count()
    top_IN_occupation = group_by_occ.idxmax()

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
calculate_demographic_data()
