# Covid-19-Science-Fair-Project

# Determining Which Factors Lead to Death by Covid-19


# Hypothesis

I hypothesize that if someone has COVID, then having a respiratory disease will contribute to their mortality rate to the greatest extent because COVID-19 is a disease that attacks the lungs, and the lungs are already severely weakened if you have a respiratory disease.


# Background

CoronaVirus Disease, or COVID-19 has led to the deaths of 1,193,026 Americans, making it one of the deadliest pandemics in recent history. COVID-19 has severely impacted the global economy. It forced new policies such as social distancing. It also made learning and working a lot harder for many people. Students couldn’t visit their school, and were forced to learn from home. Many blue collar workers lost their jobs. But arguably the worst impact of COVID-19 is the huge number of deaths that were caused by it. While on average only about 1% of people with COVID die, there are many other factors such as age and pre-existing conditions that can make this number much higher. 


# Purpose

The purpose of this experiment is to learn more about the different factors leading to deaths, and to be able to predict the likelihood of someone dying of COVID-19. Also, learning how and why each factor impacts COVID-19 as much as it did. Also, using AI, it is possible to test different factors such as if they were hospitalized or not. Such factors may seem meaningful, but knowing to what extent they impact the mortality rate is much more important. 


# Abstract

The purpose of this experiment is to learn more about the different factors leading to deaths, and to be able to predict the likelihood of someone dying of COVID-19. I plan on finding the amount of people who died with each pre-existing condition along with COVID using a dataset. I will also, with the help of a different data set, find the amount of people who died with each pre-existing condition. Since one data set may be bigger than the other, I will make sure my numbers are of the same scale. Then, after dividing those who died with each pre-existing condition with COVID by the number of people that died with each pre-existing condition and COVID, I will then find the mortality rate of each pre-existing condition. I plan to do the same thing except for age as well. After finishing this process, I will know which factors influence the mortality rate a lot, and which influence it a little. 


# Conclusion

Respiratory diseases are by far the most impacting factors when it comes to COVID-19 deaths. Respiratory diseases such as COPD (Chronic obtrusive pulmonary disease) and Pneumonia can almost guarantee death to those who have COVID-19.  Lung diseases by far have the highest mortality rate, at 98.3%. Sepsis is in second place with 67%. This shows that 98% of people with respiratory diseases die if they have COVID, compared to only about 1% of COVID patients dying, in America at least. Also, Sepsis only accounts for 3.1% of COVID deaths, and 32.9% of people who died from COVID have some form of Respiratory disease. However, even tumors and dementia had a high mortality rate. The dementia is likely influencing mortality rate due to the fact that it may cause pneumonia. When it comes to ages, those who are older than 85 have the highest likelihood of dying. This is mainly due to the weakening of the immune system (immunosenescence), which makes it take longer for the immune system to respond to the threat. This allows COVID to spread throughout the body, and attack the lungs.




# Practical Implications

Being able to know the mortality rate of each age and pre-existing condition along with COVID can be extremely important. If you had COVID, it would be very useful to know if you have a high chance to live or not. This also reveals many new things about the tendencies of COVID. Sepsis and respiratory illness are very deadly with COVID. Most of the respiratory diseases, such as COPD and Bronchitis are caused by smoking. This also proves that smoking can increase the likelihood of death from COVID-19. To conclude, this experiment is important in the real world because you can know the probability of one’s death if they have COVID, and it also reveals many new things about the factors that impact COVID.



