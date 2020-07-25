Q1. How many users does Wave have?

Ans1. select count(u_id) from business.users;


Q2. How many transfers have been sent in the currency CFA?

Ans2. SELECT count(send_money_currency) from business.transfers where send_money_currency = 'CFA';


Q3. How many different users have sent a transfer in CFA?

Ans3. SELECT count (distinct(u_id)) from business.transfers where send_money_currency = 'CFA';

Q4. How many agent_transactions did we have in the months of 2018 (broken down bymonth)?

Ans4. select count(u_id) from business.agent_transactions where date between '01/01/2018' and '12/31/2018'

Q5. Over the course of the last week, how many Wave agents were “net depositors” vs. “netwithdrawers”?

Ans5. 

Q6. Build an “atx volume city summary” table: find the volume of agent transactions createdin the last week, grouped by city.

Ans6. select count(atx_id) as "atx_volume_city_summary" from business.agent_transactions left outer join business.agents on
agent_transactions.agent_id = agents.agent_id where date between '01/01/2018' and '01/07/2018' group by city;

Ans6. select count(atx_id) as "atx_volume_city_summary" from business.agent_transactions left outer join business.agents on
agent_transactions.agent_id = agents.agent_id where date > current_date - interval '7 days' group by city;

Q7. Now separate the atx volume by country as well (so your columns should be country,city, volume)

Ans7.

Q10. Finally, which wallets have sent more than 10,000,000 CFA in transfers in the last month(as identified by 
the source_wallet_id column on the transfers table), and how much did they send?

Ans10. select source_wallet_id, send_money_scaler from business.transfers where send_money_scaler > '10000' and 
date > current_date - interval '31 days';