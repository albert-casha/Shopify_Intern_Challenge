# Shopify_Intern_Challenge
 ## Question 1

The main issue with the calculation is that there is no filtering of the data. Looking at the dataset, there are two stores that are outliers: Store 42, where every order is for 2000 pairs of shoes, and Store 78, where the price per item is $25725. It seems likely to me that Store 42 is a wholesale retailer, and the data from Store 78 is likely missing a decimal point. If possible, I would investigate these two stores further, to try and validate these assumptions. Given the limited amount of information here, the data from these two stores should not be included in this assessment, and so must be filtered out.

I think it is still useful to know the AOV of all the sneaker shops, which I calculated to be $302.58. However, I think it would be more informative to see how the AOV changes per store. Rather than list 98 numbers, I created a histogram showing the AOV distribution. As seen, people typically spend between $250-$350, with the median value consistent with the combined AOV for all stores.

<p align="center">
<img src="https://github.com/albert-casha/Shopify_Intern_Challenge/blob/main/figures/AOV%20per%20Shop.png" width=50% height=50%/>
</p>

To see whether the AOV was dependent on who was buying the shoes, rather than the store selling them, I also plotted the AOV per customer (assuming that the user_id is consistent across stores). A similar trend emerges, where customers are most likely to spend between $250 - $350, and unlikely to spend more than $400 in a single transaction. 

<p align="center">
<img src="https://github.com/albert-casha/Shopify_Intern_Challenge/blob/main/figures/AOV%20per%20Customer.png" width=50% height=50%/>
</p>


Finally, I calculated the AOVs separately for new vs returning customers, and found them to be $297.68 and $302.90 respectively. When compared to the cost of a pair of shoes, the difference in these two numbers is neglibile, and so it seems that the AOV is independent of whether a customer has prevoiusly bought shoes on Shopify. 


## Question 2

### a.	How many orders were shipped by Speedy Express in total?

Speedy Express shipped 54 orders.

### b.	What is the last name of the employee with the most orders?

The last name of the employee with the most orders is Peacock.

### c.	What product was ordered the most by customers in Germany?

The product that was ordered the most was Boston Crab Meat, with 160 units shipped over 4 orders. However, the product with the most orders, regardless of total quantity sold, was Gorgonzola Telino with 5 orders placed.
