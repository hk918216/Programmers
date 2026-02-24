-- 코드를 입력하세요
SELECT A.TITLE, 
       A.BOARD_ID, 
       B.REPLY_ID, 
       B.WRITER_ID,
       B.CONTENTS, 
       TO_CHAR(B.CREATED_DATE, 'YYYY-MM-DD') as CREATED_DATE
  from USED_GOODS_BOARD A
  join USED_GOODS_REPLY B
    on A.BOARD_ID = B.BOARD_ID
 where to_char(A.CREATED_DATE, 'YYYY-MM') = '2022-10'
 order by B.CREATED_DATE, A.TITLE
