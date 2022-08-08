
SELECT DISTINCT monthh,weekofmonth,dayofweek,
ROUND(SUM(fraudfound_p) OVER(PARTITION BY monthh)::numeric/COUNT(fraudfound_p) 
	  OVER(PARTITION BY monthh)*100,2) AS percentage_fraud_month,
ROUND(SUM(fraudfound_p) OVER(PARTITION BY monthh,weekofmonth)::numeric/COUNT(fraudfound_p) 
	  OVER(PARTITION BY monthh, weekofmonth)*100,2) AS percentage_fraud_month_week,
ROUND(SUM(fraudfound_p) OVER(PARTITION BY monthh,weekofmonth,dayofweek)::numeric/COUNT(fraudfound_p) OVER(PARTITION BY monthh,weekofmonth,dayofweek)*100,2) AS percentage_fraud_month_week_day
FROM public.fraudes
ORDER BY monthh, weekofmonth;
