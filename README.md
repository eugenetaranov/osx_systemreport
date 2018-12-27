# osx_systemreport
Logs cpu stats, load, power source, battery level into file

## Usage

- Download systemreport.py
- Setup cronjob `*/5 * * * * python <PATH>/systemreport.py --log <LOGFILE>`, replace `<PATH>` and `<LOGFILE>` with actual values

## Record example
`{"processes": {"running": "2", "total": "437", "sleeping": "435"}, "cpu": {"sys": 21.21, "idle": 70.9, "usr": 7.87}, "ts": "2018-12-27T15:55:00", "power": {"source": "battery", "battery_state": "discharging", "battery_level": 87}, "load_avg": 1.27}`

If you get 'Operation not permitted' when editing crontab, go to System Preferences -> Security & Privacy -> Privacy -> Full disk access, add Terminal or iTerm apps there.
