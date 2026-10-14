## 1.Executive Summary

NorthwoodFresh's Southeast region saw monthly revenue fall about $108,335, around 23% decrease, in the second half of the year. The 95% confidence interval puts the true drop between roughly $84,553 to $132,117 per month. The other three regions do not show any significant drop like the southeast region. At most, month-to-month variation. It is highly recommended that we find the root cause of Southeast region, focusing on what caused the change starting from month 7 before commiting to any changes. 

## 2.Finding

The analysis was prototyped on synthetic dataset, but based on the same shape and same expected pattern. It will only demonstrate how we use the methods, not get actual numbers. We split the Southeast 12 months into the first 6 months and the latter 6 months and compared the two. 

The average of the first 6 months is $472110.81 and the average of the second 6 months is $363775.88.
Effect Size is at $108334.94 with a  22.95% drop. 
The 85% confidence interval is $84,552.95 to $132,116.93. Only with 6 months each period, we have a huge interval but it is still a huge loss.
With the two-sample t-test at 8.93 and p=0.0000044, the chance that this sample of a true drop happening by luck is extremely small.

With this data, the drop is real and a huge amount. The data also tells us that this is not random noise but very much real.

## Recommendation

NorthwoodFresh should first rerun analysis on the actual data once it is ready. Examine in more depth of when the drop actually occured on the week of the drop. Check if any special event or season could explain the drop. Then check if there a reason, such as commpetition or management problem. Until we have the actual data, we should not take any measures that would major costs to do so. 

## AI Uses

I used Claude two times during this project. I used it on northwoodfresh_analysis.ipynb, trying to figure out how to add the IQR to the summary statstics. Claude told me to use lambda. The second time was verifiying the effective size, CI, t-statstic, and p-value. The results was similiar to the results I have receieved. 