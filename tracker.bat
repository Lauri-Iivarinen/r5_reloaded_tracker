FOR /F "tokens=*" %%i in ('type .env') do SET %%i

::%~dp0

set script_path=%~dp0
del full_log.txt

cd %filepath%


FOR %%i in (aimtrainer_results_*) do (
    forfiles /M %%i /C "cmd /c echo new_log @fdate-@ftime>> full_log.txt"
    type %%i >> full_log.txt
)

copy full_log.txt %script_path%

del full_log.txt

cd %script_path%

call python tracker.py