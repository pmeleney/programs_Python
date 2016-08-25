# zScore_numSamples

#### zScore_numSamples[numSamples, OneSided = False, zTable_min = 1, zTable_max = 6.001, zStep = 0.001]

Provides a test for whether outliers are caused by stochastic error or some other influence.  The function takes the number of samples in a dataset and returns the number of standard deviations beyond which one would expect to see a single data point 50% of the time.  If there exist many outliers beyond this number of standard deviations away, then the outliers are probably caused by some influence other than stochastic error.

The actual rate of occurrence is limited by the zStep, this is accounted for in the results by printing the actual number of samples at which one can expect to see one occurrence.  This value is rounded to the nearest whole number. Since it is constant in zStep is not constant in numSamples, the calculation becomes much less accurate as Z increases.  I chose 8.0 as the default zTable_max because erf(9.0/np.sqrt(2)) is beyond the precision of the default float variable.

#### Parameters:

***numSamples: [int]*** The number of samples in the dataset.  
***OneSided: [bool, default False]*** Specify one sided or two sided test.  Normally this will be false.  
***zTable_min: [int or float, default 1]*** Minimum range of standard deviations.   
***zTable_max: [int or float, default 6.001]*** Maximum range of standard deviations to be checked.  
***zStep = 0.001: [float, default 0.001]*** Precision of calculation.  The program will return the nearest z score to this level of precision.