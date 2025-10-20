UPDATE customer_customer
SET is_block = backup.is_block
FROM customer_customer_14040727 backup
WHERE customer_customer.national_code = backup.national_code;
-------------------------------------------------------------------------
UPDATE customer_customer
SET is_block = (
    SELECT backup.is_block 
    FROM customer_customer_14040727 backup 
    WHERE backup.national_code = customer_customer.national_code
)
WHERE national_code IN (
    SELECT national_code 
    FROM customer_customer_14040727
);
-------------------------------------------------------------------------
