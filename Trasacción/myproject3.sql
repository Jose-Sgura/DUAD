DO $$
DECLARE
    v_user_id INT :=1;
    v_bill_id INT;
    v_stock INT;
    v_item RECORD;

BEGIN
IF NOT EXISTS(SELECT 1 FROM users WHERE id = v_user_id) THEN
 RAISE EXCEPTION 'User % does not exist', v_user_id;
END IF;

FOR v_item IN
    SELECT * FROM (VALUES
        (1,2),
        (2,3),
        (3,5)
    ) AS items(product_id, quantity)
LOOP
    SELECT stock INTO v_stock FROM products WHERE id = v_item.product_id;

    IF v_stock IS NULL THEN
    RAISE EXCEPTION 'Product id % does not exist', v_item.product_id;
    END IF;

    IF v_stock < v_item.quantity THEN
    RAISE EXCEPTION 'Not enough stock for product %, Available %,
    Requested %', v_item.product_id, v_stock, v_item.quantity;
    END IF;

END LOOP;

INSERT INTO bills (user_id, total, status)
VALUES (v_user_id, 0.00, 'pending')
RETURNING id INTO v_bill_id;

FOR v_item IN 
SELECT * FROM (VALUES
    (1,2),
    (2,3),
    (3,5)
) AS items(product_id, quantity)
LOOP
    INSERT INTO bill_item (bill_id, product_id, quantity, unit_price)
    SELECT v_bill_id, id, v_item.quantity, price
    FROM products WHERE id = v_item.product_id;

    UPDATE products SET stock = stock - v_item.quantity
    WHERE id = v_item.product_id;
END LOOP;

UPDATE bills
SET total = (
    SELECT SUM(quantity*unit_price)
    FROM bill_item
    WHERE bill_id = v_bill_id
)

WHERE id = v_bill_id;

RAISE NOTICE 'Massive buy Successful. Invoice ID: %, Total:%', v_bill_id, 
(SELECT total FROM bills WHERE id = v_bill_id);

EXCEPTION
WHEN OTHERS THEN
 RAISE EXCEPTION 'Transaction aborted %', SQLERRM;

END;

$$ LANGUAGE plpgsql;
