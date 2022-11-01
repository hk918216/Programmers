-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, 
        to_char(HIRE_YMD, 'YYYY-MM-DD') as HIRE_YMD
  from doctor
 where mcdp_cd = 'CS' or mcdp_cd='GS'
 order by HIRE_YMD desc, dr_name