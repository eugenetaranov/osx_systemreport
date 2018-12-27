# osx_systemreport
Logs cpu stats, load, power source, battery level into file

## Usage

- Download systemreport.py
- Setup cronjob `*/5 * * * * python <PATH>/systemreport.py --log <LOGFILE>`, replace <PATH> and <LOGFILE> with actual values
