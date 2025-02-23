# Bluey-Pi

Using the Raspberry Pi and its Bluetooth LE GATT server to simulate a Bluetooth device.

This code simulates an [In-Situ data logger](https://in-situ.com/en/products/water-level), but it can be adapted to simulate _any_ Bluetooth device (and even other com types, like serial)!

![](readme/Bluey.png)
*Images by Pixabay (tree), Freepik (Raspberry Pi, Bluetooth, ladybug, mite), Flat Icons (log), logisstudio (bee), Nsit (cockroach), and Ylivdesign (firefly).*

Based on [Creating BLE GATT Server (UART Service) on Raspberry Pi](https://scribles.net/creating-ble-gatt-server-uart-service-on-raspberry-pi/). Version 1 of the [runme.py](https://github.com/sdiaman1/Bluey/commits/main/runme.py) in this repo is from there, and also Max's instructions are excellent, check them out!

Getting Started
---------------

Copy the `.py` and `.txt` files from this repo to a folder on your Raspberry Pi and run the `runme.py` file.

How It Works
------------

In the real world, your client app requests [parameter values](https://in-situ.com/en/parameters) (temperature, conductivity, pH, etc.), from In-Situ data loggers (the server), over Bluetooth.

For each request, the response is (may be) different (e.g., temperature at time 1 is 22 degrees C, and at time 2 is 21.9 degrees C).

> The _request_ messages are the same, in both cases, but the _responses_ are different.

[In-Situ smarTROLL.txt](https://github.com/sdiaman1/Bluey/commits/main/In-Situ%20smarTROLL.txt) is an example of such messages; both the requests, and the responses, recorded using the [Eltima Serial Port Monitor](https://www.electronic.us/products/serial-port-monitor) app, monitoring a (real) In-Situ smarTROLL data logger's com. (This data logger supports both serial and Bluetooth, and the messages are the same for both.)

> _One request_ in _In-Situ smarTROLL.txt_ has _many responses_, each with different parameter values (e.g., the temperature at the time of measurement).

In the simulation, [messages.py](https://github.com/sdiaman1/Bluey/commits/main/messages.py) reads _In-Situ smarTROLL.txt_, and when the client app requests something, it responds with a random response message (e.g., temperature value) for that request. (It doesn't need to be random, this code can be updated to use the same order as the real data logger's com, from the recording, e.g., by adding a `current` index to each request message, and incrementing it every time a response is sent for that request.)

Also, [runme.py](https://github.com/sdiaman1/Bluey/commits/main/runme.py)'s service UUID and characteristics were updated to match those of a (real) In-Situ data logger.

When It's Needed
----------------

When you have a limited number of real devices (e.g., In-Situ data loggers), and or when people are scattered in different locations and they need to test and debug your code (e.g., on multiple OSs and phone/tablet models).

There's also some situations (e.g., response messages) that happen rarely in the real world, and a simulator makes it easier to debug them.