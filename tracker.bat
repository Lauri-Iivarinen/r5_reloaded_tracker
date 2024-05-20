:: Read .env
FOR /F "tokens=*" %%i in ('type .env') do SET %%i

:: Setup variables and files
set script_path=%~dp0
del full_log.txt

:: Read all log files into 1
cd %filepath%
FOR %%i in (aimtrainer_results_*) do (
    forfiles /M %%i /C "cmd /c echo new_log @fdate-@ftime>> full_log.txt"
    type %%i >> full_log.txt
)

:: Copy resulting file back to script directory and run python
copy full_log.txt %script_path%
del full_log.txt
cd %script_path%

cd report
type data.json > old_data.json
cd ..

echo "" > report/data.json
call python tracker.py
del full_log.txt

:: Create variable with report json data
:: because fetching local files in html+js
:: is dumb as fuck
cd report
echo const data=>report.js
type data.json>>report.js
type default.js>>report.js
cd ..

::Open HTML page that shows report
start "" "./report/report.html"