# Bluey

Using the Raspberry Pi and its Bluetooth LE GATT server and a message log from an [In-Situ data logger](https://in-situ.com/en/products/water-level) as a simulator to help test and debug your Bluetooth client app. (This can be adapted to simulate _any_ Bluetooth device!)

![](readme/Bluey.png)
*Images by Pixabay (tree), Freepik (Raspberry Pi, Bluetooth, ladybug, mite), Flat Icons (log), logisstudio (bee), Nsit (cockroach), and Ylivdesign (firefly).*

Based on [Creating BLE GATT Server (UART Service) on Raspberry Pi](https://scribles.net/creating-ble-gatt-server-uart-service-on-raspberry-pi/). Version 1 of the [runme.py](https://github.com/sdiaman1/Bluey/commits/main/runme.py) in this repo is from there, and also Max's instructions are excellent, check them out!

# Getting Started

Copy the `.py` and `.txt` files from this repo to a folder on your Raspberry Pi and run the `runme.py` file.

# How it Works

In the real world, your client app requests [parameter values](https://in-situ.com/en/parameters) (temperature, conductivity, pH, etc.), from In-Situ data loggers (the server), over Bluetooth.

For each request, the response is (may be) different (e.g., temperature at time 1 is 22 degrees C, and at time 2 is 21.9 degrees C).

The request messages are the same, in both cases, but the responses are different.

[In-Situ smarTROLL.txt](https://github.com/sdiaman1/Bluey/commits/main/In-Situ%20smarTROLL.txt) is an example of such messages; both the requests, and the responses, recorded using the [Eltima Serial Port Monitor](https://www.electronic.us/products/serial-port-monitor) app, monitoring a (real) In-Situ smarTROLL data logger's com. (This data logger supports both serial and Bluetooth, and the messages are the same for both.)

One request in _In-Situ smarTROLL.txt_ has many responses, each with different parameter values (e.g., the temperature at the time of measurement).

In the simulation, [messages.py](https://github.com/sdiaman1/Bluey/commits/main/messages.py) reads _In-Situ smarTROLL.txt_, and when the client app requests something, it responds with a random response message (e.g., temperature value) for that request.

Also, [runme.py](https://github.com/sdiaman1/Bluey/commits/main/runme.py)'s service UUID and characteristics were updated to match those of a (real) In-Situ data logger.