/* Using the following database, write a Prolog query to find all the surgeons who live in Texas and make over 100,000 dollars in a year. You will have to add some additional data, such as about different types ofsurgeons, city-state relationships. */

occupation(joe,oral_surgeon).
occupation(sam,patent_laywer).
occupation(bill,trial_laywer).
occupation(cindy,investment_banker).
occupation(joan,civil_laywer).
occupation(len,plastic_surgeon).
occupation(lance,heart_surgeon).
occupation(frank,brain_surgeon).
occupation(charlie,plastic_surgeon).
occupation(lisa,oral_surgeon).

address(joe,houston).
address(sam,pittsburgh).
address(bill,dallas).
address(cindy,omaha).
address(joan,chicago).
address(len,college_station).
address(lance,los_angeles).
address(frank,dallas).
address(charlie,houston).
address(lisa,san_antonio).

salary(joe,50000).
salary(sam,15000).
salary(bill,200000).
salary(cindy,140000).
salary(joan,80000).
salary(len,70000).
salary(lance,650000).
salary(frank,85000).
salary(charlie,120000).
salary(lisa,190000).

surgeon(plastic_surgeon).
surgeon(heart_surgeon).
surgeon(brain_surgeon).
surgeon(oral_surgeon).

city_state(houston, texas).
city_state(dallas, texas).
city_state(college_station, texas).
city_state(san_antonio, texas).

surgeonswithsalary(X,Y,Z) :- surgeon(O), occupation(X,O), address(X,K), city_state(K,Z), salary(X,V), V>Y.
% X is a surgeon with greater than Y salary who lives in Z state
% Use the following query to find all the surgeons who live in texas and earn over $100,000 --- "surgeonswithsalary(X,100000, texas)."