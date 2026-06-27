-- Table: public.bill_item

-- DROP TABLE IF EXISTS public.bill_item;

CREATE TABLE IF NOT EXISTS public.bill_item
(
    id integer NOT NULL DEFAULT nextval('bill_item_id_seq'::regclass),
    bill_id integer NOT NULL,
    product_id integer NOT NULL,
    quantity integer NOT NULL,
    unit_price numeric(10,2) NOT NULL,
    delivered boolean DEFAULT false,
    CONSTRAINT bill_item_pkey PRIMARY KEY (id),
    CONSTRAINT bill_item_bill_id_fkey FOREIGN KEY (bill_id)
        REFERENCES public.bills (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT bill_item_product_id_fkey FOREIGN KEY (product_id)
        REFERENCES public.products (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.bill_item
    OWNER to postgres;

-- Table: public.bills

-- DROP TABLE IF EXISTS public.bills;

CREATE TABLE IF NOT EXISTS public.bills
(
    id integer NOT NULL DEFAULT nextval('bills_id_seq'::regclass),
    user_id integer NOT NULL,
    total numeric(10,2) DEFAULT 0.00,
    status character varying(50) COLLATE pg_catalog."default" DEFAULT 'pending'::character varying,
    CONSTRAINT bills_pkey PRIMARY KEY (id),
    CONSTRAINT bills_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES public.users (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.bills
    OWNER to postgres;

-- Table: public.categories

-- DROP TABLE IF EXISTS public.categories;

CREATE TABLE IF NOT EXISTS public.categories
(
    id integer NOT NULL DEFAULT nextval('categories_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT categories_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.categories
    OWNER to postgres;

-- Table: public.products

-- DROP TABLE IF EXISTS public.products;

CREATE TABLE IF NOT EXISTS public.products
(
    id integer NOT NULL DEFAULT nextval('products_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    price numeric(10,2) NOT NULL,
    stock integer NOT NULL,
    category_id integer NOT NULL,
    version integer DEFAULT 1,
    CONSTRAINT products_pkey PRIMARY KEY (id),
    CONSTRAINT products_category_id_fkey FOREIGN KEY (category_id)
        REFERENCES public.categories (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.products
    OWNER to postgres;

-- Table: public.users

-- DROP TABLE IF EXISTS public.users;

CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;