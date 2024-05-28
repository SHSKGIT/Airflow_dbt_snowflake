{{ dbt_utils.union_relations(
    relations=[ref('travel_data_1'), ref('travel_data_2')]
) }}