File to run: 
--> nlp_project.py

Minimum Python version to run the file: 3.5
Library : APACHE SOLR 7.1.0


--------------------------------------------------------------------------------------


HOW TO RUN:

1. Create two Solr Cores : nlp-core1 and nlp-core2
2. Specify the location to save the documents from NLTK reuters corpus into your local folder
   e.g. fileName = "<your local path>" + str(i) + ".txt" LINE#:47 in code
3. To change the input sentence to be queried e.g. "coffee exports dropped over the years"  
	Refer LINE#: 36 in code


--> On the command line interface, type the file name along with the python extension, 
	Example: nlp_project.py

--> The program takes approximately 10 seconds to run

--> Indexing takes 10 mins.


--------------------------------------------------------------------------------------


OUTPUT:

--> The command line will display the Results of all the tasks.
--> The format of Output is as follows:
	- Input sentence
	- The matched sentence from the corpus with its ID
	- The matched sentence
	- The score of matching

e.g.

************************************ OUTPUT ******************************************

REGULAR SEARCH

-----------------------------------------------------------------------------------------------

Input sentence 1 :  coffee exports dropped over the years
The ID is '2338-1'.
The text is '['"The target is to raise exports to 20 pct of Gross Domestic Product over the next four years compared to 15 pct now," he said.']'.
The Score is '12.522194'.


The ID is '1745-10'.
The text is '['Exports to Western Europe eased 3.5 pct and Far East exports, due to an economic revival in Japan, dropped 5.2 pct.']'.
The Score is '12.023144'.


The ID is '2585-0'.
The text is '['THAI COFFEE EXPORTS RISE IN 1986 Thai coffee exports rose to 22,068 tonnes in 1986 from 20,430 a year earlier, the Customs Department said.']'.
The Score is '12.017353'.


The ID is '2013-1'.
The text is '['He said exporter registrations dropped from an average weekly 500 tonnes in March to 45 tonnes last week, with exports in coffee year 1986/87, ending September, forecast to total about 8,000 tonnes against 48,000 in 1985/86.']'.
The Score is '11.829805'.


The ID is '2013-0'.
The text is '["PHILIPPINE COFFEE EXPORTS SEEN FALLING SHARPLY Philippine coffee exports are expected to fall sharply due to a combination of the International Coffee Organisation's (ICO) decision not to revive export quotas and higher local prices, ICO Certifying Agency official Dante de Guzman told Reuters."]'.
The Score is '10.932764'.


The ID is '813-0'.
The text is '['ICO BOARD PASSES OVER COFFEE QUOTA ISSUE Executive board members of the International Coffee Organization, ICO, passed over the issue of export quota negotiations at its regular meeting here, delegates said.']'.
The Score is '10.838769'.


The ID is '2934-3'.
The text is '['French trade with Yugoslavia has grown little over the past two years.']'.
The Score is '10.5841055'.


The ID is '1528-0'.
The text is '['COFFEE FUTURES UNDER DLR A POUND AT SIX-YEAR LOW Coffee futures dipped further and closed below one dlr a pound for the first time in six years.']'.
The Score is '10.340917'.


The ID is '188-0'.
The text is '['ZIMBABWE COFFEE OUTPUT SET TO RISE Zimbabwean coffee output will reach 13,000 tonnes this year, up on just over 11,000 tonnes produced in 1986, the Commercial Coffee Growers Association said.']'.
The Score is '10.33176'.


The ID is '2697-0'.
The text is '["BRAZIL HAS NO SET COFFEE EXPORT TARGETS - IBC Brazil has no set target for its coffee exports following this week's breakdown of International Coffee Organization talks on export quotas, President of the Brazilian Coffee Institute, IBC, Jorio Dauster said."]'.
The Score is '10.331606'.



 DEEPER SEARCH

-----------------------------------------------------------------------------------------------

Saw 10 result(s). 

Input sentence 1 :  coffee exports dropped over the years 

The ID is '2013-1'.
The Sentence is '['He said exporter registrations dropped from an average weekly 500 tonnes in March to 45 tonnes last week, with exports in coffee year 1986/87, ending September, forecast to total about 8,000 tonnes against 48,000 in 1985/86.']'.
The Score is '861.7426'.


The ID is '1434-7'.
The Sentence is '['"I definitely see 90 cents and would not rule out a brief drop to 85 cents," said Debra Tropp, a coffee analyst with Prudential Bache.']'.
The Score is '728.2395'.


The ID is '813-12'.
The Sentence is '['There, the producers expressed their political will to negotiate basic quotas, particularly in the face of the damaging drop in coffee prices after the council failed to agree quotas, Montes said.']'.
The Score is '710.4506'.


