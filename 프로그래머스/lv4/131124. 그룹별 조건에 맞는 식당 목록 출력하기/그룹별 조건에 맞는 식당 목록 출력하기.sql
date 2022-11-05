-- 코드를 입력하세요
SELECT M.MEMBER_NAME AS MEMBER_NAME,
       R.REVIEW_TEXT AS REVIEW_TEXT,
       TO_CHAR(R.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
  FROM MEMBER_PROFILE M JOIN REST_REVIEW R
    ON M.MEMBER_ID = R.MEMBER_ID
 WHERE R.MEMBER_ID IN (SELECT MEMBER_ID
                         FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                       HAVING COUNT(*) 
                       = 
                       (SELECT MAX(COUNT(*))
                         FROM REST_REVIEW
                        GROUP BY MEMBER_ID)
                       )
 ORDER BY REVIEW_DATE, REVIEW_TEXT