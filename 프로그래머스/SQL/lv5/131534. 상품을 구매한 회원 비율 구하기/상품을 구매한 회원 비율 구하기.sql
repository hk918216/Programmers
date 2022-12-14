-- 코드를 입력하세요
SELECT TO_CHAR(SALES_DATE, 'YYYY') YEAR,
       TO_NUMBER(TO_CHAR(SALES_DATE, 'MM')) MONTH,
       COUNT(DISTINCT OS.USER_ID) PURCHASED_USERS,
       ROUND(COUNT(DISTINCT OS.USER_ID) / (SELECT COUNT(JOINED) 
                                    FROM USER_INFO
                                   WHERE TO_CHAR(JOINED, 'YYYY') = '2021'),1) AS        PURCHASE_RATIO
  FROM USER_INFO UI JOIN ONLINE_SALE OS
    ON UI.USER_ID = OS.USER_ID
 WHERE TO_CHAR(JOINED, 'YYYY') = '2021'
 GROUP BY TO_CHAR(SALES_DATE, 'YYYY'),
          TO_NUMBER(TO_CHAR(SALES_DATE, 'MM'))
 ORDER BY YEAR, MONTH
  
