import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Rutas a los archivos de configuración
    pkg_dir = get_package_share_directory('my_nav2_system')
    nav2_yaml = os.path.join(pkg_dir, 'param', 'burger.yaml')
    map_file = os.path.join(pkg_dir, 'map', 'my_map.yaml')
    rviz_config_dir = os.path.join(pkg_dir, 'rviz', 'tb3_navigation2.rviz')

    return LaunchDescription([
        # 1. Nodo Map Server: Carga el archivo YAML/PGM
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[nav2_yaml, 
                        {'yaml_filename': map_file},
                        {'use_sim_time': True}]
        ),

        # 2. Nodo AMCL: Localización probabilística
        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[nav2_yaml, 
                        {'use_sim_time': True}]
        ),

        # 3. Gestor del Ciclo de Vida: El "interruptor" automático
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[{'use_sim_time': True},
                        {'autostart': True},
                        {'node_names': ['map_server', 'amcl']}]
        ),

        # 4. Visualización en RViz con tu configuración guardada
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_dir],
            parameters=[{'use_sim_time': True}],
            output='screen'
        )
    ])