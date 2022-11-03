-- 코드를 입력하세요
SELECT a.apnt_no,
       p.pt_name, 
       a.pt_no, 
       a.mcdp_cd, 
       d.dr_name, 
       a.apnt_ymd
  from APPOINTMENT a 
  join patient p
    on a.pt_no = p.pt_no
  join doctor d
    on a.mddr_id = d.dr_id
 where to_char(apnt_ymd, 'YYYY-MM-DD') = '2022-04-13'
   and apnt_cncl_yn = 'N'
   and a.mcdp_cd = 'CS'
 order by apnt_ymd

