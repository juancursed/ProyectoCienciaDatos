import kaggle
import pandas as pd
import os
import string

#
# Extracion de datos
#

# Descargar el dataset
path = kagglehub.dataset_download("mehmettahiraslan/customer-shopping-dataset")

# Listar los archivos en el directorio descargado
files = os.listdir(path)
print("Archivos en el dataset:", files)

# Suponiendo que el dataset es un archivo CSV
csv_file = [f for f in files if f.endswith(".csv")][0]  # Toma el primer archivo CSV encontrado
df = pd.read_csv(os.path.join(path, csv_file))

#
# Transformacion de datos
#

# funcion para transformar indice
def convertirIndice(idxString):
    lista_letras = list(string.ascii_lowercase)
    nuevo_idx = ""
    for char in idxString:
        if char.lower() in lista_letras:
            nuevo_idx += str(lista_letras.index(char.lower()))
        else:
            nuevo_idx += char
    return int(nuevo_idx)
        
# Tranformaciones de datos
df['customer_id'] = [convertirIndice(x) for x in df['customer_id']]
df['invoice_no'] = [convertirIndice(x) for x in df['invoice_no']]

# Crear la tabla DimCliente
DimCliente = df[['customer_id', 'gender', 'age']].drop_duplicates().reset_index(drop=True)
DimCliente.rename(columns={'customer_id': 'IDCliente', 'gender': 'Genero', 'age': 'Edad'}, inplace=True)

# Crear la tabla DimProducto
DimProducto = df[['category']].drop_duplicates().reset_index(drop=True)
DimProducto['IDProducto'] = DimProducto.index + 1
DimProducto.rename(columns={'category': 'Categoria'}, inplace=True)

# Crear la tabla DimFecha
df['invoice_date'] = pd.to_datetime(df['invoice_date'], dayfirst=True, errors='coerce')
DimFecha = df[['invoice_date']].drop_duplicates().reset_index(drop=True)
DimFecha['IDFecha'] = DimFecha.index + 1
DimFecha['Año'] = DimFecha['invoice_date'].dt.year
DimFecha['Mes'] = DimFecha['invoice_date'].dt.month
DimFecha['DíaSemana'] = DimFecha['invoice_date'].dt.day_name()
DimFecha.rename(columns={'invoice_date': 'FechaFactura'}, inplace=True)


# Crear la tabla DimTienda
DimTienda = df[['shopping_mall']].drop_duplicates().reset_index(drop=True)
DimTienda['IDTienda'] = DimTienda.index + 1
DimTienda.rename(columns={'shopping_mall': 'CentroComercial'}, inplace=True)


# Fusionar con cada tabla de dimensiones
Ventas = df.merge(DimCliente, left_on='customer_id', right_on='IDCliente')\
           .merge(DimProducto, left_on='category', right_on='Categoria')\
           .merge(DimFecha, left_on='invoice_date', right_on='FechaFactura')\
           .merge(DimTienda, left_on='shopping_mall', right_on='CentroComercial')

# Seleccionar solo las columnas necesarias
Ventas = Ventas[['invoice_no', 'IDCliente', 'IDProducto', 'IDFecha', 'IDTienda', 'quantity', 'price', 'payment_method']]
Ventas.rename(columns={'invoice_no': 'NumFacturaNominal', 'quantity': 'Cantidad', 'price': 'Precio', 'payment_method': 'MetodoPago'}, inplace=True)

import matplotlib.pyplot as plt
import seaborn as sns

# Asegurarse de que la columna de fechas está en formato datetime
df['invoice_date'] = pd.to_datetime(df['invoice_date'])

# Agregar las ventas por mes
ventas_por_mes = df.groupby(df['invoice_date'].dt.month)['price'].sum().reset_index()
ventas_por_mes.columns = ['Mes', 'TotalVenta']

# Crear etiquetas de meses
meses_labels = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
                "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

# Graficar con Matplotlib
plt.figure(figsize=(10, 5))
plt.bar(ventas_por_mes['Mes'], ventas_por_mes['TotalVenta'], color='cornflowerblue')

# Personalización
plt.xticks(ticks=range(1, 13), labels=meses_labels, rotation=45)
plt.xlabel("Mes")
plt.ylabel("Total de Ventas")
plt.title("Comparación de Ventas por Mes")
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()

# Guardar el gráfico en lugar de mostrarlo (útil en entornos no interactivos)
plt.savefig("histograma.png")  # Guarda el gráfico en un archivo
plt.close()  # Cierra la figura para liberar memoria
