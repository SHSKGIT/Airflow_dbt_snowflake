SELECT
    A.id,
    A.first_name,
    A.last_name,
    B.location,
    B.cost
FROM {{ ref('customer') }} AS A
JOIN {{ ref('combined_travel_data') }} AS B
    ON A.id = B.id