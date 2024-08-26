# Cargar las librerías necesarias
install.packages("caret")
install.packages("readxl")
install.packages("tidyverse")
library(caret)
library(readxl)
library(tidyverse)

# Cargar el dataset
ruta_excel <- "C:/Users/jossu/Desktop/Maestria Ciencia de Datos/Vinculación/Jumain.xlsx"
data <- read_excel(ruta_excel, sheet = 1, na = c("N/A"))

# Manejar valores nulos
data <- na.omit(data)

# Exploración básica
summary(data)

# Convertir tipo de discapacidad, grado escolar y nombre de la escuela a factores si no lo están
data$tipo_discapacidad <- as.factor(data$tipo_discapacidad)
data$grado_escolar <- as.factor(data$grado_escolar)
data$nombre_escuela <- as.factor(data$nombre_escuela)

# Entrenar un modelo de regresión lineal
model <- train(porcentaje_discapacidad ~ grado_escolar + tipo_discapacidad + nombre_escuela, data = data, method = "lm")

# Predicción en el conjunto de prueba
predictions <- predict(model, newdata = data)
predictions

# Evaluación del modelo
postResample(predictions, data$porcentaje_discapacidad)
