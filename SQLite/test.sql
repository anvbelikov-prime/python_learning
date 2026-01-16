SELECT
	t.id  as id,
	t.num as num
FROM test as t
WHERE MOD(t.id,  2) == 0;
 