The ID is '2013-3'.
The Sentence is '['Coffee production was expected to drop slightly to about one mln bags of 60 kg each in the 1986/87 crop year ending June from 1.1 mln bags last year, he said.']'.
The Score is '704.4379'.


The ID is '2569-0'.
The Sentence is '["COFFEE PRICE DROP NOT AFFECTING COLOMBIA'S DEBT the sharp fall in international coffee prices will not affect colombia's external credit situation, finance minister cesar gaviria told reuters."]'.
The Score is '675.013'.


The ID is '2910-4'.
The Sentence is '['Calls for a rescheduling of the debt have come this week from the opposition conservative party and the biggest trade union following the coffee price drop.']'.
The Score is '597.1971'.


The ID is '1518-0'.
The Sentence is '['COFFEE FUTURES AT SIX-YEAR LOW, UNDER 1 DLR/LB Coffee futures dipped further today and closed below 1 dlr a pound for the first time in six years.']'.
The Score is '574.96094'.


The ID is '1528-0'.
The Sentence is '['COFFEE FUTURES UNDER DLR A POUND AT SIX-YEAR LOW Coffee futures dipped further and closed below one dlr a pound for the first time in six years.']'.
The Score is '567.71484'.


The ID is '2585-0'.
The Sentence is '['THAI COFFEE EXPORTS RISE IN 1986 Thai coffee exports rose to 22,068 tonnes in 1986 from 20,430 a year earlier, the Customs Department said.']'.
The Score is '463.7874'.


The ID is '407-5'.
The Sentence is '['Coffee export quotas, used to regulate coffee prices under an International Coffee Agreement, were suspended a year ago when prices soared in response to a drought in Brazil.']'.
The Score is '443.20526'.



 SPECIALIZED DEEPER SEARCH

-----------------------------------------------------------------------------------------------

Saw 10 result(s). 

Input sentence 1 :  coffee exports dropped over the years 

The ID is '2013-1'.
The Sentence is '['He said exporter registrations dropped from an average weekly 500 tonnes in March to 45 tonnes last week, with exports in coffee year 1986/87, ending September, forecast to total about 8,000 tonnes against 48,000 in 1985/86.']'.
The Score is '770.2349'.


The ID is '813-12'.
The Sentence is '['There, the producers expressed their political will to negotiate basic quotas, particularly in the face of the damaging drop in coffee prices after the council failed to agree quotas, Montes said.']'.
The Score is '650.9953'.


The ID is '2013-3'.
The Sentence is '['Coffee production was expected to drop slightly to about one mln bags of 60 kg each in the 1986/87 crop year ending June from 1.1 mln bags last year, he said.']'.
The Score is '645.2108'.


The ID is '1434-7'.
The Sentence is '['"I definitely see 90 cents and would not rule out a brief drop to 85 cents," said Debra Tropp, a coffee analyst with Prudential Bache.']'.
The Score is '635.6073'.


The ID is '2569-0'.
The Sentence is '["COFFEE PRICE DROP NOT AFFECTING COLOMBIA'S DEBT the sharp fall in international coffee prices will not affect colombia's external credit situation, finance minister cesar gaviria told reuters."]'.
The Score is '621.8184'.


The ID is '2910-4'.
The Sentence is '['Calls for a rescheduling of the debt have come this week from the opposition conservative party and the biggest trade union following the coffee price drop.']'.
The Score is '527.40686'.


The ID is '1518-0'.
The Sentence is '['COFFEE FUTURES AT SIX-YEAR LOW, UNDER 1 DLR/LB Coffee futures dipped further today and closed below 1 dlr a pound for the first time in six years.']'.
The Score is '499.97958'.


The ID is '1528-0'.
The Sentence is '['COFFEE FUTURES UNDER DLR A POUND AT SIX-YEAR LOW Coffee futures dipped further and closed below one dlr a pound for the first time in six years.']'.
The Score is '493.62842'.


The ID is '2585-0'.
The Sentence is '['THAI COFFEE EXPORTS RISE IN 1986 Thai coffee exports rose to 22,068 tonnes in 1986 from 20,430 a year earlier, the Customs Department said.']'.
The Score is '462.65875'.


The ID is '407-5'.
The Sentence is '['Coffee export quotas, used to regulate coffee prices under an International Coffee Agreement, were suspended a year ago when prices soared in response to a drought in Brazil.']'.
The Score is '417.15283'.


Total Time Taken:  0.04  minutes

Process finished with exit code 0
