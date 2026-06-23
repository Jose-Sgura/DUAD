--se actuliza tabla prouducts para dejar stock en 1 y version también.
UPDATE products SET stock = 1, version = 1 WHERE id = 1;

--se agrega columna version a la tabla producto
--para llevar un indicador de cambio
ALTER TABLE products 
ADD COLUMN version in DEFAULT 1;

DO $$
DECLARE
    v_user_id      INT := 1;
    v_product_id   INT := 1;
    v_quantity     INT := 1;
    v_bill_id      INT;
    v_stock        INT;
    v_version      INT;
    v_rows_updated INT;

BEGIN
    IF NOT EXISTS (SELECT 1 FROM users WHERE id = v_user_id) THEN
        RAISE EXCEPTION 'The user % does not exist', v_user_id;
    END IF;

    SELECT stock, version INTO v_stock, v_version
    FROM products
    WHERE id = v_product_id;

    RAISE NOTICE 'Read stock: %, Read version: %', v_stock, v_version;

    IF v_stock < v_quantity THEN
        RAISE EXCEPTION 'The stock is not enough. Available: %, Requested: %', v_stock, v_quantity;
    END IF;

    INSERT INTO bills (user_id, total, status)
    VALUES (v_user_id, 0.00, 'pending')
    RETURNING id INTO v_bill_id;

--Usé una transacción que lea el stock y actualicé solo si el stock no cambió en el proceso
    
    UPDATE products
    SET stock   = stock - v_quantity,
        version = version + 1
    WHERE id      = v_product_id
    AND   version = v_version
    AND   stock   >= v_quantity;

    GET DIAGNOSTICS v_rows_updated = ROW_COUNT;

--Si otro proceso modificó el stock mientras tanto, debe abortar la compra
    IF v_rows_updated = 0 THEN
        RAISE EXCEPTION 'Aborted buy, another process modified the stock from product %', v_product_id;
    END IF;

    INSERT INTO bill_item (bill_id, product_id, quantity, unit_price)
    SELECT v_bill_id, id, v_quantity, price
    FROM products WHERE id = v_product_id;

    UPDATE bills
    SET total = (
        SELECT SUM(quantity * unit_price)
        FROM bill_item
        WHERE bill_id = v_bill_id
    )
    WHERE id = v_bill_id;

    RAISE NOTICE 'Successful buy. Invoice ID: %, Product ID: %, New version: %',
        v_bill_id, v_product_id, v_version + 1;

EXCEPTION
    WHEN OTHERS THEN
        RAISE EXCEPTION 'Transaction aborted: %', SQLERRM;

END;
$$ LANGUAGE plpgsql;