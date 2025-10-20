-- with list as(
-- select s.*
-- from _tmp01_list l
-- join account_staff s on concat(lower(l.mail), '@emofid.com') = lower(s.email)
-- where type = N'راهنما'
-- limit 1
-- )
--
-- update account_staff
-- set is_guide = true
-- where account_staff.id = list.id


update account_staff
set is_guide = True, extra_info = N'گرفتن نقش راهنما'
from _tmp01_list
where account_staff.email = concat(lower(_tmp01_list.mail), '@emofid.com') and _tmp01_list.type = N'راهنما'

-- where account_staff.email = concat(lower(_tmp01_list.mail), '@emofid.com') and _tmp01_list.type = N'راهنما'

select _tmp01_list.*, account_staff.*
from account_staff
left join _tmp01_list on account_staff.email = concat(lower(_tmp01_list.mail), '@emofid.com')
where _tmp01_list.type = N'راهنما'

select *
from account_staff
where extra_info = N'گرفتن نقش راهنما'
