# MX Keys Mini Battery Indicator 🌈⌨️

A lightweight battery indicator for the Logitech MX Keys Mini on Linux.

The indicator reads the keyboard's battery level directly from the BlueZ
`org.bluez.Battery1` D-Bus interface and displays it in the desktop tray
using Ayatana AppIndicator.

## Features

- 🔋 Real-time MX Keys Mini battery percentage
- 🌈 Custom rainbow keyboard tray icon
- 🖥️ Cinnamon / Ayatana AppIndicator
- 🔵 Direct BlueZ battery reading
- 🔄 Automatic battery refresh
- 🐧 Linux

## Requirements

- Linux
- BlueZ
- Python 3
- GTK 3
- Ayatana AppIndicator 3
- Logitech MX Keys Mini connected via Bluetooth

## Usage

```bash
python3 mx-keys-battery.py
```

## Battery source

The indicator reads:

`org.bluez.Battery1`

This provides the MX Keys Mini's actual rechargeable battery level
directly through BlueZ.

## License

MIT License. See `LICENSE`.
