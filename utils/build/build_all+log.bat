@echo. >> log.txt
@echo ### %DATE% - %TIME% >> log.txt
@echo  * Building All >> log.txt
@echo  * Building All
@echo -----------------
@echo.
@python build_log.py --default --min --extra 2>>log.txt
@echo.
@pause