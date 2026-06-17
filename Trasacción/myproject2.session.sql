DO $$
DECLARE
    v_user_id INT := 1;
    v_bill_id INT;
    v_stock INT;

    v_qty_p1 INT := 2;
    v_qty_p2 INT := 3;
    v_qty_p3 INT := 5;

BEGIN

IF NOT EXISTS (SELECT 1 FROM users WHERE id = v_user_id)
THEN RAISE EXCEPTION 'The user id % does not exist', v_user_id;
END IF;


SELECT stock INTO v_stock FROM products WHERE id = 1;
IF v_stock < v_qty_p1 
THEN RAISE EXCEPTION 'Stock is not enough for product id =1. Enable: %, Requested: %',v_stock, v_qty_p1; 
END IF;

SELECT stock INTO v_stock FROM products WHERE id = 2;
IF v_stock < v_qty_p2 
THEN RAISE EXCEPTION 'Stock is not enough for product id =2. Enable: %, Requested: %',v_stock, v_qty_p2;
END IF;

SELECT stock INTO v_stock FROM products WHERE id = 3;
IF v_stock < v_qty_p3 
THEN RAISE EXCEPTION 'Stock is not enough for product id =3. Enable: %, Requested: %',v_stock, v_qty_p3;
END IF;

INSERT INTO bills (user_id, total, status)
VALUES (v_user_id, 0.00, 'pending')
RETURNING id INTO v_bill_id;

INSERT INTO bill_item (bill_id, product_id, quantity, unit_price)
SELECT v_bill_id, id,
    CASE id
        WHEN 1 THEN v_qty_p1
        WHEN 2 THEN v_qty_p2
        WHEN 3 THEN v_qty_p3
    END,
    price
FROM products
WHERE id IN (1,2,3);

UPDATE products SET stock = stock - v_qty_p1 WHERE id = 1;
UPDATE products SET stock = stock - v_qty_p2 WHERE id = 2;
UPDATE products SET stock = stock - v_qty_p3 WHERE id = 3;

UPDATE bills
SET total = (
    SELECT SUM (quantity * unit_price)
    FROM bill_item
    WHERE bill_id = v_bill_id
)

WHERE id = v_bill_id;

RAISE NOTICE 'Massive buy successfully. Invoice id: %, total: %', 
v_bill_id,
(SELECT total FROM bills WHERE id = v_bill_id);

EXCEPTION
    WHEN OTHERS THEN
    RAISE EXCEPTION 'Transaction called off: %', SQLERRM;

END;
$$ LANGUAGE plpgsql;
