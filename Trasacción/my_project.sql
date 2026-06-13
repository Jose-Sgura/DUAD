DO $$
DECLARE
    v_user_id INT := 1;
    v_bill_id INT;
    v_stock INT;

BEGIN

#
Confirmar que el usuario que realiza la compra existe en la DB.
    IF NOT EXISTS (SELECT 1 FROM users WHERE id = v_user_id) THEN
        RAISE EXCEPTION 'The user with id % does not exist.', v_user_id;
    END IF;

#Comprobar si hay existencias suficientes de cada uno de los productos dentro de la factura.
SELECT stock INTO v_stock from products WHERE id =1;
IF v_stock < 2 THEN
    RAISE EXCEPTION 'Not enough stock for product with id %.', v_stock;
END IF;

SELECT stock INTO v_stock from products WHERE id =3;
IF v_stock < 4 THEN
    RAISE EXCEPTION 'Not enough stock for product with id %.', v_stock;
END IF;



#Insertar la factura con el usuario relacionado
INSERT INTO bills (user_id, total, status) 
VALUES (v_user_id,0.00,'pending')
RETURNING id INTO v_bill_id;

INSERT INTO bill_item (bill_id, product_id, quantity, unit_price)
VALUES (v_bill_id, 1, 2, 999.99),
(v_bill_id, 3, 4, 29.99);

#Reducir el stock de los productos según la cantidad comprada.
UPDATE products SET stock  = stock - 2 WHERE id = 1;
UPDATE products SET stock  = stock - 4 WHERE id = 3;

UPDATE bills 
SET total = (
    SELECT SUM(quantity * unit_price)
    FROM bill_item
    WHERE bill_id = v_bill_id
) 
WHERE id = v_bill_id;

RAISE NOTICE 'Buy process completed successfully. Bill ID:%', v_bill_id;



EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'An error occurred: %', SQLERRM;

END; $$ language plpgsql;


