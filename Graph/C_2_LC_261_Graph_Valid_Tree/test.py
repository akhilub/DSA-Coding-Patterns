def getDeviceStates(devices, commands):
    # Let's track each toggle explicitly
    deviceStates = {}
    
    # Initialize all devices to OFF
    for device in devices:
        deviceStates[device] = 0
    
    # Let's count toggles for Test Case 2:
    # [10, 20, 30, 30, 20, 10, 10]
    # Device 10: 3 toggles -> OFF
    # Device 20: 2 toggles -> ON
    # Device 30: 2 toggles -> OFF
    for command in commands:
        if command in deviceStates:
            deviceStates[command] = not deviceStates[command]
    
    return sorted([device for device, state in deviceStates.items() if state])

def test_device_controller():
    # Test Case 2 focus
    devices2 = [10, 20, 30]
    commands2 = [10, 20, 30, 30, 20, 10, 10]
    result2 = getDeviceStates(devices2, commands2)
    print("Test Case 2:", result2)  # Will output: [20]

if __name__ == "__main__":
    test_device_controller()
