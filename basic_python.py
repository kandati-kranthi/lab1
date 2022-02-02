import statistics as st

l = [2,3,4,1,7,8,2,3,4,5,1,8,5,6,8,2]
## printing the mean of the data.
print('Mean of data is {}'.format(st.mean(l)))
## printing the median of the data.
print('Median of data is {}'.format(st.median(l)))
## Printing the mode of the data, but here it will generate error because here in this ## data two value are most occuring,hence not able to handle.
print('Mode of the data is {}'.format(st.mode(l)))

#[Output]:
#Mean of data is 4.3125
#Median of data is 4.0

#---------------------------------------------------------------------------
#StatisticsError                           Traceback (most recent call last)
#<ipython-input-2-f297ad04a792> in <module>()
#      8 
#      9 ## Printing the mode of the data, but here it will generate error because here in this data two value are most occuring,hence not able to handle.
#---> 10 print('Mode of the data is {}'.format(st.mode(l)))
#~AppDataLocalContinuumanaconda2envspy35libstatistics.py in mode(data)
#    472     elif table:
#    473         raise StatisticsError(
#--> 474                 'no unique mode; found %d equally common values' % len(table)
#    475                 )
#    476     else:
#StatisticsError: no unique mode; found 2 equally common values


## Checking the mode value for another dataset
l1 = [1,2,2,3,4]
## Here it is working fine.
print(st.mode(l1))

#[Output]:
2


