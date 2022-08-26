import pandas as pd
import statistics
import csv
df = pd.read_csv("StudentsPerformance.csv")
gender_list = df["gender"].to_list()
math_score = df["math score"].to_list()
#Mean for height and Weight
gender_mean = statistics.mean(gender_list)
math_mean = statistics.mean(math_score)
#Median for height and weight
gender_median = statistics.median(gender_list)
math_median = statistics.median(math_score)
#Mode for height and weight
gender_mode = statistics.mode(gender_list)
math_mode = statistics.mode(math_score)
#Printing mean, median and mode to validate
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(gender_mean, gender_median, gender_mode))
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(math_mean, math_median, math_mode))
#Standard deviation for height and weight
gender_std_deviation = statistics.stdev(gender_list)
math_std_deviation = statistics.stdev(math_score)
#1, 2 and 3 Standard Deviations for height
gender_first_std_deviation_start, gender_first_std_deviation_end = gender_mean-gender_std_deviation, gender_mean+gender_std_deviation
gender_second_std_deviation_start, gender_second_std_deviation_end = gender_mean-(2*gender_std_deviation), gender_mean+(2*gender_std_deviation)
gender_third_std_deviation_start, gender_third_std_deviation_end = gender_mean-(3*gender_std_deviation), gender_mean+(3*gender_std_deviation)
#1, 2 and 3 Standard Deviations for math score
math_first_std_deviation_start, math_first_std_deviation_end = math_mean-math_std_deviation, math_mean+math_std_deviation
math_second_std_deviation_start, math_second_std_deviation_end = math_mean-(2*math_std_deviation), math_mean+(2*math_std_deviation)
math_third_std_deviation_start, math_third_std_deviation_end = math_mean-(3*math_std_deviation), math_mean+(3*math_std_deviation)
#Percentage of data within 1, 2 and 3 Standard Deviations for Height
gender_list_of_data_within_1_std_deviation = [result for result in gender_list if result > gender_first_std_deviation_start and result < gender_first_std_deviation_end]
gender_list_of_data_within_2_std_deviation = [result for result in gender_list if result > gender_second_std_deviation_start and result < gender_second_std_deviation_end]
gender_list_of_data_within_3_std_deviation = [result for result in gender_list if result >gender_third_std_deviation_start and result < gender_third_std_deviation_end]
#Percentage of data within 1, 2 and 3 Standard Deviations for math score
math_score_of_data_within_1_std_deviation = [result for result in math_score if result > math_first_std_deviation_start and result < math_first_std_deviation_end]
math_score_of_data_within_2_std_deviation = [result for result in math_score if result > math_second_std_deviation_start and result < math_second_std_deviation_end]
math_score_of_data_within_3_std_deviation = [result for result in math_score if result > math_third_std_deviation_start and result < math_third_std_deviation_end]
#Printing data for height and math score (Standard Deviation)
print("{}% of data for gender lies within 1 standard deviation".format(len(gender_list_of_data_within_1_std_deviation)*100.0/len(gender_list)))
print("{}% of data for gender lies within 2 standard deviations".format(len(gender_list_of_data_within_2_std_deviation)*100.0/len(gender_list)))
print("{}% of data for gender lies within 3 standard deviations".format(len(gender_list_of_data_within_3_std_deviation)*100.0/len(gender_list)))
print("{}% of data for maths score lies within 1 standard deviation".format(len(math_score_of_data_within_1_std_deviation)*100.0/len(math_score)))
print("{}% of data for maths score lies within 2 standard deviations".format(len(math_score_of_data_within_2_std_deviation)*100.0/len(math_score)))
print("{}% of data for maths score lies within 3 standard deviations".format(len(math_score_of_data_within_3_std_deviation)*100.0/len(math_score)))