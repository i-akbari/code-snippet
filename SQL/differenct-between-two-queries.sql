--first query
select A.RegNum, B.RegNum
from Funds_Fact_NAV0_Historical_New A
         right join Funds_Fact_NAV2_Historical_Revised_New B on A.RegNum = B.RegNum and A.date = '2025-08-22'
where A.RegNum is null and B.date = '2025-08-22';

--second query
select A.RegNum, B.RegNum
from Funds_Fact_NAV0_Historical_New A
right join Funds_Fact_NAV2_Historical_Revised_New B
on A.RegNum = B.RegNum
   and A.date = '2025-08-22'
   and B.date = '2025-08-22'
where A.RegNum is null;


--the difference
Query 1: Shows only unmatched B records from 2025-08-22 (27 records)
Query 2: Shows ALL unmatched B records across the entire historical table (1+ million records)
The RIGHT JOIN preserves all B records when there's no match in A, but Query 1 then filters these down to just one date, while Query 2 keeps all historical unmatched records.  Query 1 is likely what you want if you're looking for records that exist in B but not in A for a specific date.