**References**


    _Conditions Contributing to COVID-19 Deaths, by State and Age, Provisional 2020-2023 - Catalog_. (n.d.). Dataset - Catalog. Retrieved January 22, 2024, from https://catalog.data.gov/dataset/conditions-contributing-to-deaths-involving-coronavirus-disease-2019-covid-19-by-age-group


    _COVID-19 Case Surveillance Public Use Data - Catalog_. (2020, May 15). Dataset - Catalog. Retrieved January 22, 2024, from https://catalog.data.gov/dataset/covid-19-case-surveillance-public-use-data


    _COVID-19 Lung Damage_. (2022, February 28). Johns Hopkins Medicine. Retrieved January 22, 2024, from https://www.hopkinsmedicine.org/health/conditions-and-diseases/coronavirus/what-coronavirus-does-to-the-lungs


    _COVID-19 outbreak: Impact on global economy - PMC_. (2023, January 30). NCBI. Retrieved January 22, 2024, from https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9923118/


    _FastStats - Chronic Lower Respiratory Disease_. (n.d.). CDC. Retrieved January 22, 2024, from https://www.cdc.gov/nchs/fastats/copd.htm


    _Products - Data Briefs - Number 446 - October 2022_. (2022, October 13). CDC. Retrieved January 22, 2024, from https://www.cdc.gov/nchs/products/databriefs/db446.htm


    _Quick kidney disease facts and stats_. (n.d.). American Kidney Fund. Retrieved January 22, 2024, from https://www.kidneyfund.org/all-about-kidneys/quick-kidney-disease-facts-and-stats


    _United States Coronavirus COVID-19 Deaths_. (n.d.). Trading Economics. Retrieved January 22, 2024, from https://tradingeconomics.com/united-states/coronavirus-deaths


    _United States COVID - Coronavirus Statistics_. (n.d.). Worldometer. Retrieved January 22, 2024, from https://www.worldometers.info/coronavirus/country/us/

Procedure:



1. Download the dataset from [https://catalog.data.gov/dataset/conditions-contributing-to-deaths-involving-coronavirus-disease-2019-covid-19-by-age-group](https://catalog.data.gov/dataset/conditions-contributing-to-deaths-involving-coronavirus-disease-2019-covid-19-by-age-group)
2. Load the dataset as a Pandas dataframe
3. Create charts of the data using matplotlib or google sheets
4. Find the amount of people who died with each pre-existing condition and age (Increments of 9)
5. Download the dataset from [https://www.google.com/url?q=https://catalog.data.gov/dataset/covid-19-case-surveillance-public-use-data&sa=D&source=docs&ust=1706841307961025&usg=AOvVaw2ZS72CuRM7vMnjeIYUgiW2](https://www.google.com/url?q=https://catalog.data.gov/dataset/covid-19-case-surveillance-public-use-data&sa=D&source=docs&ust=1706841307961025&usg=AOvVaw2ZS72CuRM7vMnjeIYUgiW2)
6. Load the dataset as a Pandas dataframe
7. Use Pandas to find the amount of people in this dataset who had COVID
8. Use this dataset to find the number of people who had a pre-existing condition.
9. Find the number of people who died in this dataset. 
10. Compare the number of people who died in the first dataset to the number of people who died in the second data set.
11. Multiply and divide all of the numbers in one dataset so that they both have the same scale factor (number of people who died.)
12. Use [https://www.cdc.gov/nchs/fastats/default.htm](https://www.cdc.gov/nchs/fastats/default.htm) to find out how many people had each pre-existing condition. (They don’t need to have COVID, they just need to have the pre-existing condition.) These results should apply to Americans only.
13. If this only includes data from one year, multiply it by the years that have passed since 2020. (When the datasets about covid started recording data.)
14. Add all of these numbers together to get the amount of people with any of the pre-existing conditions. (They don’t need to have COVID).
15. Find the number of people who had COVID and a pre-existing condition, which you should already have from the second data set. (Step 8)
16. Divide the number of people with COVID and a pre-existing condition by the number of people with any of the pre-existing conditions. This is the percentage of people who had COVID along with a pre-existing condition.
17. Divide the number of people who died with a specific pre-existing condition by the number of people who had COVID and the pre-existing condition. To find the number of people who had covid and the pre-existing condition, multiply the amount of people who have the condition who may not have COVID by the percentage that you got in step 16.
18. When you do this, you will get a number that is the mortality rate of each condition and covid.
19. Divide the amount of people who died of covid in each age from the 1st dataset by the amount of people in each age who had covid from the 2nd dataset. Make sure that they still have the same scale factor. 
20. You now have mortality rates for all pre-existing conditions as well as the mortality rate for each age. Graph your results or put them in a table.
