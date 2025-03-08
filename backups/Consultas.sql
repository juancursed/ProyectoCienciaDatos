1. Total de Ventas por Categoría de Producto

SELECT p."Categoria", SUM(v."Cantidad" * v."Precio") AS Total_Ventas
FROM ventas v
JOIN dim_producto p ON v."IDProducto" = p."IDProducto"
GROUP BY p."Categoria"
ORDER BY Total_Ventas DESC;

2. Clientes con Mayor Volumen de Compras

SELECT c."IDCliente", SUM(v."Cantidad" * v."Precio") AS Total_Compras
FROM ventas v
JOIN dim_cliente c ON v."IDCliente" = c."IDCliente"
GROUP BY c."IDCliente"
ORDER BY Total_Compras DESC
LIMIT 10;

3. Métodos de Pago más Utilizados

SELECT "MetodoPago", COUNT(*) AS Frecuencia
FROM ventas
GROUP BY "MetodoPago"
ORDER BY Frecuencia DESC;

4. Comparación de Ventas por Mes

SELECT f."Año", f."Mes", SUM(v."Cantidad" * v."Precio") AS Total_Ventas
FROM ventas v
JOIN dim_fecha f ON v."IDFecha" = f."IDFecha"
GROUP BY f."Año", f."Mes"
ORDER BY f."Año", f."Mes";

Optimización con Índices y Agregaciones

CREATE INDEX idx_ventas_idproducto ON ventas("IDProducto");
CREATE INDEX idx_ventas_idcliente ON ventas("IDCliente");
CREATE INDEX idx_ventas_metodopago ON ventas("MetodoPago");
CREATE INDEX idx_ventas_idfecha ON ventas("IDFecha");

Uso de Agregaciones Materializadas

CREATE MATERIALIZED VIEW ventas_por_categoria AS
SELECT p."Categoria", SUM(v."Cantidad" * v."Precio") AS Total_Ventas
FROM ventas v
JOIN dim_producto p ON v."IDProducto" = p."IDProducto"
GROUP BY p."Categoria";