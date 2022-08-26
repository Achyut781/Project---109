import random
import plotly.figure_factory as ff
import statistics
dice_result = []

for i in range(0, 1000):
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)
    dice_result.append(dice_1+dice_2)
mean = sum(dice_result)/len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std_deviation = statistics.stdev(dice_result)
print(mean)
print(median)
print(mode)
print(std_deviation)
fig = ff.create_distplot([dice_result], ['Result'], show_hist = False)
fig.show()
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
list_of_data_within_1_standardDeviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
print('{}%  of data lies within 1 standard deviation'.format(len(list_of_data_within_1_standardDeviation)*100.0/len(dice_result)))

second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
list_of_data_within_2_standardDeviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
print('{}%  of data lies within 2 standard deviation'.format(len(list_of_data_within_2_standardDeviation)*100.0/len(dice_result)))

third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)
list_of_data_within_3_standardDeviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]
print('{}%  of data lies within 3 standard deviation'.format(len(list_of_data_within_3_standardDeviation)*100.0/len(dice_result)))