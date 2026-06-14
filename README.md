# MSc Drone - Autonomous Environmental Monitoring & Obstacle Avoidance

## Project Overview

This is an MSc final project in Embedded Systems and IoT at Newcastle University. The project focuses on developing an autonomous drone system capable of:

- **Environmental Monitoring**: Collecting sensor data (temperature, humidity, air quality, GPS)
- **Obstacle Avoidance**: Real-time detection and autonomous navigation around obstacles
- **IoT Integration**: Cloud-based data transmission and remote monitoring
- **Embedded Systems**: Optimized real-time control and sensor fusion

## Technology Stack

- **Autopilot**: PX4 (Open-source, research-friendly)
- **Simulator**: Gazebo (Physics-based 3D simulation)
- **Control**: Python (DroneKit-Python) + C++ (Custom firmware extensions)
- **Sensors**: Virtual (Gazebo) + Real sensors (future hardware phase)
- **Communication**: MAVLink protocol, MQTT for IoT
- **Operating System**: Linux/Ubuntu 20.04+

## Project Structure

```
MSc_Drone/
├── README.md
├── docs/
│   ├── SETUP.md                    # Installation and setup guide
│   ├── PROJECT_ROADMAP.md          # Development timeline
│   └── ARCHITECTURE.md             # System architecture
├── src/
│   ├── px4_controller/             # PX4 flight controller code
│   │   ├── main.cpp
│   │   └── CMakeLists.txt
│   ├── drone_controller/           # Python flight control layer
│   │   ├── __init__.py
│   │   ├── offboard_control.py     # Offboard control mode
│   │   └── mission_planner.py      # Autonomous mission planning
│   ├── sensors/                    # Sensor integration modules
│   │   ├── __init__.py
│   │   ├── environmental.py        # Environmental sensors (temp, humidity, air quality)
│   │   ├── distance_sensor.py      # Obstacle detection (rangefinder/lidar)
│   │   └── imu_fusion.py           # IMU data fusion
│   ├── obstacle_avoidance/         # Obstacle avoidance algorithms
│   │   ├── __init__.py
│   │   ├── pathfinding.py          # A* / RRT pathfinding
│   │   └── collision_detection.py  # Real-time collision detection
│   └── iot_communication/          # IoT and cloud integration
│       ├── __init__.py
│       ├── mqtt_client.py          # MQTT publisher/subscriber
│       └── data_logger.py          # Data storage and logging
├── simulations/
│   ├── gazebo_models/              # Custom Gazebo models
│   ├── worlds/                     # Gazebo world files
│   ├── launch_files/               # PX4 + Gazebo launch configs
│   └── test_scenarios/             # Simulation test cases
├── tests/
│   ├── unit_tests/                 # Unit tests for modules
│   └── integration_tests/          # Integration tests with Gazebo
├── requirements.txt                # Python dependencies
├── CMakeLists.txt                  # Build configuration
└── .gitignore
```

## Quick Start

### Prerequisites
- Ubuntu 20.04 LTS or later
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sudar1491/MSc_Drone.git
   cd MSc_Drone
   ```

2. **Follow the detailed setup guide**
   ```bash
   cat docs/SETUP.md
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the project**
   ```bash
   mkdir build && cd build
   cmake ..
   make
   ```

### Running a Simulation

```bash
# Terminal 1: Start PX4 SITL with Gazebo
cd ~/PX4-Autopilot
make px4_sitl gazebo

# Terminal 2: Run the drone controller
cd ~/MSc_Drone
python src/drone_controller/offboard_control.py
```

## Features (Phase by Phase)

### Phase 1: Foundation (Weeks 1-3)
- [x] PX4 & Gazebo setup
- [x] Basic drone control (takeoff, land, navigate)
- [ ] Simulated environmental sensors

### Phase 2: Environmental Monitoring (Weeks 4-6)
- [ ] Multi-sensor data collection
- [ ] Data logging and cloud integration
- [ ] Real-time telemetry dashboard

### Phase 3: Obstacle Avoidance (Weeks 7-10)
- [ ] Obstacle detection (simulated LiDAR)
- [ ] Pathfinding algorithms (A*, RRT)
- [ ] Real-time collision avoidance

### Phase 4: Integration & Testing (Weeks 11-12)
- [ ] End-to-end system testing
- [ ] Performance optimization
- [ ] Documentation & presentation

## Development Documentation

- **[SETUP.md](docs/SETUP.md)** - Detailed installation instructions
- **[PROJECT_ROADMAP.md](docs/PROJECT_ROADMAP.md)** - Timeline and milestones
- **[ARCHITECTURE.md](docs/ARCHITECTURE.md)** - System design and data flow

## Key References

- [PX4 Autopilot Documentation](https://docs.px4.io/)
- [DroneKit-Python](http://dronekit-python.readthedocs.io/)
- [Gazebo Simulation](http://gazebosim.org/)
- [MAVLink Protocol](https://mavlink.io/)

## Author

**Sudar** - MSc Embedded Systems & IoT, Newcastle University

## License

This project is licensed under the MIT License - see LICENSE file for details.

---

**Last Updated**: June 2026
