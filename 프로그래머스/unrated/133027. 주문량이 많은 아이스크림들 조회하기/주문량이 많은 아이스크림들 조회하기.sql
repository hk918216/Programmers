-- 코드를 입력하세요
-- SELECT flavor, total_order
--   from first_half

-- select flavor, total_order
--   from july

select T.flavor
  from (select b.flavor, sum(b.total_order)+sum(a.total_order) as total
          from first_half b join july a
            on b.flavor = a.flavor
         group by b.flavor
         order by total desc)  T
 where rownum < 4