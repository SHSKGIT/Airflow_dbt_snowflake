SELECT
    id,
    first_name,
    last_name
FROM {{ ref('customer_data') }}