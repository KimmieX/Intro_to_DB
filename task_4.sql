-- Use the database passed as an argument
USE alx_book_store;

-- Query to get the full description of the Books table
SELECT 
    COLUMN_NAME AS 'Column Name',
    DATA_TYPE AS 'Data Type',
    CHARACTER_MAXIMUM_LENGTH AS 'Max Length',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_DEFAULT AS 'Default Value'
FROM 
    information_schema.COLUMNS
WHERE 
    TABLE_NAME = 'Books' 
    AND TABLE_SCHEMA = 'alx_book_store';
