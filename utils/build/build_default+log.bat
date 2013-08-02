@echo. >> log.txt
@echo ### %DATE% - %TIME% >> log.txt
@python build_log.py --default 2>>log.txt
@echo.
@rem pause
