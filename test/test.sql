
SELECT
	s.name
FROM
	salesperson s
	join orders o on s.id=o.salesperson_id
	join customer c on c.id=o.custid
	and c.name='Samsonic'
	

SELECT
	s.name
FROM
	salesperson s
	join orders o on s.id=o.salesperson_id
	left join customer c on c.id=o.custid and c.name='Samsonic'
	

SELECT
	s.name
FROM
	salesperson s
	join orders o on s.id=o.salesperson_id
group by s.name
having count(s.name) >= 2


SELECT
	s.name
FROM
	salesperson s
	join orders o on s.id=o.salesperson_id
group by s.name
having sum(amount) > 1400

