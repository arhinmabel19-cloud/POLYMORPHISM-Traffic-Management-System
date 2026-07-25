# POLYMORPHISM-Traffic-Management-System

 Overview

This project demonstrates a **Smart Traffic Management System** using **Object-Oriented Programming (OOP)** principles in Python. It showcases how different traffic devices can respond to the same command (`activate()`) in their own unique way using **polymorphism**.



 Objectives

* Implement a parent class "TrafficDevice"
* * Create multiple child classes:

  * "TrafficLight"
  * "SpeedCamera"
  * "PedestrianSignal"
* Override the "activate()" method in each subclass
* Store objects in a list and activate them **without type checking**
* Extend the system by adding a new class ("EmergencySiren") **without modifying existing code**

## Class Structure

###  Parent Class

* **TrafficDevice**

  * Defines the method "activate()" (to be overridden)

### Child Classes

* **TrafficLight**

  * Simulates changing traffic signals
* **SpeedCamera**

  * Detects and captures speed violations
* **PedestrianSignal**

  * Controls pedestrian crossing
* **EmergencySiren**

  * Clears traffic for emergency vehicles

---

## Implementation

```python
# Parent Class
class TrafficDevice:
    def activate(self):
        raise NotImplementedError("Subclasses must override this method")


# Child Classes
class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic Light: Changing signals (Red → Green → Yellow)")


class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed Camera: Capturing speed violations")


class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian Signal: Allowing pedestrians to cross")


# New Class (Added without modifying activation loop)
class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency Siren: Clearing traffic for emergency vehicle")


# Create objects and store in a list
devices = [
    TrafficLight(),
    SpeedCamera(),
    PedestrianSignal(),
    EmergencySiren()
]

# Activate all devices
for device in devices:
    device.activate()
```

---

## Key Concepts

###  Inheritance

All device classes inherit from the "TrafficDevice" parent class.

###  Method Overriding

Each subclass provides its own implementation of the "activate()" method.

### Polymorphism

The same method call ("activate()") behaves differently depending on the object:

```python
for device in devices:
    device.activate()
```

### Extensibility (Open/Closed Principle)

New devices (like "EmergencySiren") can be added **without changing existing code**.

---

##  How to Run

1. Ensure Python is installed on your system
2. Save the code in a file (e.g., `traffic_system.py`)
3. Run the file:

   ```bash
   python traffic_system.py
   ```

---

## Expected Output

```
Traffic Light: Changing signals (Red → Green → Yellow)
Speed Camera: Capturing speed violations
Pedestrian Signal: Allowing pedestrians to cross
Emergency Siren: Clearing traffic for emergency vehicle
```

---

## Conclusion

This project effectively demonstrates how **polymorphism** enables flexible and scalable system design. It avoids complex conditional logic and makes it easy to extend the system with new traffic devices.

---

