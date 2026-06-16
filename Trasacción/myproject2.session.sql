DO $$
DECLARE
    v_bill_id INT := 1;

BEGIN
    IF NOT EXISTS (SELECT 1 FROM bills WHERE id = v_bill_id) THEN
        RAISE EXCEPTION 'The invoice with id % does not exist', v_bill_id;
    END IF;

    IF NOT EXISTS (SELECT 1 FROM bills WHERE id = v_bill_id AND status = 'pending') THEN
        RAISE EXCEPTION 'The invoice % is not in pending status. It cannot be canceled', v_bill_id;  -- ❌ faltaba la coma y v_bill_id
    END IF;

    UPDATE products
    SET stock = stock + bi.quantity
    FROM bill_item bi
    WHERE products.id = bi.product_id
    AND bi.bill_id = v_bill_id
    AND bi.delivered = FALSE;

    UPDATE bills
    SET status = 'cancelled'
    WHERE id = v_bill_id;

    RAISE NOTICE 'The invoice % deleted, Stock up to date only for not delivered products', v_bill_id;

EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Transaction called off: %', SQLERRM;

END;
$$ LANGUAGE plpgsql;