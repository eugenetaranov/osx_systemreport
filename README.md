# osx_systemreport
Logs cpu stats, load, power source, battery level into file

## Usage

- Download systemreport.py
- Setup cronjob `*/5 * * * * python <PATH>/systemreport.py --log <LOGFILE>`, replace `<PATH>` and `<LOGFILE>` with actual values

If you get 'Operation not permitted' when editing crontab, go to System Preferences -> Security & Privacy -> Privacy -> Full disk access, add Terminal or iTerm apps there.
