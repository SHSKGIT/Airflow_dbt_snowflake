SELECT
    COUNT(id) AS location_count
FROM {{ ref('prepared_data') }}
GROUP BY
    location