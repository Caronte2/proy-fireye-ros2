# 🔥 Fireye - Proyecto Robótica ROS 2

Proyecto de robótica basado en ROS 2 cuyo objetivo es la simulación y control de un robot en un entorno personalizado.

---

## 📁 Estructura del proyecto

```
proy-fireye-ros2/
├── src/
│   ├── proy-fireye/          # Código principal del robot
│   ├── proy-fireye_world/    # Mundo de simulación
│
├── build/     # Archivos de compilación (autogenerados)
├── install/   # Archivos de instalación (autogenerados)
├── log/       # Logs de ejecución (autogenerados)
```

---

## ⚙️ Requisitos

* ROS 2 (Humble o compatible)
* colcon
* Python 3
* Gazebo (para simulación)

---

## 🚀 Instalación

Clonar el repositorio:

```
git clone https://github.com/TU_USUARIO/proy-fireye-ros2.git
cd proy-fireye-ros2
```

---

## 🛠️ Compilación

⚠️ Importante: ejecutar siempre desde la raíz del workspace

```
colcon build
```

Después de compilar:

```
source install/setup.bash
```

---

## 🌍 Lanzar el mundo

```
ros2 launch proy-fireye_world fireye_world.launch.py
```

---

## 🤖 Funcionalidades

* Simulación de entorno personalizado
* Control del robot mediante nodos ROS 2
* Comunicación mediante servicios y/o topics
* Ejecución de movimientos (ej: trayectoria circular)

---

## 📸 Resultados

*(Añadir aquí capturas de pantalla de la simulación)*

---

## 👥 Autores

* GRUPO 6
* Pablo Chasi, Imanol Fifuero, Manuel Pérez, Yixuan Chen, Yulin Jiang y Greysy Burgos

---

## 📚 Notas

* Las carpetas `build`, `install` y `log` son generadas automáticamente y no deben modificarse.
* Asegúrate de tener correctamente configurado el entorno ROS 2.

---

## 🧹 .gitignore recomendado

```
build/
install/
log/
```

---

## 📌 Estado del proyecto

🚧 En desarrollo
