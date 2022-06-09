How to use :
- clone repo 
- install python3.7+
- install selenium (pip install selenium)
- add the folder containing chrome driver for selenium (Izicap\chromedriver_win32) to PATH env variable
  - chrome version +102.x.x
- run python script (py main.py)

outcome:
- a navigator opens with automated tests running
- a real-time report in the stdout in the console
- a time-stamped custom-made HTML report is generated in the Izicap/html_reports folder
  - name format of the report : html_report_ddmmyy_hhmmss
  - report contains the following KPIs:
    - title of test
    - duration of test
    - status of test failed/passed (red/green background color)


solutions found :
- CSS_SELECTOR and XPATH don't always work 
    => instead : Full_XPATH

- pause DOM to look for the XPATH of the popups
    => F8 while focus is on devTools