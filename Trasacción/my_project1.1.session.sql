DO $$
DECLARE
    v_bill_id INT := 4;
    v_exists INT;
BEGIN

IF NOT EXISTS (SELECT 1 FROM bills WHERE id = v_bill_id) THEN
    RAISE EXCEPTION 'The invoice id % does not exist ', v_bill_id;
END IF;

IF EXISTS (SELECT 1 FROM bills WHERE id = v_bill_id AND status = 'returned')
THEN RAISE EXCEPTION 'The invoice % has been already been returned', v_bill_id;
END IF;

UPDATE products
SET stock = stock + bi.quantity
FROM bill_items bi
WHERE products.id = bi.product_id
AND bi.bill_id = v_bill_id;

UPDATE bills
SET status = 'returned'
WHERE id = v_bill_id;

RAISE NOTICE 'Returning proceed succesfully for the invoice %', v_bill_id;

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'Transaction failed: %', SQLERRM;

END; $$ language plpgsql;