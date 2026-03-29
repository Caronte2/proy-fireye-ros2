import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition  # <-- ¡NUEVA IMPORTACIÓN AQUÍ!
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # --- 1. Definir Rutas y Paquetes ---
    # El paquete estándar de Nav2 que nos ayuda a lanzar todo
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    
    # SU paquete personalizado
    my_nav_package_name = 'proy_fireye_my_nav2_system'
    my_nav_package_dir = get_package_share_directory(my_nav_package_name)

    # --- 2. Declarar Argumentos de Lanzamiento ---
    # Esto permite cambiar el mapa o los parámetros desde la terminal al lanzar.

    # Ruta predeterminada al mapa que guardaron en Paso 1.1 (Asegúrense de cambiar el nombre aquí)
    map_yaml_file_default = os.path.join(my_nav_package_dir, 'map', 'my_map.yaml')
    
    # Ruta predeterminada al archivo burger.yaml que guardaron en Paso 1.2
    params_file_default = os.path.join(my_nav_package_dir, 'param', 'burger.yaml')

    # Otros argumentos útiles (pueden dejarlos como predeterminados)
    use_sim_time = LaunchConfiguration('use_sim_time', default='false') # 'true' si usan Gazebo
    autostart = LaunchConfiguration('autostart', default='true')
    use_rviz = LaunchConfiguration('use_rviz', default='true')
    rviz_config_file_default = os.path.join(my_nav_package_dir, 'rviz', 'fireye_navegation2.rviz')

    declare_use_sim_time_cmd = DeclareLaunchArgument(
        'use_sim_time',
        default_value='false',
        description='Use simulation (Gazebo) clock if true')

    declare_map_yaml_cmd = DeclareLaunchArgument(
        'map',
        default_value=map_yaml_file_default,
        description='Full path to map yaml file to load')

    declare_params_file_cmd = DeclareLaunchArgument(
        'params_file',
        default_value=params_file_default,
        description='Full path to the ROS2 parameters file to use for all launched nodes')
        
    declare_autostart_cmd = DeclareLaunchArgument(
        'autostart',
        default_value='true',
        description='Automatically startup the nav2 stack')

    declare_use_rviz_cmd = DeclareLaunchArgument(
        'use_rviz',
        default_value='true',
        description='Whether to start RViz')
        
    declare_rviz_config_file_cmd = DeclareLaunchArgument(
        'rviz_config_file',
        default_value=rviz_config_file_default,
        description='Full path to the RViz config file to use')


    # --- 3. Incluir el Launch Principal de Nav2 Bringup ---
    # Este es el paso clave. Incluimos el archivo launch estándar de 'nav2_bringup'
    # pero le pasamos NUESTROS argumentos personalizados (mapa y params).
    
    bringup_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': LaunchConfiguration('map'),
            'use_sim_time': use_sim_time,
            'params_file': LaunchConfiguration('params_file'),
            'autostart': autostart
        }.items()
    )

    # --- 4. Incluir RViz (Opcional pero muy útil) ---
    rviz_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_bringup_dir, 'launch', 'rviz_launch.py')
        ),
        launch_arguments={
            'use_sim_time': use_sim_time,
            'rviz_config': LaunchConfiguration('rviz_config_file')
        }.items(),
        condition=IfCondition(LaunchConfiguration('use_rviz')) # <-- ¡CORRECCIÓN AQUÍ!
    )

    # --- 5. Crear la Descripción del Launch ---
    ld = LaunchDescription()

    # Añadir los argumentos declarados
    ld.add_action(declare_use_sim_time_cmd)
    ld.add_action(declare_map_yaml_cmd)
    ld.add_action(declare_params_file_cmd)
    ld.add_action(declare_autostart_cmd)
    ld.add_action(declare_use_rviz_cmd)
    ld.add_action(declare_rviz_config_file_cmd)

    # Añadir las acciones de inclusión (bringup y rviz)
    ld.add_action(bringup_cmd)
    ld.add_action(rviz_cmd)

    return ld