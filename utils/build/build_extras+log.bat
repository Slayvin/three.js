@echo. >> log.txt
@echo ### %DATE% - %TIME% >> log.txt
@echo  * Building Extras >> log.txt
@echo  * Building Extras
@echo -----------------
@echo.
@python build_log.py --extra 2>>log.txt
@echo.
@pause