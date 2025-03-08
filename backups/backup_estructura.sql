--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4 (Debian 17.4-1.pgdg120+2)
-- Dumped by pg_dump version 17.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dim_cliente; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dim_cliente (
    "IDCliente" bigint,
    "Genero" text,
    "Edad" bigint
);


ALTER TABLE public.dim_cliente OWNER TO admin;

--
-- Name: dim_fecha; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dim_fecha (
    "FechaFactura" timestamp without time zone,
    "IDFecha" bigint,
    "Año" integer,
    "Mes" integer,
    "DíaSemana" text
);


ALTER TABLE public.dim_fecha OWNER TO admin;

--
-- Name: dim_producto; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dim_producto (
    "Categoria" text,
    "IDProducto" bigint
);


ALTER TABLE public.dim_producto OWNER TO admin;

--
-- Name: dim_tienda; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.dim_tienda (
    "CentroComercial" text,
    "IDTienda" bigint
);


ALTER TABLE public.dim_tienda OWNER TO admin;

--
-- Name: ventas; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.ventas (
    "NumFacturaNominal" bigint,
    "IDCliente" bigint,
    "IDProducto" bigint,
    "IDFecha" bigint,
    "IDTienda" bigint,
    "Cantidad" bigint,
    "Precio" double precision,
    "MetodoPago" text
);


ALTER TABLE public.ventas OWNER TO admin;

--
-- PostgreSQL database dump complete
--

