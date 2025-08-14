pytest -s -v -m "sanity or regression" --html=./Reposts/report.html testcases/ --browser chrome
REM pytest -s -v -m "sanity and regression" --html=./Reposts/report.html testcases/ --browser chrome
REM pytest -s -v -m "sanity" --html=./Reposts/report.html testcases/ --browser chrome
REM pytest -s -v -m "regression" --html=./Reposts/report.html testcases/ --browser chrome